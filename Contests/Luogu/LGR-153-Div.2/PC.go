package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	type pair struct{ a, b int64 }

	var n int
	var a, b, mx, ans, s int64
	Fscan(in, &n)
	rev := []pair{}
	for i := 0; i < n; i++ {
		Fscan(in, &a, &b)
		mx = max(mx, a)
		mx = max(mx, b)
		if a > b {
			rev = append(rev, pair{a, b})
		}
	}
	sort.Slice(rev, func(i, j int) bool {
		if rev[i].b == rev[j].b {
			return rev[i].a >= rev[j].a
		} else {
			return rev[i].b >= rev[j].b
		}
	})
	last := mx
	for _, r := range rev {
		if r.b >= last {
			continue
		} else {
			if r.a > last {
				s += last - r.b
			} else {
				s += r.a - r.b
			}
			last = r.b
		}
	}
	ans = mx + s*2
	last = mx
	for _, r := range rev {
		if r.b >= last {
			continue
		}
		if r.a > last {
			s -= last - r.b
		} else {
			s -= r.a - r.b
		}
		last = r.b
		ans = min(ans, mx+mx-r.b+s*2)
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int64) int64 {
	if a >= b {
		return a
	} else {
		return b
	}
}
func min(a, b int64) int64 {
	if a <= b {
		return a
	} else {
		return b
	}
}
