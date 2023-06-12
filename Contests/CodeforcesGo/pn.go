package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func ReadInt(in *bufio.Reader) int {
	nStr := ReadString(in)
	n, _ := strconv.Atoi(nStr)
	return n
}

func ReadString(r *bufio.Reader) string {
	s, _ := r.ReadString('\n')
	return strings.TrimSpace(s)
}

func ReadInts(r *bufio.Reader) (int, int) {
	splitted := strings.Split(ReadString(r), " ")
	first, _ := strconv.Atoi(splitted[0])
	second, _ := strconv.Atoi(splitted[1])

	return first, second
}

func ReadArrInt(in *bufio.Reader) []int {
	numbs := readLineNumbs(in)
	arr := make([]int, len(numbs))
	for i, n := range numbs {
		val, _ := strconv.Atoi(n)
		arr[i] = val
	}
	return arr
}

func readLineNumbs(in *bufio.Reader) []string {
	line := ReadString(in)
	numbs := strings.Split(line, " ")
	return numbs
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}

func PrintlnArr(writer *bufio.Writer, arr []int) {
	for i := 0; i < len(arr); i++ {
		PrintInt(writer, arr[i])
		if i != len(arr)-1 {
			writer.WriteByte(' ')
		}
	}
	writer.WriteByte('\n')
}

func PrintlnInt(writer *bufio.Writer, n int) {
	PrintInt(writer, n)
	writer.WriteByte('\n')
}

func PrintlnString(writer *bufio.Writer, s string) {
	writer.WriteString(s)
	writer.WriteByte('\n')
}

func PrintInt(writer *bufio.Writer, n int) {
	writer.WriteString(strconv.Itoa(n))
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	t := ReadInt(reader)
	for i := 0; i < t; i++ {
		nums := ReadArrInt(reader)
		_, k, q := nums[0], nums[1], nums[2]
		a := ReadArrInt(reader)
		res := solve(a, k, q)
		PrintlnInt(writer, res)
	}
}

func solve(arr []int, k, q int) int {
	res := 0

	l := 0

	for r := 0; r < len(arr); r++ {
		if arr[r] > q {
			l = r + 1
			continue
		}

		if r-l+1 >= k {
			res += r - k - l + 2
		}
	}

	return res
}
