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

	var n, t int
	var k, b int
	mp := map[int]map[int]int{}
	ss := map[int]int{}
	cnt := 0
	Fscan(in, &n)
	for i := 0; i < n; i++ {
		Fscan(in, &t, &k, &b)
		if t == 1 {
			if submap, ok := mp[k]; ok {
				submap[b]++
			} else {
				submap := map[int]int{}
				submap[b]++
				mp[k] = submap
			}
			ss[k]++
			cnt++
		} else if t == 2 {
			ans := cnt - ss[k]
			Fprintln(out, ans)
		} else {
			cnt = ss[k]
			sm := map[int]int{}
			if submap, ok := mp[k]; ok {
				cnt -= submap[b]
				delete(submap, b)
				sm = submap
			}
			for k := range mp {
				delete(mp, k)
			}
			for k := range ss {
				delete(ss, k)
			}
			if cnt > 0 {
				mp[k] = sm
				ss[k] = cnt
			}
		}
	}

}

func main() { solve(os.Stdin, os.Stdout) }
