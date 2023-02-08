package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func CF1442A(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, n int
	var left, pre, a int
	var ans bool
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		Fscan(in, &left)
		pre = 0
		ans = true
		for ; n > 1; n-- {
			Fscan(in, &a)

			if ans {
				if a < pre {
					ans = false
				}
				left = min(left, a-pre)
				pre = a - left
			}
		}

		if ans {
			Fprintln(out, "YES")
		} else {
			Fprintln(out, "NO")
		}
	}
}

func main() { CF1442A(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
