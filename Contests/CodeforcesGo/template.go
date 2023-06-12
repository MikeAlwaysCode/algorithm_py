// package main CP in Go is fun!
// But the kid is not my son
// She says I am the one,
package main

import (
	"bufio"
	"bytes"
	"container/heap"
	"fmt"
	"index/suffixarray"
	"math"
	"math/bits"
	"math/rand"
	"os"
	"reflect"
	"sort"
	"strconv"
	"strings"
	"time"
)

// MULTITESTS is 1 if multitests are used in a problem, otherwise it's 0
const MULTITESTS int = 1

func solve() {
	n := ri()
	for i := 0; i < n; i++ {
		printf("%d ", n-ri()+1)
	}
	println()
}

func main() {
	checkIfOnLocal()
	defer flush() // don't forget to flush the output at the end

	t := 1
	if MULTITESTS == 1 {
		t = ri()
	}

	startTime := time.Now()
	for t > 0 {
		t--
		solve()
	}
	timeUsed := time.Since(startTime)

	debugf("Time used: %.2fs\n", timeUsed.Seconds())

	// Go gives you an error if you don't use an imported package
	use(time.After)
	use(fmt.Append)
	use(math.Abs)
	use(rand.ExpFloat64)
	use(strings.Split)
	use(bufio.NewWriter)
	use(os.Args)
	use(sort.Ints)
	use(strconv.AppendBool)
	use(heap.Init)
	use(reflect.Append)
	use(bytes.Compare)
	use(bits.LeadingZeros32)
	use(suffixarray.New)
}

// this is a functiong to deal with Go being overprotective
func use(thing ...any) {
	_ = thing
}

// to distinguish between online judge and my local pc
var onLocal = false

// the name talks for itself
func checkIfOnLocal() {
	if os.Getenv("CP_GO") == "LOCAL" {
		onLocal = true
	} else {
		onLocal = false
	}
}

//! this is a collection of interfaces

// represents a signed integer
type signed interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64
}

// represents an unsigned integer
type unsigned interface {
	~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64
}

// represents an integer
type integer interface {
	signed | unsigned
}

// represents a float
type float interface {
	~float32 | ~float64
}

// represents a number
type number interface {
	integer | float
}

// represents a comparator
type comparator[T any] interface {
	Less(first, second T) bool    // true if first has less priority than second
	Equal(first, second T) bool   // true if first has less priority than second
	Greater(first, second T) bool // true if first has less priority than second
}

// less comparator for numbers
type less[T number] struct{}

func (c less[T]) Less(first, second T) bool    { return first < second }
func (c less[T]) Equal(first, second T) bool   { return first == second }
func (c less[T]) Greater(first, second T) bool { return first > second }

// greater comparator for numbers
type greater[T number] struct{}

func (c greater[T]) Less(first, second T) bool    { return first > second }
func (c greater[T]) Equal(first, second T) bool   { return first == second }
func (c greater[T]) Greater(first, second T) bool { return first < second }

type comparatorWrapper[T any, C comparator[T]] struct {
	comp C
}

func (c comparatorWrapper[T, C]) Less(first, second T) bool         { return c.comp.Less(first, second) }
func (c comparatorWrapper[T, C]) Greater(first, second T) bool      { return c.comp.Greater(second, first) }
func (c comparatorWrapper[T, C]) Equal(first, second T) bool        { return c.comp.Equal(first, second) }
func (c comparatorWrapper[T, C]) LessEqual(first, second T) bool    { return !c.Greater(first, second) }
func (c comparatorWrapper[T, C]) GreaterEqual(first, second T) bool { return !c.Less(first, second) }

//! these are some core functions. i will use them in all my structures

// returns type of x
func typeOf(x any) string {
	kind := reflect.TypeOf(x).Kind().String()
	return kind
}

func min[T number](args ...T) T {
	res := args[0]
	for _, x := range args {
		if x < res {
			res = x
		}
	}
	return res
}

func max[T number](args ...T) T {
	res := args[0]
	for _, x := range args {
		if x > res {
			res = x
		}
	}
	return res
}

func sum[T number](args ...T) T {
	res := args[0]
	for i := 1; i < len(args); i++ {
		res += args[i]
	}
	return res
}

func gcd[T integer](args ...T) (res T) {
	for _, val := range args {
		val = abs(val)
		if res > val {
			res, val = val, res
		}
		for res > 0 {
			res, val = val%res, res
		}
		res = val
	}
	return res
}

func lcm[T integer](args ...T) (res T) {
	res = 1
	for _, val := range args {
		res = res / gcd(res, val) * val
	}
	return res
}

func abs[T number](x T) T {
	if x < 0 {
		return -x
	}
	return x
}

func bpowm[T integer](base, exp, mod T) T {
	res := T(1)
	for exp > 0 {
		if (exp & 1) == 1 {
			res = res * base % mod
		}
		exp >>= 1
		base = base * base % mod
	}
	return res
}

func invm[T integer](x, mod T) T {
	return bpowm(x, mod-2, mod)
}

func reverse[T any](x []T) {
	for i := 0; i < len(x)/2; i++ {
		x[i], x[len(x)-i-1] = x[len(x)-i-1], x[i]
	}
}

func fill[T any](arr []T, x T) {
	for i := range arr {
		arr[i] = x
	}
}

func insert[T any](arr []T, pos int, x T) []T {
	res := append(arr[:pos+1], arr[pos:]...)
	res[pos] = x
	return res
}

func lowerBound[T number](arr []T, x T) int {
	L := -1
	R := len(arr)
	for R > L+1 {
		mid := (L + R) / 2
		if arr[mid] >= x {
			R = mid
		} else {
			L = mid
		}
	}
	return R
}

func upperBound[T number](arr []T, x T) int {
	L := -1
	R := len(arr)
	for R > L+1 {
		mid := (L + R) / 2
		if arr[mid] > x {
			R = mid
		} else {
			L = mid
		}
	}
	return R
}

//! these are some extra functions

// returns time in s since the Epoch.
// time complexity O(1).
// memory complexity O(1).
func getTime() float64 {
	return float64(time.Now().UnixNano()) / 1e9
}

// ! ds
type setNode[T any] struct {
	data           T
	priority, size int
	left, right    *setNode[T]
}

type set[T any, C comparator[T]] struct {
	root *setNode[T]
	comp C
}

func (s set[T, C]) _newNode(data T) *setNode[T] {
	return &setNode[T]{data, rand.Int(), 1, nil, nil}
}

func (s set[T, C]) _size(v *setNode[T]) int {
	if v == nil {
		return 0
	}
	return v.size
}

func (s set[T, C]) _recalc(v *setNode[T]) {
	if v != nil {
		v.size = 1 + s._size(v.left) + s._size(v.right)
	}
}

func (s set[T, C]) _split(v *setNode[T], cnt int) (*setNode[T], *setNode[T]) {
	if v == nil {
		return nil, nil
	}
	if s._size(v.left) >= cnt {
		left, right := s._split(v.left, cnt)
		v.left = right
		s._recalc(v)
		return left, v
	}

	left, right := s._split(v.right, cnt-s._size(v.left)-1)
	v.right = left
	s._recalc(v)
	return v, right
}

// core. splits the treap node into smaller and larger group than val
func (s set[T, C]) _splitOrdered(v *setNode[T], val T) (*setNode[T], *setNode[T]) {
	if v == nil {
		return nil, nil
	}

	if s.comp.Less(val, v.data) {
		left, right := s._splitOrdered(v.left, val)
		v.left = right
		s._recalc(v)
		return left, v
	}

	left, right := s._splitOrdered(v.right, val)
	v.right = left
	s._recalc(v)
	return v, right
}

func (s set[T, C]) _splitDeletePos(v *setNode[T], pos int) (*setNode[T], *setNode[T]) {
	if v == nil {
		return nil, nil
	}

	if s._size(v.left) > pos {
		left, right := s._splitDeletePos(v.left, pos)
		v.left = right
		s._recalc(v)
		return left, v
	} else if s._size(v.left) < pos {
		left, right := s._splitDeletePos(v.right, pos-s._size(v.left)-1)
		v.right = left
		s._recalc(v)
		return v, right
	}

	return v.left, v.right
}

func (s set[T, C]) _merge(a *setNode[T], b *setNode[T]) *setNode[T] {
	if a == nil {
		return b
	}
	if b == nil {
		return a
	}

	if a.priority < b.priority {
		a.right = s._merge(a.right, b)
		s._recalc(a)
		return a
	}

	b.left = s._merge(a, b.left)
	s._recalc(b)
	return b
}

func (s set[T, C]) _slice(v *setNode[T], res *[]T) {
	if v == nil {
		return
	}

	s._slice(v.left, res)
	*res = append(*res, v.data)
	s._slice(v.right, res)
}

func (s set[T, C]) size() int {
	return int(s._size(s.root))
}

func (s set[T, C]) empty() bool {
	return s.size() == 0
}

func (s *set[T, C]) clear() {
	s.root = nil
}

func (s set[T, C]) first() T {
	if s.empty() {
		panic("")
	}
	v := s.root
	for v.left != nil {
		v = v.left
	}
	return v.data
}

func (s set[T, C]) last() T {
	if s.empty() {
		panic("")
	}
	v := s.root
	for v.right != nil {
		v = v.right
	}
	return v.data
}

func (s set[T, C]) atPos(pos int) T {
	v := s.root
	for v != nil {
		if s._size(v.left) == pos {
			break
		}
		if s._size(v.left) > pos {
			v = v.left
		} else {
			pos -= s._size(v.left) + 1
			v = v.right
		}
	}
	return v.data
}

func (s set[T, C]) contains(x T) bool {
	v := s.root
	for v != nil {
		if s.comp.Equal(x, v.data) {
			return true
		}

		if s.comp.Less(x, v.data) {
			v = v.left
		} else {
			v = v.right
		}
	}
	return false
}

func (s set[T, C]) countLess(x T) int {
	v := s.root
	res := 0
	for v != nil {
		if s.comp.Less(v.data, x) {
			res += s._size(v.left) + 1
			v = v.right
		} else {
			v = v.left
		}
	}
	return res
}

func (s set[T, C]) countGreater(x T) int {
	v := s.root
	res := 0
	for v != nil {
		if s.comp.Greater(v.data, x) {
			res += s._size(v.right) + 1
			v = v.left
		} else {
			v = v.right
		}
	}
	return res
}

func (s set[T, C]) countEqual(x T) int {
	return s.size() - s.countLess(x) - s.countGreater(x)
}

func (s *set[T, C]) insert(data ...T) {
	for _, x := range data {
		left, right := s._splitOrdered(s.root, x)
		s.root = s._merge(left, s._merge(s._newNode(x), right))
	}
}

func (s *set[T, C]) insertUnique(data ...T) {
	for _, x := range data {
		if !s.contains(x) {
			s.insert(x)
		}
	}
}

func (s *set[T, C]) delete(data ...T) {
	for _, x := range data {
		//s.root = s._merge(s._splitDelete(s.root, x))
		s.deleteAt(s.countLess(x))
	}
}

func (s *set[T, C]) deleteAt(pos int) {
	if 0 <= pos && pos < s.size() {
		s.root = s._merge(s._splitDeletePos(s.root, pos))
	}
}

func (s *set[T, C]) next(x T) (T, bool) {
	var res T
	found := false

	v := s.root
	for v != nil {
		if !s.comp.Less(x, v.data) {
			v = v.right
			continue
		}

		found = true
		res = v.data
		v = v.left
	}
	return res, found
}

func (s *set[T, C]) nextOrEqual(x T) (T, bool) {
	var res T
	found := false

	v := s.root
	for v != nil {
		if s.comp.Greater(x, v.data) {
			v = v.right
			continue
		}

		found = true
		res = v.data
		v = v.left
	}
	return res, found
}

func (s *set[T, C]) prev(x T) (T, bool) {
	var res T
	found := false

	v := s.root
	for v != nil {
		if !s.comp.Greater(x, v.data) {
			v = v.left
			continue
		}

		found = true
		res = v.data
		v = v.right
	}
	return res, found
}

func (s *set[T, C]) prevOrEqual(x T) (T, bool) {
	var res T
	found := false

	v := s.root
	for v != nil {
		if s.comp.Less(x, v.data) {
			v = v.left
			continue
		}

		found = true
		res = v.data
		v = v.right
	}
	return res, found
}

func (s *set[T, C]) init(data ...T) {
	s.insert(data...)
}

func (s set[T, C]) slice() []T {
	var res []T
	s._slice(s.root, &res)
	return res
}

func (s set[T, C]) str() string {
	return fmt.Sprint(s.slice())
}

type binHeap[T any, C comparator[T]] struct {
	data []T
	comp C
}

func (h binHeap[T, C]) size() int {
	return len(h.data)
}

func (h binHeap[T, C]) empty() bool {
	return h.size() == 0
}

func (h *binHeap[T, C]) insert(x T) {
	v := h.size()
	h.data = append(h.data, x)

	for v != 0 {
		par := (v - 1) >> 1
		if h.comp.Less(h.data[v], h.data[par]) {
			h.data[v], h.data[par] = h.data[par], h.data[v]
			v = par
		} else {
			break
		}
	}
}

func (h *binHeap[T, C]) deleteFirst() {
	h.data[0], h.data[h.size()-1] = h.data[h.size()-1], h.data[0]
	h.data = h.data[:len(h.data)-1]
	v := 0
	n := h.size()
	for (v<<1 | 1) < n {
		kid1, kid2 := v<<1|1, (v<<1)+2
		if kid2 < n && h.comp.Greater(h.data[kid1], h.data[kid2]) {
			kid1, kid2 = kid2, kid1
		}
		if h.comp.Less(h.data[v], h.data[kid1]) {
			break
		}
		h.data[v], h.data[kid1] = h.data[kid1], h.data[v]
		v = kid1
	}
}

func (h *binHeap[T, C]) clear() {
	h.data = make([]T, 0)
}

func (h binHeap[T, C]) first() T {
	return h.data[0]
}

func (h binHeap[T, C]) slice() []T {
	res := make([]T, h.size())
	copy(res, h.data)
	sort.Slice(res, func(i, j int) bool {
		return h.comp.Less(h.data[i], h.data[j])
	})
	return res
}

func (h binHeap[T, C]) str() string {
	return fmt.Sprint(h.slice())
}

// ! io
var stdout = bufio.NewWriter(os.Stdout)
var stdin = bufio.NewReader(os.Stdin)
var inputString string
var inputStringPtr int

// prints space-separated args
func print(args ...any) { fmt.Fprint(stdout, args...) }

// prints args with a given format f
func printf(f string, args ...any) { fmt.Fprintf(stdout, f, args...) }

// prints space-separated args and adds a newline
func println(args ...any) { fmt.Fprintln(stdout, args...) }

// prints space-separated args if onLocal is true
func debug(args ...any) {
	if onLocal {
		print(args...)
		flush()
	}
}

// prints args with a given format f if onLocal is true
func debugf(f string, args ...any) {
	if onLocal {
		printf(f, args...)
		flush()
	}
}

// prints space-separated args and adds a newline if onLocal is true
func debugln(args ...any) {
	if onLocal {
		println(args...)
		flush()
	}
}

// flushes stdout writer
func flush() {
	stdout.Flush()
}

// reads a string from stdin
func readString() string {
	str, _ := stdin.ReadString('\n')
	return strings.Trim(str, "\n\r")
}

// reads a string from stdin if necesarry
func readStringIfNecessary() {
	if inputStringPtr == len(inputString) {
		inputString = readString()
		inputStringPtr = 0
	}
}

// skips all spaces in the input until it meets a non-space character
func skipSpaces() {
	readStringIfNecessary()
	for {
		readStringIfNecessary()
		for ; inputStringPtr < len(inputString); inputStringPtr++ {
			if inputString[inputStringPtr] == ' ' {
				continue
			} else {
				break
			}
		}
		if inputStringPtr != len(inputString) {
			break
		}
	}
}

// if n > 0, reads at most n non-space characters.
// if n = 0 reads a full non-space token.
// if n = -1 reads a full string with spaces included.
func nextToken(n int) string {
	if n == -1 {
		for inputStringPtr == len(inputString) {
			readStringIfNecessary()
		}
		start := inputStringPtr
		inputStringPtr = len(inputString)
		return inputString[start:]
	}

	if n == 0 {
		n = math.MaxInt
	}

	skipSpaces()
	start := inputStringPtr
	cnt := 0
	for inputStringPtr < len(inputString) {
		if inputString[inputStringPtr] == ' ' {
			break
		} else {
			cnt++
			inputStringPtr++
			if cnt == n {
				break
			}
		}
	}
	return inputString[start : start+cnt]
}

func readSingle(i any) {
	var token string

	switch v := i.(type) {
	case *int:
		token = nextToken(0)
		*v, _ = strconv.Atoi(token)
	case *uint:
		token = nextToken(0)
		x, _ := strconv.ParseUint(token, 10, 64)
		*v = uint(x)

	case *int8:
		token = nextToken(0)
		x, _ := strconv.ParseInt(token, 10, 8)
		*v = int8(x)
	case *int16:
		token = nextToken(0)
		x, _ := strconv.ParseInt(token, 10, 16)
		*v = int16(x)
	case *int32:
		token = nextToken(0)
		x, _ := strconv.ParseInt(token, 10, 32)
		*v = int32(x)
	case *int64:
		token = nextToken(0)
		*v, _ = strconv.ParseInt(token, 10, 64)

	case *uint8:
		token = nextToken(0)
		x, _ := strconv.ParseUint(token, 10, 8)
		*v = uint8(x)
	case *uint16:
		token = nextToken(0)
		x, _ := strconv.ParseUint(token, 10, 16)
		*v = uint16(x)
	case *uint32:
		token = nextToken(0)
		x, _ := strconv.ParseUint(token, 10, 32)
		*v = uint32(x)
	case *uint64:
		token = nextToken(0)
		*v, _ = strconv.ParseUint(token, 10, 64)

	case *float32:
		token = nextToken(0)
		x, _ := strconv.ParseFloat(token, 32)
		*v = float32(x)
	case *float64:
		token = nextToken(0)
		*v, _ = strconv.ParseFloat(token, 64)

	case *string:
		token = nextToken(0)
		*v = token
	}
}

// reads a full slice
func readSlice[T any](arg []T) {
	for i := range arg {
		readSingle(&arg[i])
	}
}

// reads many arguments with readSingle()
func readMany(args ...any) {
	for _, val := range args {
		readSingle(val)
	}
}

// reads and returns an int
func ri() int {
	var x int
	readSingle(&x)
	return x
}

// reads and returns an int8
func ri8() int8 {
	var x int8
	readSingle(&x)
	return x
}

// reads and returns an int16
func ri16() int16 {
	var x int16
	readSingle(&x)
	return x
}

// reads and returns an int32
func ri32() int32 {
	var x int32
	readSingle(&x)
	return x
}

// reads and returns an int64
func ri64() int64 {
	var x int64
	readSingle(&x)
	return x
}

// reads and returns a uint
func ru() uint {
	var x uint
	readSingle(&x)
	return x
}

// reads and returns a uint8
func ru8() uint8 {
	var x uint8
	readSingle(&x)
	return x
}

// reads and returns a uint16
func ru16() uint16 {
	var x uint16
	readSingle(&x)
	return x
}

// reads and returns a uint32
func ru32() uint32 {
	var x uint32
	readSingle(&x)
	return x
}

// reads and returns a uint64
func ru64() uint64 {
	var x uint64
	readSingle(&x)
	return x
}

// reads and returns a float32
func rf32() float32 {
	var x float32
	readSingle(&x)
	return x
}

// reads and returns a float64
func rf64() float64 {
	var x float64
	readSingle(&x)
	return x
}

// reads and returns a string of non-space characters
func rstr() string {
	var x string
	readSingle(&x)
	return x
}

// reads and returns a single byte(character) from stdin
func rb() byte {
	return nextToken(1)[0]
}

// reads and returns a full string from stdin
func rfullString() string {
	return nextToken(-1)
}

// reads and returns a slice of length n
func rs[T any](n int) []T {
	res := make([]T, n)
	readSlice(res)
	return res
}
