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
	var ans, tot int
	s := make([]string, n)
	trie := newTrie()
	for i := range s {
		Fscan(in, &s[i])
		tot += len(s[i])
		trie.insert((s[i]))
	}
	for i := range s {
		cnt := trie.search(s[i])
		ans += tot + len(s[i])*n - cnt*2
	}
	Fprintln(out, ans)
}

func main() { solve(os.Stdin, os.Stdout) }

type Trie struct {
	children map[byte]*Trie
	cnt      int
}

func newTrie() *Trie {
	m := map[byte]*Trie{}
	return &Trie{children: m}
}
func (this *Trie) insert(w string) {
	node := this
	for i := len(w) - 1; i >= 0; i-- {
		if _, ok := node.children[w[i]]; !ok {
			node.children[w[i]] = newTrie()
		}
		node, _ = node.children[w[i]]
		node.cnt++
	}
}
func (this *Trie) search(w string) int {
	node := this
	res := 0
	for i := range w {
		if _, ok := node.children[w[i]]; !ok {
			return res
		}
		node, _ = node.children[w[i]]
		res += node.cnt
	}
	return res
}
