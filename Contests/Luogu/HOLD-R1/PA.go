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

	var m, a, b int
	Fscan(in, &m, &a, &b)

	for b&2 == 0 || b&1 > 0 {
		b -= 1
	}
	b -= 2
	if b == 0 {
		b = 1
	}

	Fprintln(out, b)
}

func main() { solve(os.Stdin, os.Stdout) }
