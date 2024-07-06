package main

import "fmt"

func main() {
	var weight float64
	var result float64
	fmt.Printf("What is your weight in pounds ")
	fmt.Scanf("%f", &weight)
	result = weight / 2.20462
	fmt.Printf("%.2f\n", result)
	if weight == 0 {
		fmt.Println("ERROR")
	}
}
