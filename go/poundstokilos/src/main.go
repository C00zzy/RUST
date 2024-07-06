package main

import "fmt"

func poundstokilos(pounds float64) float64 {
	return pounds * 0.453592
}

func main() {
	pounds := 180.0
	kilograms := poundstokilos(pounds)
	fmt.Printf("%.2f pounds is equal to %.2f kilograms\n", pounds, kilograms)
}
