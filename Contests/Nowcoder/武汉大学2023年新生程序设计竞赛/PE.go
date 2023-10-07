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
	Fscan(in, &n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			Fprint(out, i*n+j+1, " ")
		}
		Fprintln(out)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
