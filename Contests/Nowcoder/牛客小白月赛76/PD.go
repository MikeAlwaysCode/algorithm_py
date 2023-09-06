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

	const MOD = 998244353
	var T, n int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		var ans, a int64
		le := true
		for i := 0; i < n; i++ {
			Fscan(in, &a)
			if le || a <= 1 {
				ans += a
			} else {
				ans *= a
			}
			if ans > 1 {
				le = false
			}
			ans %= MOD
		}
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
