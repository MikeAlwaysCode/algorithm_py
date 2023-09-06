package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"strings"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var s string
	Fscan(in, &s)

	if strings.Contains(s, "ove") || strings.Contains(s, "lve") || strings.Contains(s, "loe") || strings.Contains(s, "lov") {
		Fprintln(out, "YES")
	} else {
		Fprintln(out, "NO")
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
