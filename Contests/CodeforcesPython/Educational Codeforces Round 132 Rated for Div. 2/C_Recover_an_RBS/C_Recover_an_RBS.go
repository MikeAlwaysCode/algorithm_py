package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T int
	var s string
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &s)

		cnt, qc := 0, 0
		for _, c := range s {
			if c == '(' {
				cnt++
			} else if c == ')' {
				cnt--
				if cnt < 0 {
					// 当前)比(多，由于s必定是一个合法rbs，前面必须有一个?变成(
					cnt++
					qc--
				}
			} else {
				if cnt > 0 {
					qc++
				} else {
					// 如果前面()一样多，当前?不可能变成)
					cnt++
				}
			}

			if cnt == 0 && qc == 1 {
				// 如果前面()一样多，且存在一个?，则?不可能变成)
				cnt++
				qc--
			}
		}

		if abs(cnt) == qc || qc == 1 {
			Fprintln(out, "YES")
		} else {
			Fprintln(out, "NO")
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
func abs(a int) int {
	if a < 0 {
		return -a
	} else {
		return a
	}
}
