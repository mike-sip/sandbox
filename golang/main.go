package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Print("Entrez le premier nombre : ")
	fmt.Scanln(&a)
	fmt.Print("Entrez le deuxième nombre : ")
	fmt.Scanln(&b)

	fmt.Println("Addition :", a+b)
	fmt.Println("Soustraction :", a-b)
	fmt.Println("Multiplication :", a*b)
	if b != 0 {
		fmt.Println("Division :", a/b)
	} else {
		fmt.Println("Division par zéro impossible")
	}
	fmt.Println("Modulo :", a%b)
}
