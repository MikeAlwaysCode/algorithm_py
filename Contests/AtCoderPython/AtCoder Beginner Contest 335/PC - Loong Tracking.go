package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, q, t, p int
	var d string
	Fscan(in, &n, &q)
	a := make([][]int, n)
	for i := range a {
		a[i] = make([]int, 2)
		a[i][0], a[i][1] = n-i, 0
	}
	for i := 0; i < q; i++ {
		Fscan(in, &t)
		if t == 1 {
			Fscan(in, &d)
			x, y := a[n-1][0], a[n-1][1]
			a = a[1:]
			if d == "U" {
				y++
			} else if d == "D" {
				y--
			} else if d == "R" {
				x++
			} else {
				x--
			}
			a = append(a, []int{x, y})
		} else {
			Fscan(in, &p)
			Fprintln(out, a[n-p][0], a[n-p][1])
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
