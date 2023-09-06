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

	var n int64
	Fscan(in, &n)
	ans := (n - 1) / 3
	if n%3 > 0 {
		ans *= 2
	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
