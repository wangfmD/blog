package main

import (
	"fmt"
)

func main() {
	// sliceOne()
}

func sliceOne() {
	s1 := make([]int, 3, 10)
	s1[0] = 1
	sa := s1[0:3]
	sb := s1[1:3]
	fmt.Println(sa, sb)
	fmt.Println(s1, cap(s1))
	for i, v := range s1 {
		fmt.Println(i, v, &i)
	}
}

func sliceTwo() {
	s1 := make([]int, 3, 6)
	fmt.Println(s1)
}

// func sl()
