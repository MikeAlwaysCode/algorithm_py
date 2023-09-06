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

	var n, T, v, t int
	ans, mx := 1, 0
	Fscan(in, &n, &T)
	for i := 1; i <= n; i++ {
		Fscan(in, &v, &t)
		h := v * (T - t)
		if h > mx {
			ans, mx = i, h
		}
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
