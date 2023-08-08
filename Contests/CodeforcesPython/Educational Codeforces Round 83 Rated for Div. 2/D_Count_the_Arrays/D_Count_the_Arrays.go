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

	var m, n int
	Fscan(in, &m, &n)

	const mod int64 = 998244353
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
	// 阶乘
	fact := make([]int64, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * int64(i) % mod
	}
	// 逆元
	inverse := make([]int64, n+1)
	inverse[n] = pow(fact[n], mod-2)
	for i := n; i > 0; i-- {
		inverse[i-1] = inverse[i] * int64(i) % mod
	}
	// 组合数
	comb := func(n, m int64) int64 {
		if m < 0 || m > n {
			return 0
		}
		return fact[n] * inverse[m] % mod * inverse[n-m] % mod
	}
	ans := comb(int64(n), int64(m-1)) % mod * int64(m-2) % mod * pow(2, int64(m-3)) % mod
	Fprintln(out, ans)

}

func main() { solve(os.Stdin, os.Stdout) }
