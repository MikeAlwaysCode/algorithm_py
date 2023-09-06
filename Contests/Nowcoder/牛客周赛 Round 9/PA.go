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

	var T, m, x int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &m, &x)
		Fprintln(out, (x-1)%m+1)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
