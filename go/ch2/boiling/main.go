package main

import (
	"fmt"
)

const BoilingF = 212.0 //dd

func main() {
	var f = BoilingF
	var c = (f - 32) * 5 / 9
	fmt.Printf("%g,%g", BoilingF, c)
}
