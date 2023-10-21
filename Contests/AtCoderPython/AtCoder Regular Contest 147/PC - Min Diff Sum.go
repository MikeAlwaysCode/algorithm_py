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

	var n, ans int
	Fscan(in, &n)
	l := make([]int, n)
	r := make([]int, n)
	for i := range l {
		Fscan(in, &l[i], &r[i])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(l)))
	sort.Ints(r)
	for i := 0; l[i] > r[i]; i++ {
		ans += (l[i] - r[i]) * (n - i*2 - 1)
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
