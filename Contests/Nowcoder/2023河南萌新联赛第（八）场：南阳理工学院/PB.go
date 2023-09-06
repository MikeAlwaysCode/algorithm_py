package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

const mod int = 1e9 + 7

func solve(_r io.Reader, _w io.Writer) {
	// in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	buf := make([]byte, 4096)
	_i := len(buf)
	rc := func() byte {
		if _i == len(buf) {
			_r.Read(buf)
			_i = 0
		}
		b := buf[_i]
		_i++
		return b
	}
	r := func() (x int) {
		b := rc()
		for ; '0' > b; b = rc() {
		}
		for ; '0' <= b; b = rc() {
			x = x*10 + int(b&15)
		}
		return
	}

	var mx int = 6 * 1e5
	cnt := make([]int, mx)
	p := make([]int, mx)
	for i := range p {
		p[i] = 1
	}
	n := r()
	rev := pow(2, mod-2)
	for i := 0; i < n; i++ {
		l1, r1, l2, r2 := r(), r(), r(), r()
		if l1 > l2 {
			l1, r1, l2, r2 = l2, r2, l1, r1
		}
		cnt[l1]++
		if l2 > r1 {
			cnt[r1+1]--
			cnt[l2]++
			cnt[r2+1]--
		} else {
			cnt[max(r1, r2)+1]--
			p[l2] = p[l2] * 2 % mod
			p[min(r1, r2)+1] = p[min(r1, r2)+1] * rev % mod
		}
	}
	ans := 0
	c, k := 0, 1
	for i := 1; i < mx; i++ {
		c += cnt[i]
		k = k * p[i] % mod
		if c == n {
			ans = (ans + k) % mod
		}
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
func pow(x, n int) int {
	res := 1
	for ; n > 0; n /= 2 {
		if n%2 > 0 {
			res = res * x % mod
		}
		x = x * x % mod
	}
	return res
}
