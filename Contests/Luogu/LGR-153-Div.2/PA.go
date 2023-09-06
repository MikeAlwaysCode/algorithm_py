package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

const mod int64 = 998244353

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var a, b, k int64
	Fscan(in, &a, &b, &k)
	t1, t2 := k/a, k/b
	if t1 <= t2 {
		if t1*a > t2*b {
			Fprintln(out, 2)
		} else {
			Fprintln(out, 1)
		}
	} else {
		Fprintln(out, pow(2, t1-t2))
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func pow(x, n int64) int64 {
	res := int64(1)
	for ; n > 0; n /= 2 {
		if n%2 > 0 {
			res = res * x % mod
		}
		x = x * x % mod
	}
	return res
}
