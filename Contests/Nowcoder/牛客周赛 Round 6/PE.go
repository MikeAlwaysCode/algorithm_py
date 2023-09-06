package main

import (
	"bufio"
	// "container/heap"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	type pair struct {
		p int64
		d int
	}

	var p, q int64
	Fscan(in, &p, &q)

	p %= q
	if p == 0 {
		Fprintln(out, -1)
		return
	}
	p *= 10
	m := map[pair]int{}
	for i := 1; p != 0; i++ {
		v := p % q
		d := int(p / q)
		pp := pair{p, d}
		if pd, ok := m[pp]; ok {
			Fprintln(out, pd-1, len(m)-pd+1)
			return
		}
		m[pp] = i
		p = v * 10
	}
	Fprintln(out, -1)
}

func main() { solve(os.Stdin, os.Stdout) }
