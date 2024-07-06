package main

import "fmt"

func forloop(max int) {
	if max > 0 {
		forloop(max - 1)
	}
	fmt.Println(max)
}

func main() {
	forloop(100)
}
