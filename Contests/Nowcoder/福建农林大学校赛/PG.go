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

	mp := map[string]string{
		"XuSheng":    "DaBao",
		"GanNing":    "DaGui",
		"QuYi":       "BaiMa",
		"HuangZhong": "LaoBao",
	}

	var s string
	Fscan(in, &s)
	Fprintln(out, mp[s])
}

func main() { solve(os.Stdin, os.Stdout) }
