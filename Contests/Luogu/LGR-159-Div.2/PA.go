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

	var T, op, n, x int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &op, &n, &x)
		if x < n-1 {
			Fprintln(out, -1)
			continue
		}
		if op == 1 {
			for i := 0; i < n-2; i++ {
				Fprint(out, 1, " ")
			}
			Fprint(out, x-n+2, " ")
			Fprintln(out, x-n+2)
		} else {
			for i := 0; i < n-1; i++ {
				Fprint(out, 1, " ")
			}
			Fprintln(out, x-n+2)
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
