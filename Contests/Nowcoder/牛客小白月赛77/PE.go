package main

import (
	"bufio"
	"container/heap"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, ans, a int
	var k, p int64
	Fscan(in, &n, &k)

	h := &hp{}
	op := false
	for i := 0; i < n; i++ {
		Fscan(in, &a)
		if a >= 0 {
			ans++
			p += int64(a)
		} else {
			if (op || p+int64(a) >= 0) && k+int64(a) >= 0 {
				ans++
				p += int64(a)
				k += int64(a)
				heap.Push(h, a)
			} else if h.Len() > 0 {
				v := heap.Pop(h).(int)
				op = true
				if v < a {
					k += int64(a - v)
					v = a
				}
				heap.Push(h, v)
			} else if !op {
				op = true
			}
		}
	}

	// op := false
	// neg := []int{}
	// for i := 0; i < n; i++ {
	// 	Fscan(in, &a)
	// 	if a >= 0 {
	// 		ans++
	// 	} else {
	// 		neg = append(neg, -a)
	// 	}
	// 	p += int64(a)
	// 	if !op && p < 0 {
	// 		sort.Ints(neg)
	// 		neg = neg[:len(neg)-1]
	// 		op = true
	// 	}
	// }
	// sort.Ints(neg)
	// for _, v := range neg {
	// 	if k >= int64(v) {
	// 		ans++
	// 		k -= int64(v)
	// 	} else {
	// 		break
	// 	}
	// }

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }

type hp struct{ sort.IntSlice }

// func (h hp) Less(i, j int) bool  { return h.IntSlice[i] > h.IntSlice[j] } //加上是最大堆
func (h *hp) Push(v interface{}) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() interface{} {
	a := h.IntSlice
	v := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return v
}
