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

	var n int
	var s string
	Fscan(in, &n)
	Fscanln(in, &s)
	software := map[string]bool{}
	data := map[string]bool{}
	for i := 0; i < n; i++ {
		// Fscanln(in, &s)
		res := []byte{}
		res, _, _ = in.ReadLine()
		s = string(res)
		// Fscan(in, &s)
		sp := strings.Fields(s)
		if sp[0] == "sudo" {
			if sp[1] == "pacman" {
				software[sp[len(sp)-1]] = true
				data[sp[len(sp)-1]] = true
			} else {
				Fprintln(out, "wuwuwu")
				break
			}
		} else if sp[0] == "pacman" {
			software[sp[2]] = false
			if sp[1] == "-Rscn" {
				data[sp[2]] = false
			}
		} else if sp[0] == "1" {
			if software[sp[1]] {
				Fprintln(out, "yes")
			} else {
				Fprintln(out, "no")
			}
		} else if sp[0] == "2" {
			if data[sp[1]] {
				Fprintln(out, "yes")
			} else {
				Fprintln(out, "no")
			}
		}
	}
}

func main() { solve(os.Stdin, os.Stdout) }
