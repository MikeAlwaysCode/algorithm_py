package main

import (
	"bufio"
	. "fmt"
	"io"
	"math"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var x, y int
	Fscan(in, &x, &y)
	ans := y - x + 1
	mx := int(math.Sqrt(float64(y*y*2 - x*x)))
	for a := x; a <= y; a++ {
		for b := a + 1; b <= mx; b++ {
			if a^a+b^b <= 2*y*y {
				ans += 2
			} else {
				break
			}
		}
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
