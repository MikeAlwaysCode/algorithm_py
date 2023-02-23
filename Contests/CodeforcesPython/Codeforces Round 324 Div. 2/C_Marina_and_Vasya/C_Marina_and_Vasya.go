package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func CF584C(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, t int
	Fscan(in, &n, &t)
	var s1, s2 string
	Fscan(in, &s1)
	Fscan(in, &s2)

	var diff, each, more, e1, e2 int
	for i := 0; i < n; i++ {
		if s1[i] != s2[i] {
			diff++
		}
	}
	if t > diff {
		more = t - diff
	} else if diff > t {
		each = diff - t
	}
	if each*2 > diff {
		Fprintln(out, -1)
		return
	}

	ans := make([]byte, n)
	for i := 0; i < n; i++ {
		if s1[i] != s2[i] {
			if e1 < each {
				ans[i] = s2[i]
				e1++
			} else if e2 < each {
				ans[i] = s1[i]
				e2++
			} else {
				for c := 'a'; c <= 'z'; c++ {
					if c != rune(s1[i]) && c != rune(s2[i]) {
						ans[i] = byte(c)
						break
					}
				}
			}
		} else {
			if more > 0 {
				for c := 'a'; c <= 'z'; c++ {
					if c != rune(s1[i]) {
						ans[i] = byte(c)
						break
					}
				}
				more--
			} else {
				ans[i] = s1[i]
			}
		}
	}

	Fprintln(out, string(ans))
}

func main() { CF584C(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
