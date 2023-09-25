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
	var s string
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &s)
		ans := []byte{}
		p := []byte{}
		cnt, l2 := 0, 0
		for i := range s {
			if len(p) == 0 {
				p = append(p, s[i])
				cnt = 1
			} else if int(s[i]-p[len(p)-1]) == 1 && int(p[0]-s[i]) == 1 {
				ans = append(ans, s[i])
			} else if s[i] == '0' && (int(p[len(p)-1]-s[i]) == 9 || int(p[len(p)-1]-s[i]) == 1) {
				if l2 > 0 {
					ans = append(ans, p[:l2]...)
					p = p[l2:]
					l2 = 0
				}
				ans = append(ans, s[i])
			} else if int(p[len(p)-1]-s[i]) == 1 {
				ans = append(ans, p[:len(p)-cnt]...)
				ans = append(ans, s[i])
				p = p[len(p)-cnt:]
				l2 = 0
			} else if p[len(p)-1] == s[i] {
				p = append(p, s[i])
				cnt++
			} else if int(p[len(p)-1]-s[i]) == 2 {
				ans = append(ans, p[:len(p)-cnt]...)
				p = p[len(p)-cnt:]
				l2 = cnt
				p = append(p, s[i])
				cnt = 1
			} else if (p[len(p)-1] == '9' || p[len(p)-1] == '1') && (s[i] == '9' || s[i] == '1') {
				if l2 > 0 {
					ans = append(ans, p[:l2]...)
					p = p[l2:]
					l2 = 0
				}
				p = append(p, s[i])
				cnt = 1
			} else {
				ans = append(ans, p...)
				p = []byte{s[i]}
				l2, cnt = 0, 1
			}
		}
		ans = append(ans, p...)
		Fprintln(out, string(ans))
	}
}

func main() { solve(os.Stdin, os.Stdout) }
