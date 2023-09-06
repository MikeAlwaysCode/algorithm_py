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

	var s, a int
	for i := 0; i < 5; i++ {
		Fscan(in, &a)
		s += a
	}
	if s < 100 {
		Fprintln(out, "Gray")
	} else if s < 120 {
		Fprintln(out, "Blue")
	} else if s < 170 {
		Fprintln(out, "Green")
	} else if s < 230 {
		Fprintln(out, "Orange")
	} else {
		Fprintln(out, "Red")
	}
}

func main() { solve(os.Stdin, os.Stdout) }
