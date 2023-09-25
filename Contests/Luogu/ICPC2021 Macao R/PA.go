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

	var T, n int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		ans := []int{}
		a := make([]int, n)
		s := 0
		for i := 0; i < n; i++ {
			for j := range a {
				Fscan(in, &a[j])
			}
			if i&1 == 0 {
				for _, v := range a {
					if len(ans) > 0 {
						if v > ans[len(ans)-1] {
							s--
						} else {
							s++
						}
					}
					ans = append(ans, v)
				}
			} else {
				for j := n - 1; j >= 0; j-- {
					if a[j] > ans[len(ans)-1] {
						s--
					} else {
						s++
					}
					ans = append(ans, a[j])
				}
			}
		}

		if s >= 0 {
			for i := 0; i < n*n; i++ {
				if i > 0 {
					Fprint(out, " ")
				}
				Fprint(out, ans[i])
			}
		} else {
			for i := n*n - 1; i >= 0; i-- {
				if i < n*n-1 {
					Fprint(out, " ")
				}
				Fprint(out, ans[i])
			}
		}
		Fprintln(out)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
