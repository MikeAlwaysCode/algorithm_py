package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var n, x, a int
	Fscan(in, &n, &x)
	cnt := make([][]int, 31)
	for i := range cnt {
		cnt[i] = make([]int, 31)
	}
	for i := 0; i < n; i++ {
		Fscan(in, &a)
		c2, c5 := 0, 0
		for a%2 == 0 {
			c2++
			a /= 2
		}
		for a%5 == 0 {
			c5++
			a /= 5
		}
		cnt[c2][c5]++
	}
	ans := 0
	for i := 0; i < 31; i++ {
		for j := 0; j < 31; j++ {
			if cnt[i][j] == 0 {
				continue
			}
			if min(i+i, j+j) >= x {
				ans += cnt[i][j] * (cnt[i][j] - 1)
			}
			for k := 0; k < 31; k++ {
				for l := 0; l < 31; l++ {
					if i == k && j == l || cnt[k][l] == 0 {
						continue
					}
					if min(i+k, j+l) >= x {
						ans += cnt[i][j] * cnt[k][l]
					}
				}
			}
		}
	}
	ans /= 2
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
