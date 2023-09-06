package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n int
	Fscan(in, &n)
	a := make([]int, 4)
	for i := 0; i < 4; i++ {
		a[i] = (n >> (i * 8)) & 255
	}
	sort.Ints(a)
	ans := 0
	for i := 3; i >= 0; i-- {
		ans += a[i] << (i * 8)
	}

	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
