package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	// "sort"
)

func Solve(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()

	var s string
	Fscan(in, &s)
	ans0, ans1 := 0, 1

	stack := []int{}
	stack = append(stack, -1)
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			stack = append(stack, i)
		} else {
			stack = stack[:len(stack)-1]
			if len(stack) == 0 {
				stack = append(stack, i)
			} else {
				curLen := i - stack[len(stack)-1]
				if curLen > ans0 {
					ans0 = i - stack[len(stack)-1]
					ans1 = 1
				} else if curLen == ans0 {
					ans1++
				}
			}
		}
	}

	// var maxLen, cnt, left, right int
	// for _, c := range s {
	// 	if c == '(' {
	// 		left++
	// 	} else {
	// 		right++
	// 	}
	// 	if left == right {
	// 		if right*2 > maxLen {
	// 			maxLen = right * 2
	// 			cnt = 1
	// 		} else if right*2 == maxLen {
	// 			cnt++
	// 		}
	// 	} else if left < right {
	// 		left, right = 0, 0
	// 	}
	// }
	// if maxLen > ans0 {
	// 	ans0, ans1 = maxLen, cnt
	// }
	// maxLen, cnt, left, right = 0, 0, 0, 0
	// for i := len(s) - 1; i >= 0; i-- {
	// 	if s[i] == '(' {
	// 		left++
	// 	} else {
	// 		right++
	// 	}
	// 	if left == right {
	// 		if right*2 > maxLen {
	// 			maxLen = right * 2
	// 			cnt = 1
	// 		} else if right*2 == maxLen {
	// 			cnt++
	// 		}
	// 	} else if left > right {
	// 		left, right = 0, 0
	// 	}
	// }
	// if maxLen > ans0 {
	// 	ans0, ans1 = maxLen, cnt
	// } else if maxLen == ans0 {
	// 	ans1 = max(ans1, cnt)
	// }

	Fprintln(out, ans0, ans1)
}

func main() { Solve(os.Stdin, os.Stdout) }
func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
