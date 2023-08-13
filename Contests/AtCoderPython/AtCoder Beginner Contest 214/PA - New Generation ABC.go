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

	var n int
	Fscan(in, &n)
	if n <= 125 {
		Fprintln(out, 4)
	} else if n <= 211 {
		Fprintln(out, 6)
	} else {
		Fprintln(out, 8)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
