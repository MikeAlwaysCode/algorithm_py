package main

import (
	"bufio"
	. "fmt"
	"io"
	"math"
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
		ans := int(math.Ceil(math.Log2(float64(n))))
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
