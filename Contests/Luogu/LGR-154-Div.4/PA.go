package main

import (
	"bufio"
	// "container/heap"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var a, b, c, d int
	Fscan(in, &a, &b, &c, &d)
	if a+b+c+d < 51 {
		Fprintln(out, "Rabbit wins")
	} else {
		Fprintln(out, "Rabbit lose")
	}
}

func main() { solve(os.Stdin, os.Stdout) }
