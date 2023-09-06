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

	var n int
	var s string
	Fscan(in, &n)
	Fscan(in, &s)
	check := false
	for i := 0; i < n; i++ {
		if s[i*2:i*2+2] == "7z" {
			check = true
			break
		}
	}
	if check {
		Fprintln(out, "YES")
	} else {
		Fprintln(out, "NO")
	}
}

func main() { solve(os.Stdin, os.Stdout) }
