package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func CF1738C(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var T, n int
	for Fscan(in, &T); T > 0; T-- {

		a, odd, even := 0, 0, 0
		for Fscan(in, &n); n > 0; n-- {
			Fscan(in, &a)
			if a&1 > 0 {
				odd++
			} else {
				even++
			}
		}

		if (odd+1)>>1&1 == 0 || (odd&1 > 0 && even&1 > 0) {
			Fprintln(out, "Alice")
		} else {
			Fprintln(out, "Bob")
		}
	}
}

func main() { CF1738C(os.Stdin, os.Stdout) }
