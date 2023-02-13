package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

// github.com/EndlessCheng/codeforces-go
type seg []struct {
	l, r, min int
	a         []int
}

func (t seg) build(a []int, o, l, r int) {
	t[o].l, t[o].r, t[o].min = l, r, 2e9
	t[o].a = append([]int(nil), a[l-1:r]...)
	sort.Ints(t[o].a)
	if l == r {
		return
	}
	m := (l + r) >> 1
	t.build(a, o<<1, l, m)
	t.build(a, o<<1|1, m+1, r)
}

var allMin int

func (t seg) update(o, i, val int) {
	if t[o].l == t[o].r {
		t[o].min = min(t[o].min, abs(val-t[o].a[0]))
		allMin = min(allMin, t[o].min)
		return
	}
	if t[o].r <= i {
		a := t[o].a
		p := sort.SearchInts(a, val)
		if (p == 0 || val-a[p-1] >= allMin) && (p == len(a) || a[p]-val >= allMin) {
			allMin = min(allMin, t[o].min)
			return
		}
	}
	m := (t[o].l + t[o].r) >> 1
	if i > m {
		t.update(o<<1|1, i, val)
	}
	t.update(o<<1, i, val)
	t[o].min = min(t[o<<1].min, t[o<<1|1].min)
}

func (t seg) query(o, l int) int {
	if l <= t[o].l {
		return t[o].min
	}
	if (t[o].l+t[o].r)>>1 < l {
		return t.query(o<<1|1, l)
	}
	return min(t.query(o<<1, l), t[o<<1|1].min)
}

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, q int
	Fscan(in, &n, &q)
	a := make([]int, n)
	for i := range a {
		Fscan(in, &a[i])
	}
	// Fscan(in, &q)
	qs := make([]struct{ l, r, i int }, q)
	for i := range qs {
		Fscan(in, &qs[i].l, &qs[i].r)
		qs[i].i = i
	}
	sort.Slice(qs, func(i, j int) bool { return qs[i].r < qs[j].r })

	ans := make([]int, q)
	t := make(seg, 4*n)
	t.build(a, 1, 1, n)
	for r, qi := 2, 0; r <= n; r++ {
		allMin = 2e9
		t.update(1, r-1, a[r-1])
		for ; qi < q && qs[qi].r == r; qi++ {
			ans[qs[qi].i] = t.query(1, qs[qi].l)
		}
	}
	for _, v := range ans {
		Fprintln(out, v)
	}
}

func main() { solve(os.Stdin, os.Stdout) }

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
