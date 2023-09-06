package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var x int
	Fscan(in, &x)

	if x%2 == 0 || x%3 == 0 || x%5 == 0 || x%7 == 0 {
		Fprintln(out, "YES")
	} else {
		Fprintln(out, "NO")
	}
}

func main() { solve(os.Stdin, os.Stdout) }
