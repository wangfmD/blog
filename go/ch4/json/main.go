package main

import (
	"fmt"
	"encoding/json"
	"log"
)

type Movie struct{
	Title string
	Year int
	Color bool
	Actors []string
}

var movies = []Movie{
    {Title: "Casablanca", 
		Year:1942, 
		Color: false,
        Actors:[]string{"Humphrey Bogart", "Ingrid Bergman"}},
}

func main (){
	// data, err := json.Marshal(movies)
	data, err := json.MarshalIndent(movies, "", "    ")
	if err != nil {
		log.Fatalf("JSON marshaling failed: %s", err)
	}
	fmt.Printf("%s\n", data)
}
