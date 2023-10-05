package main

import (
	"bufio"
	. "fmt"
	"io"
	"math/bits"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, k int
	Fscan(in, &n, &k)
	a := make([]int, n)
	s := 0
	for i := range a {
		Fscan(in, &a[i])
		s += a[i]
	}

	ans := 0

	for bit := 1 << (bits.Len(uint(s)) - 1); bit > 0; bit >>= 1 {
		cnt := 0
		for i := range a {
			s = 0
			for _, v := range a[i:] {
				s += v
				if s&ans == ans && s&bit > 0 {
					cnt++
				}
			}
		}
		if cnt >= k {
			ans |= bit
		}
	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
