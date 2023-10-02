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

	var s string
	var o string
	var q, x int
	Fscan(in, &s)
	n, index := len(s), 0
	for Fscan(in, &q); q > 0; q-- {
		Fscan(in, &o, &x)
		if o == "M" {
			index = (index + x + n) % n
		} else {
			Fprintln(out, string(s[(index+x-1)%n]))
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
