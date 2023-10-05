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

	const mod int = 1e9 + 7
	var n int
	Fscan(in, &n)
	ans := 0
	a := make([]int, n)
	for i := range a {
		Fscan(in, &a[i])
	}
	cnt := 0
	// cnt, s := 0, 0
	for i := n - 1; i >= 0; i-- {
		if a[i] == 5 {
			cnt += 1
			ans = (ans + (i+1)*cnt) % mod
		} else {
			cnt = 0
		}
		// s = (s + cnt) % mod
		// ans = (ans + s) % mod
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
