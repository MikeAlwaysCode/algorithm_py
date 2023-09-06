package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

const mod int64 = 998244353

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	dp := map[int64]int64{}
	var f func(x int64) int64
	f = func(x int64) int64 {
		if x == 1 {
			return 1
		} else if x == 2 {
			return 499122178
		} else {
			if res, ok := dp[x]; ok {
				return res
			} else {
				dp[x] = (1 + (f((x+1)/2)*((x+1)/2)+f(x/2)*(x/2))%mod*pow(x, mod-2)) % mod
				return dp[x]
			}
		}
	}

	var T, n int64
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		ans := f(n)
		Fprintln(out, ans)
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
