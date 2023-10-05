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

	var n int
	var s string
	Fscan(in, &n)
	ans := []int{}
	for i := 1; i <= n; i++ {
		Fscan(in, &s)
		if s != "AC" {
			ans = append(ans, i)
		}
	}
	for _, v := range ans {
		Fprint(out, v, " ")
	}
}

func main() { solve(os.Stdin, os.Stdout) }
