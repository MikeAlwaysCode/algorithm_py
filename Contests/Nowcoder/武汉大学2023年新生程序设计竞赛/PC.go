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

	mx := int(1e10)

	a := make([][]int, 3)
	ans := 0
	x1, y1, x2, y2 := -mx, -mx, mx, mx
	for i := range a {
		a[i] = make([]int, 4)
		Fscan(in, &a[i][0], &a[i][1], &a[i][2], &a[i][3])
		x1 = max(x1, a[i][0])
		y1 = max(y1, a[i][1])
		x2 = min(x2, a[i][2])
		y2 = min(y2, a[i][3])
		ans += (a[i][2] - a[i][0]) * (a[i][3] - a[i][1])
	}
	if x2 > x1 && y2 > y1 {
		ans += (x2 - x1) * (y2 - y1)
	}
	for i := 0; i < 2; i++ {
		for j := i + 1; j < 3; j++ {
			x1 = max(a[i][0], a[j][0])
			y1 = max(a[i][1], a[j][1])
			x2 = min(a[i][2], a[j][2])
			y2 = min(a[i][3], a[j][3])
			if x2 > x1 && y2 > y1 {
				ans -= (x2 - x1) * (y2 - y1)
			}
		}
	}
	Fprintln(out, ans)
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
