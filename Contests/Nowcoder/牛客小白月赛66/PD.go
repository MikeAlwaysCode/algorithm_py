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

	var n, m int
	Fscan(in, &n, &m)
	a := make([]int, m+2)
	for i := 1; i <= m; i++ {
		Fscan(in, &a[i])
	}
	a[m+1] = n
	ans := 0
	for l := 0; l <= m; l++ {
		for j := 0; j <= 500; j++ {
			r := l + j + 1
			if r > m+1 {
				break
			}
			ans = max(ans, a[r]-a[l]-j*j)
		}
	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
