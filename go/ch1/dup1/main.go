package main

import (
	// "bufio"
	"fmt"
	// "os"
)

// func main() {
// 	counts := make(map[string]int)
// 	input := bufio.NewScanner(os.Stdin)
// 	fmt.Println(input.Scan())
// 	if input.Scan() {
// 		counts[input.Text()]++
// 	}
// 	fmt.Println("plseas input")
// 	// NOTE: ignoring potential errors from input.Err()
// 	for line, n := range counts {
// 		fmt.Printf(">>%d\t%s<<\n", n, line)
// 	}

// }

func main() {
	// counts := make(map[string]int)
	s1 := "dasd"
	for n, w := range s1 {
		fmt.Printf("%c\t%d\n", w, n)
		fmt.Printf("%v\t%d\n", w, n)
		fmt.Printf("%T\t%d\n", w, n)
		fmt.Printf("%q\t%d\n", w, n)
		fmt.Printf("%t\t%d\n", w, n)
	}
}
