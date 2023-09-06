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

	var T, n, u, v int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		g := make([][]int, n)
		for i := 1; i < n; i++ {
			Fscan(in, &u, &v)
			u--
			v--
			g[u] = append(g[u], v)
			g[v] = append(g[v], u)
		}
		cnt := make([]int, n)
		v := make([]int, n)
		for i := range v {
			Fscan(in, &v[i])
		}
		sort.Ints(v)

		var dfs func(x, p int)
		dfs = func(x int, p int) {
			cnt[x] = 1
			if p >= 0 {
				cnt[x] += cnt[p]
			}
			for _, y := range g[x] {
				if y != p {
					dfs(y, x)
				}
			}
		}
		dfs(0, -1)
		sort.Ints(cnt)

		ans := 0
		for i, c := range cnt {
			ans += c * v[i]
		}
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
