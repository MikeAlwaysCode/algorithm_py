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

	var n int
	Fscan(in, &n)
	mn := n
	ansx, ansy := 1, 1
	x, fact := 3, 2
	for ; fact*x-1 <= n; x++ {
		fact *= x
		cy := n / (fact - 1)
		for y := cy - 1; y <= cy+1; y++ {
			if y < 1 || y == 2 {
				continue
			}
			res := n - (fact-1)*y
			if res < 0 {
				res = -res
			}
			if res < mn {
				mn, ansx, ansy = res, x, y
			}
		}
	}
	fact *= x
	if fact-1-n < mn {
		ansx, ansy = x, 1
	}

	Fprintln(out, ansx, ansy)
}

func main() { solve(os.Stdin, os.Stdout) }
