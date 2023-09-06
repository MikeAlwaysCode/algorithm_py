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

	var T, n, m int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &m)
		if m < n-m {
			Fprintln(out, m, n-m)
		} else {
			Fprintln(out, -1)
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
