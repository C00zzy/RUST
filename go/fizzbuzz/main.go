package main

import "fmt"

// fizzbuzz

func fizzbuzz(value int) string {
	if value%3 == 0 && value%6 == 0 {
		return "FizzBuzz"
	} else if value%3 == 0 {
		return "Fizz"
	} else if value%5 == 0 {
		return "Buzz"
	} else {
		return fmt.Sprint("NONE: ", value)
	}
}

func forloop(start, end int, action func(int) string) {
	for i := start; i <= end; i++ {
		fmt.Println(action(i))
	}
}

func main() {
	forloop(1, 100, fizzbuzz)
}
