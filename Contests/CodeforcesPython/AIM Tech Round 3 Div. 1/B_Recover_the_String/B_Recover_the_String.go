package main

import (
	"bufio"
	. "fmt"
	"io"
	"math"
	"os"
	"strings"
	// "sort"
)

func CF708B(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var a00, a01, a10, a11 int
	Fscan(in, &a00, &a01, &a10, &a11)
	f := func(c int) int {
		x := (1 + int(math.Sqrt(float64(1+8*int64(c))))) / 2
		if x*(x-1)/2 == c {
			return x
		}
		return -1
	}
	n, m := f(a00), f(a11)

	if n < 0 || m < 0 {
		Fprintln(out, "Impossible")
		return
	}

	if a01 == 0 && a10 == 0 {
		if a00 == 0 && a11 == 0 {
			Fprintln(out, "0")
			return
		} else if a00 > 0 && a11 > 0 {
			Fprintln(out, "Impossible")
			return
		} else if a00 > 0 {
			Fprintln(out, strings.Repeat("0", n))
			return
		} else if a11 > 0 {
			Fprintln(out, strings.Repeat("1", m))
			return
		}
	}

	if a01+a10 != n*m {
		if a00 == 0 && a01+a10 == m {
			n = 1
		} else if a11 == 0 && a10+a10 == n {
			m = 1
		} else {
			Fprintln(out, "Impossible")
			return
		}
	}

	r1 := a01 / n
	l0 := a01 % n
	r0 := n - l0
	m1 := 0
	if l0 > 0 {
		m1 = 1
		a10 -= n - l0
	}
	l1 := m - m1 - r1
	ans := strings.Repeat("1", l1) + strings.Repeat("0", l0) + strings.Repeat("1", m1) + strings.Repeat("0", r0) + strings.Repeat("1", r1)
	Fprintln(out, ans)
}

func main() { CF708B(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
