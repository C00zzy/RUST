package main

import "fmt"

func main() {
	var name string
	fmt.Printf("What is your name: ")
	fmt.Scanln(&name)
	fmt.Println("Your name is", name)
}
