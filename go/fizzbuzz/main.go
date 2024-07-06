package main

import "fmt"

func main() {
	for i := 0; i < 100; i++ {
		fmt.Println(i)
		if i%3 == 0 && i%5 == 0 {
			fmt.Println("FizzBuzz")
		} else if i%3 == 0 {
			fmt.Println("Buzz")
		} else if i%5 == 0 {
			fmt.Println("Fizz")
		}
	}
}
