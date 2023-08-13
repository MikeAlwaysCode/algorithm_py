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

	var n int
	Fscan(in, &n)
	s := make([]int64, n)
	t := make([]int64, n)

	for i := range s {
		Fscan(in, &s[i])
	}
	mx := int64(1e9 + 7)
	idx := -1
	for i := range t {
		Fscan(in, &t[i])
		if t[i] < mx {
			mx = t[i]
			idx = i
		}
	}
	for i := idx; i < idx+n; i++ {
		nxt := t[i%n] + s[i%n]
		if t[(i+1)%n] > nxt {
			t[(i+1)%n] = nxt
		}
	}
	for _, v := range t {
		Fprintln(out, v)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
