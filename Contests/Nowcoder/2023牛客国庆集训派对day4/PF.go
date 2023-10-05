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

	var T, a, b, c, d int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &a, &b, &c, &d)
		var nearA, nearB string
		if a < b {
			nearA = "C"
		} else {
			nearA = "D"
		}
		if c < d {
			nearB = "C"
		} else {
			nearB = "D"
		}
		if nearA == nearB {
			if nearA == "C" {
				if b < d {
					nearA = "D"
				} else {
					nearB = "D"
				}
			} else {
				if a < c {
					nearA = "C"
				} else {
					nearB = "C"
				}
			}
		}

		Fprintln(out, "AB//"+nearA+nearB)
	}
}

func main() { solve(os.Stdin, os.Stdout) }
