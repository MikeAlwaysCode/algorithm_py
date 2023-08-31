package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, p, pp int
	Fscan(in, &n)
	for i := 0; i < n; i++ {
		pp = p
		Fscan(in, &p)
	}
	if p > pp+1 || (p-n)%2 == 0 {
		Fprintln(out, "Alice")
	} else {
		Fprintln(out, "Bob")
	}
}

func main() { solve(os.Stdin, os.Stdout) }
