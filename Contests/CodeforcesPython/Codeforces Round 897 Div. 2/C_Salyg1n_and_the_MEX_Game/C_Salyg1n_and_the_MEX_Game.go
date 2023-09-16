package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	// out := bufio.NewWriter(_w)
	// defer out.Flush()

	var T, n, a int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		x := n
		for i := 0; i < n; i++ {
			Fscan(in, &a)
			if x == n && i != a {
				x = i
			}
		}
		for x >= 0 {
			Println(x)
			// Fprintln(out, x)
			// out.Flush()
			Fscan(in, &x)
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
