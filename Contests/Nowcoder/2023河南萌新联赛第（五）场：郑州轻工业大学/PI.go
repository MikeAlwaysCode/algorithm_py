package main

import (
	"bufio"
	"sort"

	// "container/heap"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, n int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		a := make([]int, n)
		b := make([]int, n)
		for i := range a {
			Fscan(in, &a[i])
		}
		eq := 0
		for i := range b {
			Fscan(in, &b[i])
			if a[i] == b[i] {
				eq++
			}
		}
		ans := eq * (eq - 1) / 2
		idx := make([]int, n)
		for i := 0; i < n; i++ {
			idx[i] = i
		}
		sort.Slice(idx, func(i, j int) bool {
			return a[idx[i]]*b[idx[j]] <= a[idx[j]]*b[idx[i]]
		})
		i, j := 0, n-1
		for i < j && a[idx[i]]*b[idx[j]] != a[idx[j]]*b[idx[i]] {
			if a[idx[i]]*a[idx[j]] < b[idx[i]]*b[idx[j]] {
				i++
			} else if a[idx[i]]*a[idx[j]] > b[idx[i]]*b[idx[j]] {
				j--
			} else {
				cnt1, cnt2 := 1, 1
				for i < j && a[idx[i]]*b[idx[i+1]] == b[idx[i]]*a[idx[i+1]] {
					cnt1++
					i++
				}
				for j > i && a[idx[j]]*b[idx[j-1]] == a[idx[j-1]]*b[idx[j]] {
					cnt2++
					j--
				}
				ans += cnt1 * cnt2
				i++
				j--
			}
		}

		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
