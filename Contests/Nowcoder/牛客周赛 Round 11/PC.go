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

	var s string
	Fscan(in, &s)
	n := len(s)
	ans := 0
	for i := 0; i < n; i++ {
		cnt := [2]int{}
		for j := i; j < n; j++ {
			c := int(s[j] - '0')
			if c != (j-i)&1 {
				cnt[0]++
			} else {
				cnt[1]++
			}
			ans += min(cnt[0], cnt[1])
		}
	}
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
