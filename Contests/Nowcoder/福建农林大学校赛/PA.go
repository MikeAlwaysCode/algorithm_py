package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	a := make([]int, 4)
	Fscan(in, &a[0], &a[1], &a[2], &a[3])
	carry := 0
	for i, d := range a {
		d += carry
		if i < 3 {
			carry = int((d - 1) / 2)
			a[i] = (d-1)%2 + 1
		} else {
			a[i] = d
		}
	}
	Fprintln(out, a[0], a[1], a[2], a[3])
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
