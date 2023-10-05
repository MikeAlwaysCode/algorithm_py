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

	var n, ans, cnt, x int
	mn := 1 << 30
	Fscan(in, &n)
	for i := 0; i < n; i++ {
		Fscan(in, &x)
		if x < 0 {
			x = -x
			cnt++
		}
		ans += x
		if x < mn {
			mn = x
		}
	}

	if cnt&1 > 0 {
		ans -= 2 * mn
	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
