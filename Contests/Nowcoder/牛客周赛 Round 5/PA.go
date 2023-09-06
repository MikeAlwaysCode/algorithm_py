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

	var s string
	Fscan(in, &s)
	ans := []byte(s)
	for i, c := range ans {
		if c >= 'a' && c <= 'z' {
			ans[i] = (c-'a'+25)%26 + 'a'
		} else if c >= 'A' && c <= 'Z' {
			ans[i] = (c-'A'+1)%26 + 'A'
		}
	}

	Fprintln(out, string(ans))

}

func main() { solve(os.Stdin, os.Stdout) }
