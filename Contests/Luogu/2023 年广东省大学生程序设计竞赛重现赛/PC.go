package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	type pair struct{ a, b int }

	var T, n int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		store := make([]pair, n)
		for i := range store {
			Fscan(in, &store[i].a, &store[i].b)
		}
		sort.Slice(store, func(i, j int) bool {
			if store[i].a == store[j].a {
				return store[i].b <= store[j].b
			} else {
				return store[i].a < store[j].a
			}
		})

		if store[0].a == store[n-1].a {
			Fprintln(out, 0)
			continue
		}

		ans := 0
		i, j := 0, n-1
		for i < j {
			m := min(store[i].b, store[j].b)
			ans += (store[j].a - store[i].a) * m
			store[i].b -= m
			store[j].b -= m
			if store[i].b == 0 {
				i += 1
			}
			if store[j].b == 0 {
				j -= 1
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
