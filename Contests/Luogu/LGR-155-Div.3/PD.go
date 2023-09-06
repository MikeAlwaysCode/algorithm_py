package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	// in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	buf := make([]byte, 4096)
	_i := len(buf)
	rc := func() byte {
		if _i == len(buf) {
			_r.Read(buf)
			_i = 0
		}
		b := buf[_i]
		_i++
		return b
	}
	r := func() (x int) {
		b := rc()
		for ; '0' > b; b = rc() {
		}
		for ; '0' <= b; b = rc() {
			x = x*10 + int(b&15)
		}
		return
	}

	// var n, m, c1, c2 int
	// Fscan(in, &n, &m, &c1, &c2)
	n, m, c1, c2 := r(), r(), r(), r()
	// s := make([]int, n)
	// t := make([]int, m)
	var s, t int
	mp := map[int][]int{}
	// for i := range s {
	// 	Fscan(in, &s[i])
	// 	mp[s[i]] = append(mp[s[i]], i)
	// }
	for i := 0; i < n; i++ {
		// Fscan(in, &s)
		s = r()
		mp[s] = append(mp[s], i)
	}
	k, cnt, last := 0, 0, n
	// for i := range t {
	// 	Fscan(in, &t[i])
	// }
	for ; m > 0; m-- {
		// Fscan(in, &t)
		t = r()
		if p, ok := mp[t]; ok {
			cnt++
			if last >= p[len(p)-1] {
				k++
				last = p[0]
			} else {
				j := sort.SearchInts(p, last+1)
				last = p[j]
			}
		}
	}

	Fprintln(out, c1*cnt, c2*k)
}

func main() { solve(os.Stdin, os.Stdout) }
