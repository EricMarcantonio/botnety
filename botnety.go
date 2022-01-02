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
	lol := `{ "commands": ["echo 'hello worl'"]}`
	response := RESPONSE{}
	err := json.Unmarshal([]byte(lol), &response)
	if err != nil {
		return
	}
	//requestTodoAndParse(&response, "https://jsonplaceholder.typicode.com/posts/1")
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
