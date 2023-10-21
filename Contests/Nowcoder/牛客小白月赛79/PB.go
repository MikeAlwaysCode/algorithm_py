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
	ans := 0
	odd := int(1e5)
	for i := 0; i < n; i++ {
		Fscan(in, &a)
		ans += a
		if a&1 > 0 && a < odd {
			odd = a
		}
	}
	if ans&1 > 0 {
		ans -= odd
	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
