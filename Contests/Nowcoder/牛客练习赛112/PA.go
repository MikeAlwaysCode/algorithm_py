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

	mx := int(1e6) + 1
	isprime := make([]bool, mx)
	for i := 2; i < mx; i++ {
		isprime[i] = true
	}
	primes := []int{}
	for i := 2; i < mx; i++ {
		if isprime[i] {
			primes = append(primes, i)
		}
		for _, p := range primes {
			if i*p >= mx {
				break
			}
			isprime[i*p] = false
			if i%p == 0 {
				break
			}
		}
	}

	var T, n int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n)
		check := true
		for n > 0 {
			if !isprime[n] {
				check = false
				break
			}
			n /= 10
		}
		if check {
			Fprintln(out, "YES")
		} else {
			Fprintln(out, "NO")
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
