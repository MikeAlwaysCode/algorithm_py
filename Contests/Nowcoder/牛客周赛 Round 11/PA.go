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

	var T, n, k int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &k, &n)
		ans := (n-1)%k + 1
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
