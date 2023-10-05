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

	var T, n, m int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &m)
		levels := []int{}
		levelc := []int{}

		k := 0

		var dfs func(s, t, l, p int)
		dfs = func(s, t, l, p int) {
			if l > k {
				levels = append(levels, 0)
				levelc = append(levelc, 0)
				k++
			}
			levels[l-1] += p
			levelc[l-1] += 1
			if s == t {
				return
			}
			mid := (s + t) / 2
			dfs(s, mid, l+1, p*2)
			dfs(mid+1, t, l+1, p*2+1)
		}
		dfs(1, n, 1, 1)
		for i := 1; i < k; i++ {
			levels[i] += levels[i-1]
			levelc[i] += levelc[i-1]
		}
		// Fprintln(out, k)
		if m > levelc[k-1]-1 {
			Fprintln(out, -1)
		} else {
			for i := k - 1; i >= 0; i-- {
				if m <= levelc[k-1]-levelc[i] {
					Fprintln(out, levels[i]/(i+1))
					break
				}
			}
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
