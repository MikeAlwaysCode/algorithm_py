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

	var s, t int
	Fscan(in, &s, &t)
	ans := 0
	for a := 0; a <= s; a++ {
		for b := 0; b <= s-a; b++ {
			for c := 0; c <= s-a-b; c++ {
				if a*b*c <= t {
					ans++
				}
			}
		}
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
