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

	var n, k, a int
	Fscan(in, &n, &k)

	ans, s := 0, 0
	for i := 0; i < n; i++ {
		Fscan(in, &a)
		g := gcd(a, k)
		s += g
		ans += gcd(a, k/g)
	}
	ans += s * (n - 1)
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }

func gcd(a, b int) int {
	for a != 0 {
		a, b = b%a, a
	}
	return b
}
