package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func Solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, n int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)

		if n == 0 {
			Fprintln(out, 5, 4, 3, 7)
		} else {
			a := 1 << 33
			b := 1 << 35
			c := 3 << 33
			d := c + n
			Fprintln(out, a, b, c, d)
		}
	}
}

func main() { Solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
