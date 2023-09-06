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

	var n int
	Fscan(in, &n)

	a := make([]int, n)
	isprime := make([]bool, n+1)
	for i := range isprime {
		isprime[i] = true
	}
	a[0] = 1

	for i := 2; i <= n; i++ {
		if a[i-1] == 0 {
			if isprime[i] {
				if i < n {
					a[i-1] = i + 1
					a[i] = i
				} else {
					a[i-1] = a[i-2]
					a[i-2] = i
				}
			} else {
				a[i-1] = i
			}
		}
		for j := i + i; j <= n; j += i {
			isprime[j] = false
		}
	}

	for _, v := range a {
		Fprint(out, v, " ")
	}
	Fprintln(out)
}

func main() { solve(os.Stdin, os.Stdout) }
