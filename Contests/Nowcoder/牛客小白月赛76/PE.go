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

	var T, n int
	var s string
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		Fscan(in, &s)

		ans := 0
		k := 0
		for i := 0; i < n; i++ {
			if s[i] == '(' {
				if k > 0 {
					ans += k
				}
				k--
			} else {
				k++
			}
		}

		if k == 0 {
			Fprintln(out, ans)
		} else {
			Fprintln(out, -1)
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
