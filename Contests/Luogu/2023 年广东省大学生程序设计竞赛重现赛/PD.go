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

	var T, n, m, a, b int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &m)
		ans := 0
		nums := make([]int, n)
		for i := range nums {
			Fscan(in, &a, &b)
			ans += a
			nums[i] = b - a
		}
		if n == 1 {
			ans += nums[0]
			Fprintln(out, ans)
			continue
		}

		sort.Ints(nums)
		i := n - 1
		for ; m > n && i > 0; m-- {
			if nums[i] <= 0 {
				break
			}
			if i == 1 {
				if nums[0]+nums[1] > 0 {
					ans += nums[0] + nums[1]
				}
				break
			}
			ans += nums[i]
			i--
		}

		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
