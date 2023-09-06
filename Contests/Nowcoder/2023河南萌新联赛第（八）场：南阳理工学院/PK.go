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

	var mx int = 1e6
	factor := make([]int, mx+1)
	for i := 2; i <= mx; i++ {
		if factor[i] != 0 {
			continue
		}
		for j := i; j <= mx; j += i {
			factor[j] = i
		}
	}
	pres := make([]int, mx+1)
	for i := 2; i <= mx; i++ {
		pres[i] = pres[i-1]
		if factor[i] == i {
			pres[i]++
		}
	}
	var T, l, r int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &l, &r)
		Fprintln(out, pres[r]-pres[l-1])
	}
}

func main() { solve(os.Stdin, os.Stdout) }
