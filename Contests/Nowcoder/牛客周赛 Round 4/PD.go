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

	var a, b int
	Fscan(in, &a, &b)

	getPrimes := func(x int) []int {
		primes := []int{}
		d := 2
		for ; d*d <= x; d++ {
			for x%d == 0 {
				primes = append(primes, d)
				x /= d
			}
			if x == 1 {
				break
			}
		}
		if x > 1 {
			primes = append(primes, x)
		}
		return primes
	}
	primes := getPrimes(a)
	primes = append(primes, getPrimes(b)...)
	sort.Ints(primes)

	ans := []int64{1}
	m := map[int64]bool{}
	for _, v := range primes {
		for i := len(ans) - 1; i >= 0; i-- {
			if _, ok := m[ans[i]*int64(v)]; !ok {
				ans = append(ans, ans[i]*int64(v))
				m[ans[i]*int64(v)] = true
			}
		}
	}

	// sort.Ints(ans)
	sort.SliceStable(ans, func(i, j int) bool {
		return ans[i] <= ans[j]
	})

	Fprintln(out, len(ans))
	for _, v := range ans {
		Fprint(out, v, " ")
	}

	Fprintln(out)
}

func main() { solve(os.Stdin, os.Stdout) }
