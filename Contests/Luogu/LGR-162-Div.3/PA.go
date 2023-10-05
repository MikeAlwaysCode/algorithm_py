package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"strings"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var s string
	Fscan(in, &s)
	ans := "solution-" + strings.ToLower(strings.ReplaceAll(s, "_", "-"))
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
