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
	type pair struct{ x, y int }

	var n, m int
	Fscan(in, &n, &m)
	ans := n - 1
	point := make([]pair, n)
	for i := range point {
		Fscan(in, &point[i].x, &point[i].y)
	}
	dis := make([][]int, m+1)
	for i := range dis {
		dis[i] = make([]int, m+1)
		for j := range dis[i] {
			dis[i][j] = 1e9
		}
	}

	dir := []pair{
		{-2, -1},
		{-2, 1},
		{-1, -2},
		{-1, 2},
		{1, -2},
		{1, 2},
		{2, -1},
		{2, 1},
	}

	bfs := func(p pair) {
		dis[p.x][p.y] = 0
		q := []pair{p}
		for len(q) > 0 {
			p = q[0]
			q = q[1:]
			x, y := p.x, p.y
			for _, d := range dir {
				nx, ny := x+d.x, y+d.y
				if nx <= 0 || nx > m || ny <= 0 || ny > m {
					continue
				}
				if dis[nx][ny] > dis[x][y]+1 {
					dis[nx][ny] = dis[x][y] + 1
					q = append(q, pair{nx, ny})
				}
			}
		}
	}

	bfs(point[0])

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
