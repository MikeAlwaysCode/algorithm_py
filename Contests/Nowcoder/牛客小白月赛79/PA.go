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
	Fscan(in, &n)
	ans := 0
	for n&1 > 0 {
		ans++
		n /= 10
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
