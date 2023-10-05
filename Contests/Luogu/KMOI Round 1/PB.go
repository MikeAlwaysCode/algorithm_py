package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

const mod = 911451407

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n int
	Fscan(in, &n)
	ans := n * pow(2, n-1) % mod
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func pow(x, n int) int {
	res := 1
	for ; n > 0; n /= 2 {
		if n%2 > 0 {
			res = res * x % mod
		}
		x = x * x % mod
	}
	return res
}
