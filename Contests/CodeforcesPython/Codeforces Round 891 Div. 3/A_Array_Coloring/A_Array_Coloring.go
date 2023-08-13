package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, n, a int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		cnt := 0
		for i := 0; i < n; i++ {
			Fscan(in, &a)
			cnt += a & 1
		}
		if cnt&1 > 0 {
			Fprintln(out, "NO")
		} else {
			Fprintln(out, "YES")
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
