package main

import "fmt"

func hellostring(num int) {
	fmt.Println(num)
}

func loop(i, max int) {
	if i < max {
		hellostring(i)
		loop(i+1, max)
	}
}

func main() {
	loop(0, 100)
}
