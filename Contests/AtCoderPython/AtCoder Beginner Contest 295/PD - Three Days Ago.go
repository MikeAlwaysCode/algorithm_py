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
	Fscan(in, &s)
	var ans, mask int
	cnt := [1024]int{1}
	for _, c := range s {
		mask ^= 1 << int(c-'0')
		ans += cnt[mask]
		cnt[mask]++
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
