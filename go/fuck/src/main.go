package main

func main() {
	for i := 0; i < 100; i++ {
		if i%2 == 0 {
			println("EVEN", i)
		} else {
			println("ODD", i)
		}
	}
}
