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

	var T, n, m, k, b int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &m, &k, &b)
		h := make([]int, n)
		a := make([]int, n)

		for i := range h {
			Fscan(in, &h[i])
		}
		for i := range a {
			Fscan(in, &a[i])
		}
		if m > 1 {
			for i, v := range h {
				t := 1
				if v <= k {
					t += (k - v + a[i]) / a[i]
				}
				if t > m {
					h[i] += (m - 1) * a[i]
					continue
				}
				t = m - t
				r := int((k - b + a[i]) / a[i])
				t %= r
				h[i] = b + t*a[i]
			}
		}

		for _, v := range h {
			Fprint(out, v, " ")
		}
		Fprintln(out)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
