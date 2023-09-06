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
	i, j := n, 1
	for i > j {
		Fprint(out, i, " ", j, " ")
		i--
		j++
	}
	if i == j {
		Fprint(out, i, " ")
	}
	Fprintln(out)
}

func main() { solve(os.Stdin, os.Stdout) }
