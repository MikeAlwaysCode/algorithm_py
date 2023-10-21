package main

import (
	"bufio"
	. "fmt"
	"io"
	"math/bits"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, n int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		ans := 21 - bits.Len(uint(n&(-n)))
		if ans <= 0 {
			Fprintln(out, 0)
			continue
		}
		for i := 1; i < 20; i++ {
			lb := (n + i) & (-n - i)
			ans = min(ans, 21-min(21, bits.Len(uint(lb)))+i)
		}

		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
