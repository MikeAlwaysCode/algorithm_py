package main

import (
	"bufio"
	"container/heap"
	. "fmt"
	"io"
	"os"
	"sort"
)

func CF1802D(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	type pair struct{ a, b int }

	var T, n, a, b int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		store := make([]pair, n)
		for i := range store {
			Fscan(in, &a, &b)
			store[i] = pair{a, b}
		}

		sort.Slice(store, func(i, j int) bool {
			if store[i].a == store[j].a {
				return store[i].b >= store[j].b
			} else {
				return store[i].a < store[j].a
			}
		})

		mx := make([]int, n)
		for i := n - 2; i >= 0; i-- {
			mx[i] = max(mx[i+1], store[i+1].b)
		}

		h := &hp{}
		ans, mnb := 1<<31, -1
		for i := 0; i < n; i++ {
			a, b = store[i].a, store[i].b
			mxb := -1
			for h.Len() > 0 && h.IntSlice[0] < a {
				mnb = heap.Pop(h).(int)
			}
			if h.Len() > 0 {
				mxb = h.IntSlice[0]
			}

			if i < n-1 {
				ans = min(ans, abs(mx[i]-a))
			}
			if mxb >= mx[i] {
				ans = min(ans, abs(mxb-a))
			}
			if mnb >= mx[i] {
				ans = min(ans, abs(mnb-a))
			}

			heap.Push(h, b)
		}

		Fprintln(out, ans)
	}
}

func main() { CF1802D(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
func min(a, b int) int {
	if b < a {
		return b
	}
	return a
}
func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

type hp struct{ sort.IntSlice }

func (h *hp) Push(v interface{}) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() interface{} {
	a := h.IntSlice
	v := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return v
}
