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

	var T, n, m, a int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &m)
		mp := map[int]bool{}
		ans := 0
		for ; n > 0; n-- {
			for j := 0; j < m; j++ {
				Fscan(in, &a)
				if !mp[a] {
					mp[a] = true
					ans++
				}
			}
		}

		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
