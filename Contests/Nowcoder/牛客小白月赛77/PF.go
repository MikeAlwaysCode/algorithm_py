package main

import (
	"bufio"
	. "fmt"
	"io"
	"math"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T int
	var a, b int64
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &a, &b)

		if a == b {
			Fprintln(out, 0)
			continue
		}
		if a > b {
			Fprintln(out, -1)
			continue
		}

		var mx int = 1e6 + 1
		dp := make([]int64, mx)
		sb := int64(math.Sqrt(float64(b)))
		if a <= sb {
			for i := range dp {
				dp[i] = 0x3f3f3f3f
			}
			dp[a] = 0
			for i := int(a) + 1; i <= int(sb); i++ {
				dp[i] = dp[i-1] + 1
				if i%2 == 0 {
					dp[i] = min(dp[i], dp[i/2]+1)
				}
				x := int(math.Sqrt(float64(i)))
				if x*x == i {
					dp[i] = min(dp[i], dp[x]+1)
				}
			}
		}

		mp := map[int64]int64{}
		var dfs func(x int64) int64
		dfs = func(x int64) int64 {
			if x <= sb {
				return dp[int(x)]
			}
			if x < a {
				return 0x3f3f3f3f
			}
			if v, ok := mp[x]; ok {
				return v
			}
			mp[x] = x - a
			if x/2 >= a {
				mp[x] = min(mp[x], dfs(x/2)+x%2+1)
			}
			sq := int64(math.Sqrt(float64(x)))
			if sq >= a {
				mp[x] = min(mp[x], dfs(sq)+x-sq*sq+1)
			}
			return mp[x]
		}

		Fprintln(out, dfs(b))
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int64) int64 {
	if a <= b {
		return a
	} else {
		return b
	}
}
