package main

import (
	"bufio"
	// "container/heap"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	type pair struct {
		p int64
		i int
	}

	const mod int64 = 1e9 + 7
	var n, k int
	Fscan(in, &n, &k)
	a := make([]int64, n)
	for i := range a {
		Fscan(in, &a[i])
	}

	var ans int64
	b := make([]int64, k)
	pres := []pair{}
	var p, op, x int64
	for i := range b {
		Fscan(in, &op, &x)
		if op == 1 {
			b[i] = x
			p -= x
		} else {
			b[i] = -x
			p += x
		}
		if len(pres) == 0 || p > pres[len(pres)-1].p {
			pres = append(pres, pair{p, i})
		}
	}

	mx := make([]int64, k+1)
	p = 0
	for i := k - 1; i >= 0; i-- {
		p += b[i]
		mx[i] = max(p, mx[i+1])
	}

	for _, v := range a {
		j := sort.Search(len(pres), func(i int) bool {
			return pres[i].p >= v
		})
		if j >= len(pres) {
			ans += v + p
		} else {
			ans += mx[pres[j].i]
		}
		ans %= mod
	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int64) int64 {
	if a >= b {
		return a
	} else {
		return b
	}
}
