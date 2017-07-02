package main

import (
	"fmt"
)

type Tz int

func main() {
	var a Tz
	a.Print()
}

func (*Tz) Print() {
	fmt.Println("TZ")
}
