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

	var n, k int
	Fscan(in, &n, &k)
	if n < k*3 {
		Fprintln(out, -1)
	} else {
		t := "you"
		ans := make([]byte, n)
		for i := 0; i < n; i++ {
			if i >= k*3 {
				ans[i] = 'y'
			} else {
				ans[i] = t[i%3]
			}
		}
		Fprintln(out, string(ans))
	}

}

func main() { solve(os.Stdin, os.Stdout) }
