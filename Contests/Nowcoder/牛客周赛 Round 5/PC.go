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

	var n int
	var l, r int64
	var s string
	var u, v int

	Fscan(in, &n, &l, &r)
	Fscan(in, &s)

	var ans int64
	g := make([][]int, n)

	for i := 0; i < n-1; i++ {
		Fscan(in, &u, &v)
		u--
		v--
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}

	var f func(x, p int, nums int64) int64
	f = func(x, p int, nums int64) int64 {
		var res int64
		if nums >= l && nums <= r {
			res++
		} else if nums > r {
			return res
		}
		for _, y := range g[x] {
			if y == p {
				continue
			}
			res += f(y, x, nums*2+int64(s[y]-'0'))
		}

		return res
	}

	for i := 0; i < n; i++ {
		nums := int64(s[i] - '0')
		for _, x := range g[i] {
			ans += f(x, i, nums*2+int64(s[x]-'0'))
		}
	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
