package main

import ("fmt")

func averageOne() string {
	var a, b float64
	weightOfA := 3.5
	weightOfB := 7.5

	// Lê os valores de entrada
	fmt.Scan(&a)
	fmt.Scan(&b)

	// Calcula a média ponderada
	media := (a*weightOfA + b*weightOfB) / (weightOfA + weightOfB)

	// Retorna o resultado formatado
	return fmt.Sprintf("MEDIA = %.5f", media)
}

func main() {
	fmt.Println(averageOne())
}
