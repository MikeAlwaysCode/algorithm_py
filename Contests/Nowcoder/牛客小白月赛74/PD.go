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

	var T, n, m int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &m)
		a := make([]int, n)
		ans := 0
		sub := []int{}
		for i := range a {
			Fscan(in, &a[i])
			ans += a[i]
			if a[i] > 0 {
				sub = append(sub, a[i]*(n-i))
			}
		}
		if len(sub) > 0 {
			sort.Sort(sort.Reverse(sort.IntSlice(sub)))
			for i := 0; i < len(sub) && i < m; i++ {
				ans -= sub[i]
			}
		}

		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
