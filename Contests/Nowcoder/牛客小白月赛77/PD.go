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
	type pair struct{ a, b int64 }

	var n, m, k int
	var s string

	Fscan(in, &n, &m, &k)
	Fscan(in, &s)

	ans := 0
	cnt := map[pair]int{}
	mp := map[pair]int{}

	const mod int64 = 998244353
	var h1, h2, base1, base2, q1, q2 int64
	base1 = int64(27)
	base2 = int64(1331)
	q1 = int64(1)
	q2 = int64(1)
	for i := 0; i < m; i++ {
		c := int64(s[i] - '0')
		h1 = (h1*base1 + c) % mod
		h2 = (h2*base2 + c) % mod
		if i > 0 {
			q1 = q1 * base1 % mod
			q2 = q2 * base2 % mod
		}
	}
	mp[pair{h1, h2}] = 0
	cnt[pair{h1, h2}] = 1
	if k == 1 {
		ans++
	}

	for i := 1; i <= n-m; i++ {
		c := int64(s[i-1] - '0')
		h1 = (h1 - c*q1 + 10*mod) % mod
		h2 = (h2 - c*q2 + 10*mod) % mod
		c = int64(s[i+m-1] - '0')
		h1 = (h1*base1 + c) % mod
		h2 = (h2*base2 + c) % mod
		p := pair{h1, h2}
		if v, ok := mp[p]; !ok {
			mp[p] = i
			cnt[p] = 1
		} else if i >= v+m {
			mp[p] = i
			cnt[p]++
		} else {
			continue
		}
		if cnt[p] == k {
			ans++
		} else if cnt[p] == k+1 {
			ans--
		}
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
