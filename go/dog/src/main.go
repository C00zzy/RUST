package main

import "fmt"

func calculateage() int {
	var age int = 10
	return age
}

func caldogyears(age int) int {
	var dogyears int = age * 7
	return dogyears
}

func main() {
	age := calculateage()

	dogyears := caldogyears(age)

	fmt.Println(age)
	fmt.Println(dogyears)
}
