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

	var n, a int
	Fscan(in, &n)
	pos := make([]int, n)
	for i := 0; i < n; i++ {
		Fscan(in, &a)
		pos[a-1] = i
	}
	var x, y int
	Fscan(in, &x, &y)
	if abs(pos[x-1]-pos[y-1]) == 1 {
		Fprintln(out, "Yes")
	} else {
		Fprintln(out, "No")
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func abs(x int) int {
	if x < 0 {
		return -x
	} else {
		return x
	}
}
