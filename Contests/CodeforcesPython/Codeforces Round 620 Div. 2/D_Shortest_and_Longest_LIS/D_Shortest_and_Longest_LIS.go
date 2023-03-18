package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func CF1304D(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, n int
	var s string
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &s)

		mn := make([]int, n)
		mx := make([]int, n)
		for i := 0; i < n; i++ {
			mn[i] = n - i
			mx[i] = i + 1
		}
		ll, rl := -1, -1
		for i := 0; i < n-1; i++ {
			if s[i] == '<' {
				if ll == -1 {
					ll = i
				}
				if rl != -1 {
					reverse(mx, rl, i)
					rl = -1
				}
			} else {
				if ll != -1 {
					reverse(mn, ll, i)
					ll = -1
				}
				if rl == -1 {
					rl = i
				}
			}
		}
		if ll != -1 {
			reverse(mn, ll, n-1)
		}
		if rl != -1 {
			reverse(mx, rl, n-1)
		}

		for _, v := range mn {
			Fprint(out, v, " ")
		}
		Fprintln(out)
		for _, v := range mx {
			Fprint(out, v, " ")
		}
		Fprintln(out)
	}
}

func main() { CF1304D(os.Stdin, os.Stdout) }
func reverse(nums []int, l, r int) {
	for l < r {
		nums[l] ^= nums[r]
		nums[r] ^= nums[l]
		nums[l] ^= nums[r]
		l++
		r--
	}
}
