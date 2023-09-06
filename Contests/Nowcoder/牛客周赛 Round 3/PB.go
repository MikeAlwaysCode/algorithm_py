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

	var s string
	Fscan(in, &s)
	ans := 26 * len(s)
	for t := 'a'; t <= 'z'; t++ {
		res := 0
		for _, c := range s {
			d := abs(int(c - t))
			res += min(d, 26-d)
		}
		ans = min(ans, res)
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func abs(a int) int {
	if a < 0 {
		return -a
	} else {
		return a
	}
}
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
