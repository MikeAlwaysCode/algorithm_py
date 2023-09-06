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

	var n int
	Fscan(in, &n)
	var s, ans int64
	a := make([]int64, n)
	for i := range a {
		Fscan(in, &a[i])
		s += a[i]
	}
	if s%int64(n) == 0 {
		k := s / int64(n)
		for _, v := range a {
			ans += abs(v - k)
		}
		Fprintln(out, ans/2)
	} else {
		sort.SliceStable(a, func(i, j int) bool {
			return a[i] <= a[j]
		})
		f := func(nums []int64, s int64) (res int64) {
			n := int64(len(nums))
			k := s / n
			var l, r int64
			for _, v := range nums {
				if v >= k {
					r += v - k
				} else {
					l += k - v
				}
			}
			res = max(l, r)
			if s%n > 0 {
				k++
				l, r = 0, 0
				for _, v := range nums {
					if v >= k {
						r += v - k
					} else {
						l += k - v
					}
				}
				res = min(res, max(l, r))
			}
			return
		}
		Fprintln(out, min(f(a[1:], s-a[0]), f(a[:n-1], s-a[n-1])))
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func abs(x int64) int64 {
	if x < 0 {
		return -x
	} else {
		return x
	}
}
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
