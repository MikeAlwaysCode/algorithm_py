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

	var T, n, k, ans, a int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &k)
		ans = 0
		cnt := make([]int, k)
		for i := 0; i < n; i++ {
			Fscan(in, &a)
			ans += a / k
			if a%k > 0 {
				cnt[a%k]++
			}
		}
		i, j := 1, k-1
		for i <= j {
			if cnt[i] == 0 {
				i++
			} else if cnt[j] == 0 {
				j--
			} else if i+j < k {
				i++
			} else if i == j {
				ans += cnt[i] / 2
				break
			} else {
				m := min(cnt[i], cnt[j])
				ans += m
				cnt[i] -= m
				cnt[j] -= m
			}
		}
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
