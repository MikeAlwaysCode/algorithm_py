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
	var a int64
	Fscan(in, &n)
	m := map[int64]int{}
	zero := []int{}
	for i := 1; i <= n; i++ {
		Fscan(in, &a)
		if a == 0 {
			zero = append(zero, i)
		} else {
			m[a] = i
		}
	}
	if len(zero) > 1 {
		Fprintln(out, zero[0], zero[1])
		return
	}
	for x, v1 := range m {
		y := x & 1
		for i := 0; x > 0; i++ {
			bit := (x & y >> i & 1) ^ (x >> (i + 1) & 1)
			y |= bit << (i + 1)
			x ^= x & (1 << i)
		}
		if v2, ok := m[y]; ok {
			Fprintln(out, v1, v2)
			return
		}
	}

	Fprintln(out, -1)
}

func main() { solve(os.Stdin, os.Stdout) }
