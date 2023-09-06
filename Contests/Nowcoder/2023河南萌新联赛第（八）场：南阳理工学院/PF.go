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

	var n, q, a, l, r, x int
	Fscan(in, &n, &q)
	cnt := make([][60]int, n+1)
	for i := 0; i < n; i++ {
		Fscan(in, &a)
		for bit := 0; bit < 60; bit++ {
			cnt[i+1][bit] = cnt[i][bit]
			if (a>>bit)&1 > 0 {
				cnt[i+1][bit]++
			}
		}
	}
	for ; q > 0; q-- {
		Fscan(in, &l, &r, &x)
		for bit := 0; bit < 60; bit++ {
			if cnt[r][bit]-cnt[l-1][bit] > 0 {
				x |= 1 << bit
			}
		}
		Fprintln(out, x)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
