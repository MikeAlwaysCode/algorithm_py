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

	var T int
	var s, t string
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &s, &t)
		cnts := [26]int{}
		for _, c := range s {
			cnts[int(c-'a')]++
		}
		cntt := [26]int{}
		for _, c := range t {
			cntt[int(c-'a')]++
		}
		ans := int(1e6)
		for i := 0; i < 26; i++ {
			if cntt[i] > 0 {
				ans = min(ans, cnts[i]/cntt[i])
			}
		}

		// n := len(t)
		// pi := make([]int, n)
		// for i := 1; i < n; i++ {
		// 	j := pi[i-1]
		// 	for j > 0 && t[i] != t[j] {
		// 		j = pi[j-1]
		// 	}
		// 	if t[i] == t[j] {
		// 		j++
		// 	}
		// 	pi[i] = j
		// }
		// ans := 0
		// j := 0
		// for i := 0; i < len(s); i++ {
		// 	if s[i] == t[j] {
		// 		j++
		// 		if j == n {
		// 			ans++
		// 			j = pi[n-1]
		// 		}
		// 	}
		// }
		Fprintln(out, ans)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}
