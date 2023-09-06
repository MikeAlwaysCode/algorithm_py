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
	type pair struct{ x, y int }

	var x, y int
	m := map[pair]int{}
	Fscan(in, &x, &y)
	m[pair{x, y}] = 1
	Fscan(in, &x, &y)
	m[pair{x, y}] = 1
	Fscan(in, &x, &y)
	DIR := []pair{{-2, -1}, {-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}}
	for _, p := range DIR {
		nx, ny := x+p.x, y+p.y
		if nx < 1 || nx > 10 || ny < 1 || ny > 10 {
			continue
		}
		res := 0
		for _, p2 := range DIR {
			if _, ok := m[pair{nx + p2.x, ny + p2.y}]; ok {
				res++
			}
		}
		if res == 2 {
			Fprintln(out, "Yes")
			return
		}
	}
	Fprintln(out, "No")

}

func main() { solve(os.Stdin, os.Stdout) }
