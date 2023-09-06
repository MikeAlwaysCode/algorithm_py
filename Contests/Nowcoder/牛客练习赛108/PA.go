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

	var T, a1, a2, a3, a4 int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &a1, &a2, &a3, &a4)
		ans := (a1 | a2 | a3 | a4) * 4
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
