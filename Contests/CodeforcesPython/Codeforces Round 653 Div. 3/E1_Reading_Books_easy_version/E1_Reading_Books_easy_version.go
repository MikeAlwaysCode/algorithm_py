package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func CF1409E(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, k int
	var t, al, bl int
	Fscan(in, &n, &k)
	a := []int{}
	b := []int{}
	c := []int{}
	for ; n > 0; n-- {
		Fscan(in, &t, &al, &bl)
		if al > 0 && bl > 0 {
			c = append(c, t)
		} else if al > 0 {
			a = append(a, t)
		} else if bl > 0 {
			b = append(b, t)
		}

	}

	m1 := len(c)
	m2 := min(len(a), len(b))

	if m1+m2 < k {
		Fprintln(out, -1)
	} else {
		sort.Ints(a)
		sort.Ints(b)
		sort.Ints(c)

		ans := 0

		for i, j := 0, 0; i+j < k; {
			if i < m1 && j < m2 && c[i] <= a[j]+b[j] {
				ans += c[i]
				i++
			} else if i < m1 && j < m2 && c[i] > a[j]+b[j] {
				ans += a[j] + b[j]
				j++
			} else if i < m1 {
				ans += c[i]
				i++
			} else if j < m2 {
				ans += a[j] + b[j]
				j++
			}
		}
		Fprintln(out, ans)
	}

}

func main() { CF1409E(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if b < a {
		return b
	}
	return a
}
