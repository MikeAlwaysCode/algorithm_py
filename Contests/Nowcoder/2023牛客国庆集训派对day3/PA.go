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

	var T, n int
	var s string
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &s)
		ans, bait := 0, 0
		for i := n - 1; i >= 0; i-- {
			if s[i] == '0' {
				bait++
			} else if s[i] == '1' {
				if bait > 0 {
					ans++
					bait--
				} else {
					bait++
				}
			} else {
				ans++
			}
		}

		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
