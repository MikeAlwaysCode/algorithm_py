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

	var n, q, op, x, y int
	Fscan(in, &n, &q)
	fa := make([]int, n+1)
	box := make([]int, n+1)
	ball := make([]int, n+1)
	for i := range fa {
		fa[i] = i
		box[i] = i
		ball[i] = i
	}

	var find func(x int) int
	find = func(x int) int {
		if fa[x] != x {
			fa[x] = find(fa[x])
		}
		return fa[x]
	}

	for i := 0; i < q; i++ {
		Fscan(in, &op)
		if op == 1 {
			Fscan(in, &x, &y)
			if box[y] == -1 {
				continue
			}
			if box[x] == -1 {
				box[x] = box[y]
				ball[box[y]] = x
			} else {
				fa[box[y]] = box[x]
			}
			box[y] = -1
		} else if op == 2 {
			Fscan(in, &x)
			n++
			fa = append(fa, n)
			ball = append(ball, n)
			if box[x] == -1 {
				ball[n] = x
				box[x] = n
			} else {
				fa[n] = box[x]
			}
		} else {
			Fscan(in, &x)
			Fprintln(out, ball[find(x)])
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
