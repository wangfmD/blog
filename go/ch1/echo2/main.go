package main

import (
	"fmt"
	"os"
)

func main() {
	s, sep := "", ""
	// for _, arg := range os.Args[1:] {
	// 	s += sep + arg
	// 	sep = " "
	// }
	// fmt.Println(s)
	for line, arg := range os.Args[1:] {
		s += sep + arg
		sep = " "
		fmt.Println(line, s)
	}
	fmt.Println(s)
}
