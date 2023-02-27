package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func CF1659D(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, n, a int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		ans := make([]int, n)
		for i := range ans {
			ans[i] = 1
		}
		first := true
		for i, v := range ans {
			Fscan(in, &a)
			if a > 0 {
				if first || v == 1 {
					first = false
					if a < n {
						ans[a] = 0
					}
				} else {
					if i+a < n {
						ans[i+a] = 0
					}
				}
			} else {
				ans[i] = 0
			}
		}

		for _, v := range ans {
			Fprint(out, v, " ")
		}
		Fprintln(out)
	}
}

func main() { CF1659D(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
