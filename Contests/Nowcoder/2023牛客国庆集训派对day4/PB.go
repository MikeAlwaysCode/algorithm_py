package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

var mod int64 = 1e9 + 7

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var mxn int = 1e6
	factor := make([]int, mxn+1)
	for i := range factor {
		factor[i] = 1
	}
	for i := 2; i <= mxn; i++ {
		if factor[i] != 1 {
			continue
		}
		for j := i; j <= mxn; j += i {
			factor[j] = i
		}
	}
	factor_count := func(x int) int {
		res := 0
		for x != 1 {
			res++
			x /= factor[x]
		}
		return res
	}

	var T, n, c int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &c)
		Fprintln(out, pow(int64(c), int64(factor_count(n))))
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func pow(x, n int64) int64 {
	var res int64 = 1
	for ; n > 0; n /= 2 {
		if n%2 > 0 {
			res = res * x % mod
		}
		x = x * x % mod
	}
	return res
}
