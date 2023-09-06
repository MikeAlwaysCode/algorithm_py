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
	type pair struct{ x, y int64 }

	var T, n int
	var x, y int64
	var s string
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &x, &y)
		Fscan(in, &s)
		var cx, cy int64
		var ok bool
		for _, c := range s {
			if c == 'U' {
				cy++
			} else if c == 'D' {
				cy--
			} else if c == 'L' {
				cx--
			} else {
				cx++
			}
			if cx == x && cy == y {
				ok = true
				break
			}
		}
		if ok {
			Fprintln(out, "Yes")
		} else {
			Fprintln(out, "No")
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
