package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func CF1054D(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, k, a int
	Fscan(in, &n, &k)
	ans, mask, xor := n*(n+1)/2, 1<<k-1, 0
	cnt := map[int]int{}
	cnt[0] = 1
	for i := 0; i < n; i++ {
		Fscan(in, &a)
		xor ^= a
		if cnt[xor] > cnt[xor^mask] {
			xor = xor ^ mask
		}
		ans -= cnt[xor]
		cnt[xor]++
	}

	Fprintln(out, ans)
}

func main() { CF1054D(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
