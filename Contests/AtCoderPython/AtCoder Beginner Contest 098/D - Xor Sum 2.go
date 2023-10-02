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
	a := make([]int, n)
	ans, x, l := 0, 0, 0
	for r := range a {
		Fscan(in, &a[r])
		for x&a[r] != 0 {
			x ^= a[l]
			l++
		}
		x |= a[r]
		ans += r - l + 1
	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
