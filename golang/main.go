package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("Hello, World! Welcome to 'Try to guess the number' !")

	number := rand.Intn(100)
	fmt.Println(number)
	count := 0

	var guess int

	for {
		fmt.Print("Enter a number between 0 and 100:")
		fmt.Scan(&guess)
		count++

		if guess == number {
			fmt.Println("You guessed it in", count, "tries!")
			break
		} else if guess < number {
			fmt.Println("Too low!")
		} else {
			fmt.Println("Too high!")
		}
	}
}
