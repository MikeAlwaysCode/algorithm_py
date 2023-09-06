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

	var s, t string
	Fscan(in, &s, &t)
	n := len(s)
	ans := 0
	for i := 0; i < n; i++ {
		check := true
		for j := 0; j < len(t); j++ {
			if s[(i+j)%n] != t[j] {
				check = false
				break
			}
		}
		if check {
			ans++
		}
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
