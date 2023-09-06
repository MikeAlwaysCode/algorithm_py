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

	var T, n, k int
	var x int64
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &k, &x)
		a := make([]int64, n)
		var ans int64
		mx := make([]int64, k)
		tot := make([]int64, k)
		cnt := make([]int64, k)
		for i := range a {
			Fscan(in, &a[i])
			d := i % k
			ans = max(ans, a[i])
			mx[d] = max(mx[d], a[i])
			cnt[d]++
			tot[d] += a[i]
		}

		for i := 0; i < k; i++ {
			x -= mx[i]*cnt[i] - tot[i]
		}

		if x < 0 {
			Fprintln(out, -1)
			continue
		}

		for i := 0; i < k; i++ {
			ans = max(ans, mx[i]+x/cnt[i])
		}

		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int64) int64 {
	if a >= b {
		return a
	} else {
		return b
	}
}
