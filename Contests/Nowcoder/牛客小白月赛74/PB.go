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

	var T, n int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		ans := []int{}
		for x := 1; n > 0; x++ {
			if n < x {
				ans[len(ans)-1] += n
				break
			} else {
				ans = append(ans, x)
				n -= x
			}
		}

		for _, v := range ans {
			Fprint(out, v, " ")
		}
		Fprintln(out)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
