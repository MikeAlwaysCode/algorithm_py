package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func CF1179B(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, m int
	Fscan(in, &n, &m)
	x1, y1, x2, y2, step := 1, 1, n, m, 1
	for x1 <= x2 {
		Fprintln(out, x1, y1)
		if x1 == x2 && y1 == y2 {
			break
		}
		Fprintln(out, x2, y2)
		if x1 == x2 && y1+step == y2 {
			break
		}

		if y1+step <= 0 || y1+step > m {
			x1 += 1
			x2 -= 1
			step = -step
		} else {
			y1 += step
			y2 -= step
		}
	}

}

func main() { CF1179B(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
