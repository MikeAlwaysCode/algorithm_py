package main

import (
	"bufio"
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
	const mod int64 = 1e9 + 7
	pow := func(x, n int64) int64 {
		x %= mod
		res := int64(1)
		for ; n > 0; n /= 2 {
			if n%2 > 0 {
				res = res * x % mod
			}
			x = x * x % mod
		}
		return res
	}

	var n int64
	Fscan(in, &n)
	var corner, edge, center int64
	// (1 + 2 + 3 + 4) * 2
	corner = 20
	if n > 2 {
		// sum(5 .. (4n - 4)) * 3
		// edge = (5 + 4*n - 4) * (4*n - 8) / 2 * 3 % mod
		edge = (5 + 4*n - 4) % mod * (4*n - 8) % mod * 3 % mod * pow(2, mod-2) % mod
		// sum((4n - 3) ... (n ^ 2)) * 4
		center = (4*n - 3 + pow(n, 2)) % mod * (pow(n, 2) - (4*n-4)%mod + mod) % mod * 2 % mod
	}
	ans := (corner + edge + center) % mod
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
