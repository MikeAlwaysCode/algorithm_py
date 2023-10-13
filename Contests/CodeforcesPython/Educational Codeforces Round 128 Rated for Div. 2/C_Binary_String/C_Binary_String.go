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

	var T int
	var s string
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &s)
		n := len(s)
		pos := []int{}
		for i, c := range s {
			if c == '1' {
				pos = append(pos, i)
			}
		}
		if len(pos) == 0 || len(pos) == n {
			Fprintln(out, 0)
			continue
		}
		m := len(pos)
		ans, l := m, 0
		for r := 0; r < m; r++ {
			for ; pos[r]-pos[l] > m-1; l++ {
			}
			ans = min(ans, max(pos[r]-pos[l], m-1)-r+l)
		}
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
func max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
