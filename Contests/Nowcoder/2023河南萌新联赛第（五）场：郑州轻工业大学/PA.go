package main

import (
	"bufio"
	// "container/heap"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, n, m int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &m)
		if n == 0 {
			Fprintln(out, "Alice")
			continue
		}
		ans := 0
		if m > 1 {
			ans = 1
		}

		if n < 3 {
			ans ^= n
		} else {
			ans ^= (n - 3) % 3
		}

		if ans == 0 {
			Fprintln(out, "Bob")
		} else {
			Fprintln(out, "Alice")
		}

	}
}

func main() { solve(os.Stdin, os.Stdout) }
