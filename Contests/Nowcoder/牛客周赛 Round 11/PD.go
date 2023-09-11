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

	const mod int64 = 1e9 + 7
	var n, k int
	Fscan(in, &n, &k)
	a := make([]int, n)
	for i := range a {
		Fscan(in, &a[i])
	}
	k = n - k
	if k == 0 {
		Fprintln(out, 1)
		return
	} else if k == 1 {
		Fprintln(out, n)
		return
	}
	sort.Ints(a)
	cnt := make([][]int64, n)
	for i := range cnt {
		cnt[i] = make([]int64, k)
		cnt[i][1] = 1
	}
	var ans int64
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if a[j]%a[i] == 0 {
				for m := 1; m < k; m++ {
					if m == k-1 {
						ans = (ans + cnt[i][m]) % mod
					} else {
						cnt[j][m+1] = (cnt[j][m+1] + cnt[i][m]) % mod
					}
				}
			}
		}
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
