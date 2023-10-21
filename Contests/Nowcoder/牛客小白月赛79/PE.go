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

	var n, m int
	Fscan(in, &n, &m)
	if n < 7 {
		Fprintln(out, -1)
		return
	}
	ans := 6 * n % 10
	for i := 0; i < 2 && i < m; i++ {
		ans = ans * ans % 10
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
