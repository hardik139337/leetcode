package main

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
)

type MyStruct struct {
	Field1 string
	Field2 int
}

func calculateHash(s any) string {
	// Convert the struct to a byte slice
	data := []byte(fmt.Sprintf("%+v", s))

	// Calculate the SHA-256 hash of the byte slice
	hash := sha256.Sum256(data)

	// Convert the hash to a hexadecimal string
	hashString := hex.EncodeToString(hash[:])

	return hashString
}

func main() {
	myStruct := MyStruct{
		Field1: "Hello",
		Field2: 42,
	}

	// Calculate the hash of the struct
	hash := calculateHash(myStruct)

	fmt.Println("Hash of the struct:", hash)
}
