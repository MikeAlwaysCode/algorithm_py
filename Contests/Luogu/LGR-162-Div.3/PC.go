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
		a := make([]int, n)
		t := make([]int, n)
		for i := range a {
			Fscan(in, &a[i])
			t[i] += a[i]
			t[n-1-i] += a[i]
		}
		mx := int(1e9)
		ans := false
		b := make([]int, n)
		for i := range b {
			Fscan(in, &b[i])
			if t[i] > 0 {
				mx = min(mx, b[i]/t[i])
			}
		}
		if mx > 10000 {
			Fprintln(out, "No")
			continue
		}

		for k := 0; k <= mx; k++ {
			res := -1
			for i := range b {
				if (b[i]-t[i]*k)%a[i] > 0 {
					res = -1
					break
				} else if res == -1 {
					res = (b[i] - t[i]*k) / a[i]
				} else if res != (b[i]-t[i]*k)/a[i] {
					res = -1
					break
				}
			}
			if res != -1 {
				ans = true
				break
			}
		}

		if ans {
			Fprintln(out, "Yes")
		} else {
			Fprintln(out, "No")
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
