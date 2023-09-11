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

	var T, n, k, u, v int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &k)
		a := make([]int, n)
		for i := range a {
			Fscan(in, &a[i])
		}
		for i := 0; i < k; i++ {
			Fscan(in, &u, &v)
			a[u-1]++
			a[v-1]--
		}
		check := true
		for i := 1; i < n; i++ {
			if a[i] < a[i-1] {
				check = false
				break
			}
		}
		if check {
			Fprintln(out, "Yes")
		} else {
			Fprintln(out, "No")
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
