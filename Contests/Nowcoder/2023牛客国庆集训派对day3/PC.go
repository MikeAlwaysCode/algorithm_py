package main

import (
	"bufio"
	. "fmt"
	"io"
	"math"
	"os"
)

func solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	type pair struct{ x, y float64 }

	var T int
	for Fscan(in, &T); T > 0; T-- {
		point := make([]pair, 20)
		for i := range point {
			Fscan(in, &point[i].x, &point[i].y)
		}
		zz := func(p1, p2 pair) float64 {
			return math.Round(math.Sqrt(math.Abs(p1.x-p2.x)*math.Abs(p1.x-p2.x) + math.Abs(p1.y-p2.y)*math.Abs(p1.y-p2.y)))
		}
		// Find segment length 6 & 9
		a, b, c := pair{}, pair{}, pair{}
		for i := range point {
			d1 := zz(point[i], point[(i+1)%20])
			d2 := zz(point[(i+1)%20], point[(i+2)%20])
			if d1 == 6 && d2 == 9 {
				a, b, c = point[i], point[(i+1)%20], point[(i+2)%20]
				break
			} else if d1 == 9 && d2 == 6 {
				a, b, c = point[(i+2)%20], point[(i+1)%20], point[i]
				break
			}
		}

		p1 := pair{b.x - a.x, b.y - a.y}
		p2 := pair{c.x - b.x, c.y - b.y}
		if p1.x*p2.y-p1.y*p2.x > 0 {
			Fprintln(out, "right")
		} else {
			Fprintln(out, "left")
		}

	}
}

func main() { solve(os.Stdin, os.Stdout) }
