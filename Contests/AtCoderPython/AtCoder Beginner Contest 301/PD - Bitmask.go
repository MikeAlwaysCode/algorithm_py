package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var s string
	var n int64
	Fscan(in, &s, &n)
	ans, _ := strconv.ParseInt(strings.ReplaceAll(s, "?", "0"), 2, 64)
	if ans > n {
		Fprintln(out, -1)
		return
	}
	for i, c := range s {
		if c == '?' && ans+(1<<(len(s)-i-1)) <= n {
			ans += 1 << (len(s) - i - 1)
		}
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
