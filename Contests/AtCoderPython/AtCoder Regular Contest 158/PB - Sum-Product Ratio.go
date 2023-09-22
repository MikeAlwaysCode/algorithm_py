package main

import (
	"bufio"
	. "fmt"
	"io"
	"math"
	"os"
	"sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, a int
	neg := []int{}
	pos := []int{}
	Fscan(in, &n)
	for i := 0; i < n; i++ {
		Fscan(in, &a)
		if a < 0 {
			neg = append(neg, a)
		} else {
			pos = append(pos, a)
		}
	}
	sort.Sort(sort.Reverse(sort.IntSlice(neg)))
	sort.Sort(sort.Reverse(sort.IntSlice(pos)))
	neg = append(neg, pos...)
	mn, mx := 3., -3.
	res := float64(neg[0]+neg[1]+neg[2]) / float64(neg[0]*neg[1]*neg[2])
	mn = math.Min(mn, res)
	mx = math.Max(mx, res)
	res = float64(neg[0]+neg[1]+neg[n-1]) / float64(neg[0]*neg[1]*neg[n-1])
	mn = math.Min(mn, res)
	mx = math.Max(mx, res)
	res = float64(neg[0]+neg[n-1]+neg[n-2]) / float64(neg[0]*neg[n-1]*neg[n-2])
	mn = math.Min(mn, res)
	mx = math.Max(mx, res)
	res = float64(neg[n-1]+neg[n-2]+neg[n-3]) / float64(neg[n-1]*neg[n-2]*neg[n-3])
	mn = math.Min(mn, res)
	mx = math.Max(mx, res)
	Fprintln(out, mn)
	Fprintln(out, mx)
}

func main() { solve(os.Stdin, os.Stdout) }
