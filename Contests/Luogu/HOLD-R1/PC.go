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
	type pair struct{ x, y int }
	dir4 := [...]pair{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	var n int
	Fscan(in, &n)
	g := make([][]int, n)
	for i := range g {
		g[i] = make([]int, n)
		for j := range g[i] {
			Fscan(in, &g[i][j])
		}
	}
	cnt := make([]int, n*n)
	time := make([][]int, n)
	for i := range time {
		time[i] = make([]int, n)
	}

	t, tot := 0, 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			tot += g[i][j]
			if g[i][j] == 1 && time[i][j] == 0 {
				t++
				time[i][j] = t
				for q := []pair{{i, j}}; len(q) > 0; {
					p := q[0]
					q = q[1:]
					cnt[t]++
					for _, d := range dir4 {
						x, y := p.x+d.x, p.y+d.y
						if x < 0 || x >= n || y < 0 || y >= n || g[x][y] == 0 || time[x][y] > 0 {
							continue
						}
						time[x][y] = t
						q = append(q, pair{x, y})
					}
				}
			}
		}
	}

	if tot == n*n {
		Fprintln(out, tot, tot)
	} else {
		mx, c := 0, 0
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if g[i][j] == 1 {
					continue
				}
				set := make(map[int]bool)

				for _, d := range dir4 {
					x, y := i+d.x, j+d.y
					if x < 0 || x >= n || y < 0 || y >= n || g[x][y] == 0 {
						continue
					}
					set[time[x][y]] = true
				}
				cur := 1
				for t := range set {
					cur += cnt[t]
				}
				if cur > mx {
					mx, c = cur, 1
				} else if cur == mx {
					c++
				}
			}
		}
		Fprintln(out, mx, c)
	}

}

func main() { solve(os.Stdin, os.Stdout) }
