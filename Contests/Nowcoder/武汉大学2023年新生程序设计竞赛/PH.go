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

	var n, k int
	Fscan(in, &n, &k)
	if k < n {
		Fprintln(out, 0)
	} else {
		Fprintln(out, 1-2*(n&1))
	}
}

func main() { solve(os.Stdin, os.Stdout) }
