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

	const mod = 998244353

	var n, a, s int
	var f, g [90001]int
	f[0], g[0] = 3, 3
	ans := 1
	Fscan(in, &n)
	for i := 0; i < n; i++ {
		Fscan(in, &a)
		s += a
		for j := s; j >= 0; j-- {
			f[j] = (f[j]*2 + f[max(j-a, 0)]) % mod
			if j >= a {
				g[j] = (g[j] + g[j-a]) % mod
			}
		}
		ans = ans * 3 % mod
	}
	if s&1 == 0 {
		f[s/2] = (f[s/2] - g[s/2] + mod) % mod
	}
	ans = (ans - f[(s+1)/2] + mod) % mod
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
