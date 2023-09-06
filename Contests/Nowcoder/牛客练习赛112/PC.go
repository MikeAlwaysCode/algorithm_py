package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, a int
	Fscan(in, &n)
	pos := make([]int, n+1)
	for i := 1; i <= n; i++ {
		Fscan(in, &a)
		pos[a] = i
	}
	d := []int{}
	for i := 1; i <= n; i++ {
		Fscan(in, &a)
		a = pos[a]
		if len(d) == 0 || d[len(d)-1] < a {
			d = append(d, a)
		} else {
			// l, r := 0, len(d)-1
			// loc := r
			// for l <= r {
			// 	mid := (l + r) >> 1
			// 	if d[mid] >= a {
			// 		loc = mid
			// 		r = mid - 1
			// 	} else {
			// 		l = mid + 1
			// 	}
			// }
			// d[loc] = a
			j := sort.SearchInts(d, a)
			d[j] = a
		}
	}

	Fprintln(out, n-len(d))
}

func main() { solve(os.Stdin, os.Stdout) }
