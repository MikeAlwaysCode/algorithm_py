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
	type pair struct {
		s string
		t int
	}

	var n, t int
	var p, s string
	Fscan(in, &n)
	game := []string{}
	q := []pair{}
	mp := map[string]int{}
	for i := 0; i < n; i++ {
		Fscan(in, &s)
		if s == "start" {
			for len(game) > 0 {
				t++
				mp[game[0]] = t
				q = append(q, pair{game[0], t})
				game = game[1:]
			}
			for len(game) < 2 && len(q) > 0 {
				if mp[q[0].s] == q[0].t {
					mp[q[0].s] = 0
					game = append(game, q[0].s)
				}
				q = q[1:]
			}
			if len(game) == 0 {
				Fprintln(out, "Error")
			} else {
				for j := 0; j < len(game); j++ {
					Fprint(out, game[j], " ")
				}
				Fprintln(out)
			}
		} else if s == "arrive" {
			Fscan(in, &p)
			if v, ok := mp[p]; ok && v != -1 {
				Fprintln(out, "Error")
			} else {
				t++
				mp[p] = t
				q = append(q, pair{p, t})
				Fprintln(out, "OK")
			}
		} else if s == "leave" {
			Fscan(in, &p)
			if v, ok := mp[p]; !ok || v == -1 || v == 0 {
				Fprintln(out, "Error")
			} else {
				mp[p] = -1
				Fprintln(out, "OK")
			}
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
