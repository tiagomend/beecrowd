package main

import ("fmt")

func main(){
	var a, b int
	fmt.Scan(&a)
	fmt.Scan(&b)
	prod := a * b
	fmt.Printf("PROD = %d\n", prod)
}