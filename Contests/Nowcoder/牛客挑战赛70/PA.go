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

	var n, k int
	var s string
	Fscan(in, &n, &k)
	Fscan(in, &s)
	if k == 1 {
		Fprintln(out, 0)
		return
	}
	ans := k - 1
	for i := 0; i < n*2-1; i++ {
		l, r := i/2, (i+1)/2
		for l >= 0 && r < n && s[l] == s[r] {
			l--
			r++
		}
		if r-l-1 >= k {
			Fprintln(out, 0)
			return
		}
		if r-l <= 2 {
			continue
		}
		cnt, len := 0, r-l-1
		for len < k && (l >= 0 || r < n) {
			if l >= 0 && r < n && s[l] == s[r] {
				l--
				r++
				len += 2
			} else if l >= 0 && s[l] == s[l+1] {
				cnt++
				l--
				len += 2
			} else if r < n && s[r] == s[r-1] {
				cnt++
				r++
				len += 2
			} else {
				break
			}
		}
		ans = min(ans, max(k-len, 0)+cnt)

	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
