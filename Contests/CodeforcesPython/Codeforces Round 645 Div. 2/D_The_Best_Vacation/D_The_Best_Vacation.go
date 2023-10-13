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

	var n, x int
	Fscan(in, &n, &x)
	a := make([]int, n*2)
	tot := make([]int, n)
	pres := make([]int, n*2+1)
	for i := n - 1; i >= 0; i-- {
		Fscan(in, &a[i])
		a[i+n] = a[i]
		tot[i] = a[i] * (a[i] + 1) / 2
	}
	for i := 1; i <= n*2; i++ {
		pres[i] = pres[i-1] + a[i-1]
	}
	var ans, s int
	j := 1
	for i := 0; i < n; i++ {
		for pres[j]-pres[i] <= x {
			s += tot[(j-1)%n]
			j++
		}
		d := x - pres[j-1] + pres[i]
		ans = max(ans, s+d*(a[j-1]*2-d+1)/2)
		s -= tot[i]
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
