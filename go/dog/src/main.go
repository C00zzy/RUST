package main

import "fmt"

func main() {
	var age int
	var result int
	fmt.Printf("What is your age: ")
	fmt.Scanf("%d", &age)
	result = age * 7
	fmt.Println(result)

}
