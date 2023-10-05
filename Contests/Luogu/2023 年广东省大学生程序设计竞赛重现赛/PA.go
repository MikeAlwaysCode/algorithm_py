package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, y1, y2, x, n int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &y1, &n)
		a := []int{}
		if n > 0 {
			for i := 0; i < n; i++ {
				Fscan(in, &x)
				a = append(a, x)
			}
		}
		Fscan(in, &y2)
		j := 0
		if n > 0 {
			j = sort.SearchInts(a, y2)
		}

		Fprintln(out, y2-y1-j+1)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
