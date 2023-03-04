package main

import (
	"bufio"
	. "fmt"
	"io"
	"math"
	"os"
	// "sort"
)

func CF1552D(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, n int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)

		set := map[int]bool{}
		check := false

		a := make([]int, n)
		for i := range a {
			Fscan(in, &a[i])
			a[i] = int(math.Abs(float64(a[i])))
			if !check && (a[i] == 0 || set[a[i]]) {
				check = true
			}
			set[a[i]] = true
		}
		if check {
			Fprintln(out, "YES")
			continue
		}
		for k := range set {
			delete(set, k)
		}

		for i := 1; i < 1<<n; i++ {
			cur := 0
			for j, v := range a {
				cur += i >> j & 1 * v
			}
			if set[cur] {
				check = true
				break
			}
			set[cur] = true
		}

		if check {
			Fprintln(out, "YES")
		} else {
			Fprintln(out, "NO")
		}
	}
}

func main() { CF1552D(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
