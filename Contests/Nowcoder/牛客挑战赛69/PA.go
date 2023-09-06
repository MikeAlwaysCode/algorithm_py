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

	var n int64
	Fscan(in, &n)
	MOD := int64(998244353)

	ans := int64(1)
	for i := int64(2); i <= n; i++ {
		ans = (ans * i) % MOD
	}
	ans = (ans - 1 + MOD) % MOD
	d := n * (n - 1) / 2 % MOD
	ans = (ans - d + MOD) % MOD
	d = n * (n - 1) * (n - 2) / 3 % MOD
	ans = (ans - d + MOD) % MOD
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }
