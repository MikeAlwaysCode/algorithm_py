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

	var T int
	var n, m int64
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &m)
		n++
		d := n / (m + 1)
		k := n % (m + 1)
		var ans int64
		if k > 0 {
			ans = (d + 1) * (n*2 - (k+1)*(d+1)) * k / 2
			n -= k * (d + 1)
		}
		ans += (n - d) * n / 2
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
