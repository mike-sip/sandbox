package main

import (
	"fmt"
	"golang/utils" // Import d’un package local
)

func main() {
	message := utils.GetGreeting("Go")
	fmt.Println(message)
}
