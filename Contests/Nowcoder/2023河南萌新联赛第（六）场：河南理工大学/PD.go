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

	var n, m int
	Fscan(in, &n, &m)
	ans := 0
	for n > 0 && m > 1 {
		n -= m
		m = (m + 1) / 2
		ans += 1
	}
	if n > 0 {
		ans += n
	}
	Fprintln(out, ans-1)
}

func main() { solve(os.Stdin, os.Stdout) }
