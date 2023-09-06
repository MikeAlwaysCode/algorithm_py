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

	var n string
	Fscan(in, &n)
	ans := 0
	for _, c := range n {
		if c == '0' || c == '6' || c == '9' {
			ans++
		} else if c == '8' {
			ans += 2
		}
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
