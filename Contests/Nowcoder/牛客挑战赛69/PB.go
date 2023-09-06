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

	var n int
	Fscan(in, &n)
	var a int
	for i := 1; i < n; i++ {
		Fscan(in, &a)
	}

	Fprintln(out, "David")
}

func main() { solve(os.Stdin, os.Stdout) }
