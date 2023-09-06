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

	var n int
	Fscan(in, &n)
	pos := make([]int64, n+1)
	var s int64
	for i := 0; i < n; i++ {
		Fscan(in, &pos[i+1])
		s += pos[i+1]
		pos[i+1] += pos[i]
	}
	var x, y int
	Fscan(in, &x, &y)
	if x > y {
		x, y = y, x
	}
	x--
	y--
	ans := min(pos[y]-pos[x], s-pos[y]+pos[x])
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int64) int64 {
	if a <= b {
		return a
	} else {
		return b
	}
}
