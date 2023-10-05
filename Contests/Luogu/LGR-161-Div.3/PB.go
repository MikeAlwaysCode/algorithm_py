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

	var T, n, p int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &p)
		if p > (n-1)/2 {
			Fprintln(out, -1)
		} else {
			ans := make([]byte, n)
			for i := range ans {
				ans[i] = '0'
			}
			for i := n - 2; i >= n-p*2; i -= 2 {
				ans[i+1] = '1'
				ans[i-1] = '1'
			}
			Fprintln(out, string(ans))
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
