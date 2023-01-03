
#ifndef LOCAL
#pragma GCC optimize ("O3,inline,omit-frame-pointer,no-asynchronous-unwind-tables,fast-math")
#pragma GCC target("tune=native,avx")
#define NDEBUG 1
#endif
#include <stdio.h>
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <x86intrin.h>

using namespace std;

// Macros

#define FOR(i, n) for(int i = 0; i < (int)(n); ++i)
#define FORU(i, j, k) for(int i = (j); i <= (int)(k); ++i)
#define FORD(i, j, k) for(int i = (j); i >= (int)(k); --i)
#define let(x) if(x;1)

#define STRINGIZE(x) STRINGIZE2(x)
#define STRINGIZE2(x) #x
#define runtime_assert(x) do { if(!(x)) { throw runtime_error(__FILE__ ":" STRINGIZE(__LINE__) " Assertion failed: " #x); } } while(0)
#define impossible() do { throw runtime_error(__FILE__ ":" STRINGIZE(__LINE__) " impossible"); } while(0)
#define all(x) begin(x), end(x)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back

// Types

template <class T> using min_queue = priority_queue<T, vector<T>, greater<T>>;
template <class T> using max_queue = priority_queue<T>;


struct uint64_hash {
  static inline uint64_t rotr(uint64_t x, unsigned k) {
    return (x >> k) | (x << (8U * sizeof(uint64_t) - k));
  }

  static inline uint64_t hash_int(uint64_t x) noexcept {
    auto h1 = x * (uint64_t)(0xA24BAED4963EE407);
    auto h2 = rotr(x, 32U) * (uint64_t)(0x9FB21C651E98DF25);
    auto h = rotr(h1 + h2, 32U);
    return h;
  }

  size_t operator()(uint64_t x) const {
    static const uint64_t FIXED_RANDOM = std::chrono::steady_clock::now().time_since_epoch().count();
    return hash_int(x + FIXED_RANDOM);
  }
};

template <typename K, typename V, typename Hash = uint64_hash>
using hash_map = __gnu_pbds::gp_hash_table<K, V, Hash>;
template <typename K, typename Hash = uint64_hash>
using hash_set = hash_map<K, __gnu_pbds::null_type, Hash>;

// Printing

template<class T>
void print_collection(ostream& out, T const& x);

template<class A>
ostream& operator<<(ostream& out, vector<A> const& x) { print_collection(out, x); return out; }
template<class A, size_t N>
ostream& operator<<(ostream& out, array<A, N> const& x) { print_collection(out, x); return out; }
template<class A>
ostream& operator<<(ostream& out, deque<A> const& x) { print_collection(out, x); return out; }
// template<class A>
// ostream& operator<<(ostream& out, multiset<A> const& x) { print_collection(out, x); return out; }
// template<class A, class B>
// ostream& operator<<(ostream& out, multimap<A, B> const& x) { print_collection(out, x); return out; }
// template<class A>
// ostream& operator<<(ostream& out, set<A> const& x) { print_collection(out, x); return out; }
// template<class A, class B>
// ostream& operator<<(ostream& out, map<A, B> const& x) { print_collection(out, x); return out; }
// template<class A>
// ostream& operator<<(ostream& out, unordered_set<A> const& x) { print_collection(out, x); return out; }
// template<class A, class B>
// ostream& operator<<(ostream& out, unordered_map<A, B> const& x) { print_collection(out, x); return out; }


template<class T, size_t... I>
void print_tuple(ostream& out, T const& a, index_sequence<I...>);
template<class... A>
ostream& operator<<(ostream& out, tuple<A...> const& x) {
  print_tuple(out, x, index_sequence_for<A...>{});
  return out;
}

template<class T, size_t... I>
void print_tuple(ostream& out, T const& a, index_sequence<I...>){
  using swallow = int[];
  out << '(';
  (void)swallow{0, (void(out << (I == 0? "" : ", ") << get<I>(a)), 0)...};
  out << ')';
}

template<class T>
void print_collection(ostream& out, T const& x) {
  int f = 0;
  out << '[';
  for(auto const& i: x) {
    out << (f++ ? "," : "");
    out << i;
  }
  out << "]";
}

// Random

long long unsigned int rdtsc() { return __rdtsc(); }

thread_local static struct xorshift128_t {
  uint32_t x, y, z, w;

  xorshift128_t(uint64_t seed = rdtsc()) {
    reset(seed);
  }

  inline void reset(uint64_t seed = rdtsc()) {

    struct splitmix64_state {
      uint64_t s;

      uint64_t splitmix64() {
        uint64_t result = (s += 0x9E3779B97f4A7C15);
        result = (result ^ (result >> 30)) * 0xBF58476D1CE4E5B9;
        result = (result ^ (result >> 27)) * 0x94D049BB133111EB;
        return result ^ (result >> 31);
      }
    };

    splitmix64_state s { seed };

    x = (uint32_t)s.splitmix64();
    y = (uint32_t)s.splitmix64();
    z = (uint32_t)s.splitmix64();
    w = (uint32_t)s.splitmix64();
  }

  inline uint32_t xorshift128() {
    uint32_t t = x;
    t ^= t << 11;
    t ^= t >> 8;
    x = y; y = z; z = w;
    w ^= w >> 19;
    w ^= t;
    return w;
  }

  // UniformRandomBitGenerator interface
  using result_type = uint32_t;
  constexpr uint32_t min(){ return numeric_limits<uint32_t>::min(); }
  constexpr uint32_t max(){ return numeric_limits<uint32_t>::max(); }
  uint32_t operator()() { return randomInt32(); }

  long long int operator()(long long int m) { return random(m); }

  inline uint32_t randomInt32() {
    return xorshift128();
  }

  inline uint64_t randomInt64() {
    return (((uint64_t)randomInt32())<<32ll) | ((uint64_t)randomInt32());
  }

  inline long long int random(long long int r) {
    return randomInt64()%r;
  }

  inline long long int random(long long int l, long long int r) {
    return l + random(r-l+1);
  }

  inline double randomDouble() {
    return (double)randomInt32() / 4294967296.0;
  }

  inline float randomFloat() {
    return (float)randomInt32() / 4294967296.0;
  }
} RNG;

// Timer

struct timer {
  chrono::high_resolution_clock::time_point t_begin;

  timer() {
    t_begin = chrono::high_resolution_clock::now();
  }

  void reset() {
    t_begin = chrono::high_resolution_clock::now();
  }

  float elapsed() const {
    return chrono::duration<float>(chrono::high_resolution_clock::now() - t_begin).count();
  }
};

// Letrec

template<class Fun>
class letrec_result {
  Fun fun_;
  public:
    template<class T>
    explicit letrec_result(T &&fun): fun_(forward<T>(fun)) {}

    template<class ...Args>
    decltype(auto) operator()(Args &&...args) {
      return fun_(ref(*this), forward<Args>(args)...);
    }
};

template<class Fun>
decltype(auto) letrec(Fun &&fun) {
  return letrec_result<decay_t<Fun>>(forward<Fun>(fun));
}

// Util

template<class T>
T& smin(T& x, T const& y) { x = min(x,y); return x; }

template <class T>
T& smax(T& x, T const& y) { x = max(x, y); return x; }


// Debug

static inline void debug_impl_seq() {
  cerr << "}";
}

template <class T, class... V>
void debug_impl_seq(T const& t, V const&... v) {
  cerr << t;
  if(sizeof...(v)) { cerr << ", "; }
  debug_impl_seq(v...);
}

#define AS_STRING_IMPL(x) #x
#define AS_STRING(x) AS_STRING_IMPL(x)
#define debug(x...) do {                                              \
    cerr << __FILE__ ":" AS_STRING(__LINE__) "  {" << #x << "} = {";  \
    debug_impl_seq(x);                                                \
    cerr << endl << flush;                                            \
  } while(0)


// https://github.com/danlark1/miniselect/

/*          Copyright Danila Kutenin, 2020-.
 * Distributed under the Boost Software License, Version 1.0.
 *    (See accompanying file LICENSE_1_0.txt or copy at
 *          https://boost.org/LICENSE_1_0.txt)
 */

namespace miniselect {
namespace floyd_rivest_detail {

enum floyd_rivest_constants {
  kQCap = 600,
};

template <class Compare>
struct CompareRefType {
  // Pass the comparator by lvalue reference. Or in debug mode, using a
  // debugging wrapper that stores a reference.
  using type = typename std::add_lvalue_reference<Compare>::type;
};

template <class Iter, class Compare,
          class DiffType = typename std::iterator_traits<Iter>::difference_type>
inline void floyd_rivest_select_loop(Iter begin, DiffType left, DiffType right,
                                     DiffType k, Compare comp) {
  while (right > left) {
    DiffType size = right - left;
    if (size > floyd_rivest_constants::kQCap) {
      DiffType n = right - left + 1;
      DiffType i = k - left + 1;

      double z = log(n);
      double s = 0.5 * exp(2 * z / 3);
      double sd = 0.5 * sqrt(z * s * (n - s) / n);
      if (i < n / 2) {
        sd *= -1.0;
      }
      DiffType new_left =
          std::max(left, static_cast<DiffType>(k - i * s / n + sd));
      DiffType new_right =
          std::min(right, static_cast<DiffType>(k + (n - i) * s / n + sd));
      floyd_rivest_select_loop<Iter, Compare, DiffType>(begin, new_left,
                                                        new_right, k, comp);
    }
    DiffType i = left;
    DiffType j = right;

    std::swap(begin[left], begin[k]);
    const bool to_swap = comp(begin[left], begin[right]);
    if (to_swap) {
      std::swap(begin[left], begin[right]);
    }
    // Make sure that non copyable types compile.
    const auto& t = to_swap ? begin[left] : begin[right];
    while (i < j) {
      std::swap(begin[i], begin[j]);
      i++;
      j--;
      while (comp(begin[i], t)) {
        i++;
      }
      while (comp(t, begin[j])) {
        j--;
      }
    }

    if (to_swap) {
      std::swap(begin[left], begin[j]);
    } else {
      j++;
      std::swap(begin[right], begin[j]);
    }

    if (j <= k) {
      left = j + 1;
    }
    if (k <= j) {
      right = j - 1;
    }
  }
}

}  // namespace floyd_rivest_detail

template <class Iter, class Compare>
inline void floyd_rivest_partial_sort(Iter begin, Iter mid, Iter end,
                                      Compare comp) {
  if (begin == end) return;
  if (begin == mid) return;
  using CompType = typename floyd_rivest_detail::CompareRefType<Compare>::type;
  using DiffType = typename std::iterator_traits<Iter>::difference_type;
  floyd_rivest_detail::floyd_rivest_select_loop<Iter, CompType>(
      begin, DiffType{0}, static_cast<DiffType>(end - begin - 1),
      static_cast<DiffType>(mid - begin - 1), comp);
  // std::sort proved to be better than other sorts because of pivoting.
  std::sort<Iter, CompType>(begin, mid, comp);
}

template <class Iter>
inline void floyd_rivest_partial_sort(Iter begin, Iter mid, Iter end) {
  typedef typename std::iterator_traits<Iter>::value_type T;
  floyd_rivest_partial_sort(begin, mid, end, std::less<T>());
}

template <class Iter, class Compare>
inline void floyd_rivest_select(Iter begin, Iter mid, Iter end, Compare comp) {
  if (mid == end) return;
  using CompType = typename floyd_rivest_detail::CompareRefType<Compare>::type;
  using DiffType = typename std::iterator_traits<Iter>::difference_type;
  floyd_rivest_detail::floyd_rivest_select_loop<Iter, CompType>(
      begin, DiffType{0}, static_cast<DiffType>(end - begin - 1),
      static_cast<DiffType>(mid - begin), comp);
}

template <class Iter>
inline void floyd_rivest_select(Iter begin, Iter mid, Iter end) {
  typedef typename std::iterator_traits<Iter>::value_type T;
  floyd_rivest_select(begin, mid, end, std::less<T>());
}

}  // namespace miniselect


const float param_coeff[5] = {0, 0.018946919744407847, 0.12848651734610936, 0.4524183454433407, 0.7440330063285268};
const float param_value0_3 = {0.6445650684010532};
const float param_value0_6 = {1.3348388828446232};
const float param_value0_9 = {2.8199923129393456};

struct union_find {
  vector<int> A;

  union_find(int n = 0) : A(n) {
    iota(all(A), 0);
  }

  int addNode() {
    A.pb(A.size());
    return A.size()-1;
  }

  int find(int a) {
    return A[a] == a ? a : A[a] = find(A[a]);
  }

  void unite(int a, int b) {
    a = find(a); b = find(b);
    A[a] = b;
  }
};

const double TL  = 9.75;
timer TM;

const int N = 30;
const int NN = N*N;
const int NNN = N*N*N;

int bsz;

inline bool bitset_get(uint64_t* bs, int ix) {
  return bs[ix/64]&(1ull<<(ix%64));
}

inline void bitset_set(uint64_t* bs, int ix) {
  bs[ix/64] |= (1ull<<(ix%64));
}

inline void bitset_reset(uint64_t* bs) {
  FOR(i,bsz) bs[i] = 0;
}

inline void bitset_copy(uint64_t* bs, uint64_t* bs2) {
  FOR(i,bsz) bs[i] = bs2[i];
}

int n,nn,nnn;
int v;
float b, sqrtb;

int A[NN];
int G[NN][4];

int D[24];
int DU[24][6];
int H[24][4];

bool is_boundary[NN];

void read(){
  cin>>n>>v>>b;
  FOR(i,n) FOR(j,n) cin>> A[i*n+j];

  nn=n*n;
  nnn=n*n*n;
  sqrtb = sqrt(b);
  bsz = (nn+63)/64;

  cerr << "[DATA] N = " << n << endl;
  cerr << "[DATA] v = " << v << endl;

  FOR(i,n) FOR(j,n) FOR(d,4) G[i*n+j][d] = -1;
  FOR(i,n) FOR(j,n) {
    if(i>0)   G[i*n+j][0] = (i-1)*n+j;
    if(i+1<n) G[i*n+j][2] = (i+1)*n+j;
    if(j>0)   G[i*n+j][1] = i*n+(j-1);
    if(j+1<n) G[i*n+j][3] = i*n+(j+1);
  }

  FOR(i,n) FOR(j,n) is_boundary[i*n+j] = i==0||i==n-1||j==0||j==n-1;

  auto getix = [&](int t, int f, int i, int j) {
    if(f > t) f -= 1;
    return t*8 + f*4 + i*2 + j;
  };

  FOR(t, 3) FOR(f, 2) FOR(i,2) FOR(j,2) {
    int rf = f >= t ? f+1 : f;
    int rl = 0; while(rl == t || rl == rf) rl++;
    int ix = getix(t,rf,i,j);
    int k = ((t==0&&rf==2)||(t==1&&rf==0)||(t==2&&rf==1))^i^j;
    D[ix] = 2*t+(i^1);

    DU[ix][0] = 2*t+i;
    DU[ix][1] = 2*t+(i^1);
    DU[ix][2] = 2*rf+j;
    DU[ix][3] = 2*rf+(j^1);
    DU[ix][4] = 2*rl+(k^1);
    DU[ix][5] = 2*rl+k;

    H[ix][0] = getix(rf,t,j,i^1);
    H[ix][2] = getix(rf,t,j^1,i);
    H[ix][1] = getix(rl,rf,k,j);
    H[ix][3] = getix(rl,rf,k^1,j);
  }
}

struct solution {
  int start, perm;
  array<int,6> dice;
  vector<int> sol;
  float score;

  void print(){
    FOR(i,6) cout << dice[DU[perm][i]] << endl;
    vector<int> cells;
    { int x = start;
      cells.eb(x);
      for(int d : sol) {
        x = G[x][d];
        cells.eb(x);
      }
    }
    cout << cells.size() << endl;
    for(int x : cells) {
      cout << x/n << " " << x%n << endl;
    }
  }
};

solution best_sol;

void test_solution(solution const& sol) {
  if(sol.score > best_sol.score) {
    debug("NEW", sol.score);
    best_sol = sol;
  }
}

struct beam_state {
  int   x, i;
  int   score;
  // int   bound;
  float heuristic;
  int   hist;
  int   start, perm;
  int   bonus;
  int   is_split;
  bool  seen_boundary;

  float value() const {
    return (bonus ? b : 1.0f) * (score + heuristic); // TODO : change ratio depending on n or v
  }

  // float upper_bound() const {
  //   return (bonus ? b : 1.0f) * (score + bound);
  // }
};

const int BEAM_MAX_WIDTH = 1'000'000;
const int LLIST_SIZE     = 3<<26;

int *llist = 0;

beam_state BEAM_A[BEAM_MAX_WIDTH];
uint64_t   BEAM_A_BS[BEAM_MAX_WIDTH * 16];

int        BEAM_I[BEAM_MAX_WIDTH * 4];
float      BEAM_H[BEAM_MAX_WIDTH * 4];

beam_state BEAM_B[BEAM_MAX_WIDTH * 4];
uint64_t   BEAM_B_BS[BEAM_MAX_WIDTH * 4 * 16];

float HEURISTIC[NN][5];
float DHEURISTIC[NN][5];
int   SCORE[NN][24];
//float BOUND[NN];

void recompute_reachable(float* oheuristic, /* int* obound, */ int* obonus,
                         float heuristic, /* int bound, */ int bonus,
                         uint64_t* bs, int start, int split_type, int x, int dx){
  static int q1[NN]; int nq1 = 0;
  static int q2[NN]; int nq2 = 0;
  static int q3[NN]; int nq3 = 0;
  int at[4] = {0,0,0,0};
  if(split_type == 4) {
    q1[nq1++] = G[x][dx^1]; at[dx^1] = 1;
    q2[nq2++] = G[x][dx];   at[dx]   = 2;
    q3[nq3++] = G[x][dx^3]; at[dx^3] = 3;
   } else if(split_type == 1){
    q1[nq1++] = G[x][dx^1]; at[dx^1] = 1;
    q2[nq2++] = G[x][dx^3]; at[dx^3] = 2;
  } else if(split_type == 2){
    q1[nq1++] = G[x][dx];   at[dx]   = at[dx^3] = 1;
    q2[nq2++] = G[x][dx^1]; at[dx^1] = 2;
  } else if(split_type == 3) {
    q1[nq1++] = G[x][dx];   at[dx]   = at[dx^1] = 1;
    q2[nq2++] = G[x][dx^3]; at[dx^3] = 2;
  }

  static uint64_t vis1[16];
  static uint64_t vis2[16];
  static uint64_t vis3[16];

  if(split_type == 4) {
    bitset_copy(vis1, bs); bitset_set(vis1, q1[0]);
    bitset_copy(vis2, bs); bitset_set(vis2, q2[0]);
    bitset_copy(vis3, bs); bitset_set(vis3, q3[0]);
    float toth1 = 0, toth2 = 0, toth3 = 0;
    // int totb1 = 0, totb2 = 0, totb3 = 0;
    int bon1 = 0, bon2 = 0, bon3 = 0;
    for(int iq = 0;; ++iq) {
      if(iq >= nq1) {
        if(iq >= nq2) {
          FOR(d,4) {
            if(at[d] == 1) {
              oheuristic[d] = toth1;
              //obound[d]     = totb1;
              obonus[d]     = bon1;
            }else if(at[d] == 2){
              oheuristic[d] = toth2;
              //obound[d]     = totb2;
              obonus[d]     = bon2;
              oheuristic[d] = heuristic-toth2;
              //obound[d]     = bound-totb2;
              obonus[d]     = bonus-bon2;
            }else if(at[d] == 3) {
              oheuristic[d] = heuristic-toth1-toth2;
              //obound[d]     = bound-totb1-totb2;
              obonus[d]     = bonus-bon1-bon2;
            }
          }
          return;
        }
        if(iq >= nq3) {
          FOR(d,4) {
            if(at[d] == 1) {
              oheuristic[d] = toth1;
              //obound[d]     = totb1;
              obonus[d]     = bon1;
            }else if(at[d] == 2){
              oheuristic[d] = heuristic-toth1-toth3;
              //obound[d]     = bound-totb1-totb3;
              obonus[d]     = bonus-bon1-bon3;
            }else if(at[d] == 3) {
              oheuristic[d] = toth3;
              //obound[d]     = totb3;
              obonus[d]     = bon3;
            }
          }
          return;
        }
      }
      if(iq >= nq2 && iq >= nq3) {
        FOR(d,4) {
          if(at[d] == 1) {
            oheuristic[d] = heuristic-toth2-toth3;
            //obound[d]     = bound-totb2-totb3;
            obonus[d]     = bonus-bon2-bon3;
          }else if(at[d] == 2){
            oheuristic[d] = toth2;
            //obound[d]     = totb2;
            obonus[d]     = bon2;
          }else if(at[d] == 3) {
            oheuristic[d] = toth3;
            //obound[d]     = totb3;
            obonus[d]     = bon3;
          }
        }
        return;
      }
      if(iq == 32) {
        FOR(d,4) {
          oheuristic[d] = -1000;
          obonus[d] = 0;
        }
        return;
      }
      if(iq < nq1){
        int y = q1[iq];
        int deg = 0;

        FOR(d,4) if(G[y][d] != -1) {
          if(G[y][d] == start) bon1 += 1;
          if(!bitset_get(bs, G[y][d])) deg += 1;
          if(!bitset_get(vis1, G[y][d])) {
            bitset_set(vis1, G[y][d]);
            q1[nq1++] = G[y][d];
          }
        }
        toth1 += HEURISTIC[y][deg];
        //totb1 += BOUND[y];
      }
      if(iq < nq2){
        int y = q2[iq];
        int deg = 0;

        FOR(d,4) if(G[y][d] != -1) {
          if(G[y][d] == start) bon2 += 1;
          if(!bitset_get(bs, G[y][d])) deg += 1;
          if(!bitset_get(vis2, G[y][d])) {
            bitset_set(vis2, G[y][d]);
            q2[nq2++] = G[y][d];
          }
        }
        toth2 += HEURISTIC[y][deg];
        //totb2 += BOUND[y];
      }
      if(iq < nq3){
        int y = q3[iq];
        int deg = 0;

        FOR(d,4) if(G[y][d] != -1) {
          if(G[y][d] == start) bon3 += 1;
          if(!bitset_get(bs, G[y][d])) deg += 1;
          if(!bitset_get(vis3, G[y][d])) {
            bitset_set(vis3, G[y][d]);
            q3[nq3++] = G[y][d];
          }
        }
        toth3 += HEURISTIC[y][deg];
        //totb3 += BOUND[y];
      }
    }
  }else{
    bitset_copy(vis1, bs); bitset_set(vis1, q1[0]);
    bitset_copy(vis2, bs); bitset_set(vis2, q2[0]);
    float toth1 = 0, toth2 = 0;
    // int totb1 = 0, totb2 = 0;
    int bon1 = 0, bon2 = 0;
    for(int iq = 0;; ++iq) {
      if(iq == nq1) {
        FOR(d,4) {
          if(at[d] == 1) {
            oheuristic[d] = toth1;
            //obound[d]     = totb1;
            obonus[d]     = bon1;
          }else if(at[d] == 2){
            oheuristic[d] = heuristic-toth1;
            //obound[d]     = bound-totb1;
            obonus[d]     = bonus-bon1;
          }
        }
        return;
      }
      if(iq == nq2) {
        FOR(d,4) {
          if(at[d] == 2) {
            oheuristic[d] = toth2;
            //obound[d]     = totb2;
            obonus[d]     = bon2;
          }else if(at[d] == 1){
            oheuristic[d] = heuristic-toth2;
            //obound[d]     = bound-totb2;
            obonus[d]     = bonus-bon2;
          }
        }
        return;
      }
      if(iq == 32) {
        FOR(d,4) {
          oheuristic[d] = -1000;
          obonus[d] = 0;
        }
        return;
      }
      { int y = q1[iq];
        int deg = 0;

        FOR(d,4) if(G[y][d] != -1) {
          if(G[y][d] == start) bon1 += 1;
          if(!bitset_get(bs, G[y][d])) deg += 1;
          if(!bitset_get(vis1, G[y][d])) {
            bitset_set(vis1, G[y][d]);
            q1[nq1++] = G[y][d];
          }
        }
        toth1 += HEURISTIC[y][deg];
        //totb1 += BOUND[y];
      }
      { int y = q2[iq];
        int deg = 0;

        FOR(d,4) if(G[y][d] != -1) {
          if(G[y][d] == start) bon2 += 1;
          if(!bitset_get(bs, G[y][d])) deg += 1;
          if(!bitset_get(vis2, G[y][d])) {
            bitset_set(vis2, G[y][d]);
            q2[nq2++] = G[y][d];
          }
        }
        toth2 += HEURISTIC[y][deg];
        //totb2 += BOUND[y];
      }

    }
  }
}

long long int niter = 0;

float solve_beam(array<int,6> const& dice, int beam_width, bool dyn, float dyn_tl) {
  int beam_max_width = min(BEAM_MAX_WIDTH, LLIST_SIZE / 4 / nn);
  beam_width = min(max(1, beam_width), beam_max_width);

  bool in_dice[10];
  FOR(i,v+1) in_dice[i] = 0;
  FOR(i,6) in_dice[dice[i]] = 1;

  int bound = 0;
  FOR(i,nn) if(A[i]>0&&in_dice[A[i]]) bound += A[i];
  if(bound * b < best_sol.score) return 0;

  float value0;
  if(v <= 6) value0 = param_value0_3 * (6-v)/(6-3) + param_value0_6 * (v-3)/(6-3);
  else value0 = param_value0_6 * (9-v)/(9-6) + param_value0_9 * (v-6)/(9-6);

  int H0[24][4];
  union_find uf(24);
  FOR(i,24) FOR(j,i) {
    bool same = true;
    FOR(k,6) if(dice[DU[i][k]] != dice[DU[j][k]]) same = false;
    if(same) uf.unite(i,j);
  }
  FOR(i,24) FOR(j,4) H0[i][j] = uf.find(H[i][j]);

  //FOR(i,nn) BOUND[i] = (A[i]>0&&in_dice[A[i]]?A[i]:0);
  FOR(j,5) FOR(i,nn) HEURISTIC[i][j] = (A[i]>0&&in_dice[A[i]]?A[i]:(A[i]<0&&in_dice[-A[i]] ? value0*0.9 : value0)) * param_coeff[j];
  FOR(i,nn) FOR(j,4) DHEURISTIC[i][j+1] = HEURISTIC[i][j] - HEURISTIC[i][j+1];

  FOR(i,nn) FOR(j,24) SCORE[i][j] = abs(A[i]) == dice[D[j]] ? A[i] : 0;

  // int total_bound = 0;
  // FOR(x,nn) total_bound += BOUND[x];

  float total_heuristic = 0;
  FOR(x,nn) {
    int deg = 0;
    FOR(d,4) if(G[x][d] != -1) {
      deg += 1;
    }
    total_heuristic += HEURISTIC[x][deg];
  }

  int na = 0;
  FOR(start, nn) FOR(j,24) if(dice[D[j]] == A[start]) {
    if(!dyn && TM.elapsed() > TL) break;
    // Initial state
    int ia = na++;
    uint64_t* bs = BEAM_A_BS + ia*bsz;
    bitset_reset(bs);
    bitset_set(bs, start);
    BEAM_A[ia].x             = start;
    BEAM_A[ia].i             = j;
    BEAM_A[ia].score         = dice[D[j]] == abs(A[start]) ? A[start] : 0;
    BEAM_A[ia].heuristic     = total_heuristic;
    //BEAM_A[ia].bound         = total_bound;
    BEAM_A[ia].hist          = 0;
    BEAM_A[ia].start         = start;
    BEAM_A[ia].perm          = j;
    BEAM_A[ia].bonus         = 0;
    BEAM_A[ia].seen_boundary = is_boundary[start];
    BEAM_A[ia].is_split      = 0;
    { int deg = 0;
      FOR(d,4) if(G[start][d] != -1) {
        deg += 1;
      }
      BEAM_A[ia].heuristic -= HEURISTIC[start][deg];
      //BEAM_A[ia].bound -= BOUND[start];
    }
    FOR(d,4) if(G[start][d] != -1) {
      BEAM_A[ia].bonus += 1;
      int deg = 0; FOR(d2,4) if(G[G[start][d]][d2] != -1) deg += 1;
      BEAM_A[ia].heuristic += DHEURISTIC[G[start][d]][deg];
    }
  }

  int llist_sz = 1;

  float best_score = 0;
  int   best_hist  = -1;
  int   best_start = 0;
  int   best_perm  = 0;

  int iter = 0;
  while(na > 0) {
    iter += 1;

    double t0 = TM.elapsed();
    // if(TM.elapsed() > TL) break;
    int nb = 0;
    FOR(ia,na) {
      niter += 1;
      beam_state const& sa = BEAM_A[ia];
      uint64_t* bsa = BEAM_A_BS + ia*bsz;

      float oheuristic[4]; int obonus[4]; // obound[4];
      FOR(d,4) {
        oheuristic[d] = sa.heuristic;
        //obound[d]     = sa.bound;
        obonus[d]     = sa.bonus;
      }
      if(sa.is_split) {
        recompute_reachable(oheuristic, obonus,
                            sa.heuristic, sa.bonus,
                            bsa, sa.start, sa.is_split, sa.x, llist[sa.hist]%4);
      }

      FOR(d,4) if(G[sa.x][d] != -1 && !bitset_get(bsa, G[sa.x][d])) {
        int ib = nb++;
        BEAM_I[ib] = ib;
        beam_state sb;
        uint64_t* bsb = BEAM_B_BS + ib*bsz;
        bitset_copy(bsb, bsa);
        sb.x = G[sa.x][d];
        sb.i = H0[sa.i][d];
        sb.score = sa.score + SCORE[sb.x][sb.i];
        sb.hist = llist_sz++;
        sb.start = sa.start;
        sb.perm  = sa.perm;
        llist[sb.hist] = 4*sa.hist+d;
        bitset_set(bsb, sb.x);
        sb.seen_boundary = sa.seen_boundary || is_boundary[sb.x];

        bool has_bonus = false;
        FOR(d2,4) if(G[sb.x][d2] == sb.start) {
          has_bonus = true;
        }

        sb.heuristic = oheuristic[d];
        //sb.bound     = obound[d];
        sb.bonus     = obonus[d];

        { int deg = 0;
          FOR(d2,4) if(G[sb.x][d2] != -1 && !bitset_get(bsb, G[sb.x][d2])) {
            deg += 1;
            int deg2 = 0; FOR(d3,4) if(G[G[sb.x][d2]][d3] != -1 && !bitset_get(bsa, G[G[sb.x][d2]][d3])) deg2 += 1;
            sb.heuristic += DHEURISTIC[G[sb.x][d2]][deg2];
          }
          sb.heuristic -= HEURISTIC[sb.x][deg];
          //sb.bound     -= BOUND[sb.x];
        }
        if(has_bonus) sb.bonus -= 1;

        bool can_go1 = G[sb.x][d^1] != -1 && !bitset_get(bsb, G[sb.x][d^1]);
        bool can_go2 = G[sb.x][d^3] != -1 && !bitset_get(bsb, G[sb.x][d^3]);
        bool can_go3 = G[sb.x][d] != -1 && !bitset_get(bsb, G[sb.x][d]);
        sb.is_split = 0;
        if(sa.seen_boundary && is_boundary[sb.x] && can_go1 && can_go2) {
          sb.is_split = 1;
        }else if(!is_boundary[sb.x] && can_go1 && can_go2 && !can_go3) {
          sb.is_split = 1;
        }else if(can_go3){
          int y = G[sb.x][d];
          bool split1 = can_go1 && bitset_get(bsb, G[y][d^1]);
          bool split2 = can_go2 && bitset_get(bsb, G[y][d^3]);
          if(split1 && split2) {
            sb.is_split = 4;
          }else if(split1) {
            sb.is_split = 2;
          }else if(split2) {
            sb.is_split = 3;
          }
        }

        BEAM_H[ib] = sb.value();

        float true_score = (has_bonus ? b : 1.0f) * sb.score;
        if(true_score > best_score) {
          best_score = true_score;
          best_hist  = sb.hist;
          best_start = sb.start;
          best_perm  = sb.perm;
        }

        BEAM_B[ib] = sb;
      }
    }

    na = nb;
    if(nb > beam_width) {
      na = beam_width;
      miniselect::floyd_rivest_select(BEAM_I, BEAM_I+na, BEAM_I+nb, [&](int i, int j){
        return BEAM_H[i] > BEAM_H[j];
      });
      for(int i = na; i > 1; i--) {
        int p = (((uint64_t)RNG.randomInt32()) * i) >> 32;
        swap(BEAM_I[i-1], BEAM_I[p]);
      }
    }
    FOR(i,na) {
      int j = BEAM_I[i];
      BEAM_A[i] = BEAM_B[j];
      bitset_copy(BEAM_A_BS+i*bsz, BEAM_B_BS+j*bsz);
    }

    if(dyn) {
      double t1 = TM.elapsed();
      double rem = dyn_tl-t1;
      if(rem > 0.01) {
        beam_width /= sqrt(max(t1-t0, 1e-6) * (nn-iter+1) / rem);
        if(beam_width < 100) beam_width = 100;
        if(beam_width > beam_max_width) beam_width = beam_max_width;
      }else{
        beam_width = 100;
      }
    }
  }

  if(dyn) debug(dice, beam_width, best_score, TM.elapsed());

  solution sol;
  sol.dice  = dice;
  sol.start = best_start;
  sol.perm  = best_perm;
  for(int h = best_hist; h != 0; h = llist[h]/4) sol.sol.eb(llist[h]%4);
  reverse(all(sol.sol));
  sol.score = best_score;
  test_solution(sol);
  return best_score;
}

void normalize_dice(array<int,6>& dice) {
  array<int,6> dice2 = dice;
  FOR(j,24){
    array<int,6> dice3;
    FOR(i,6) dice3[i] = dice[DU[j][i>=4?i^1:i]];
    dice2=max(dice2,dice3);
  }
  dice = dice2;
}

void solve(){
  set<array<int,6>> set_dice;
  vector<array<int,6>> all_dice;
  auto add_dice_perms = [&](array<int,6> dice){
    sort(all(dice));
    do {
      auto dice2 = dice;
      normalize_dice(dice2);
      if(!set_dice.count(dice2)) {
        set_dice.insert(dice2);
        all_dice.eb(dice2);
      }
    } while(next_permutation(all(dice)));
  };

  { array<int,6> dice;
    auto bt = letrec([&](auto bt, int i, int cur){
      if(cur == 6) {
        add_dice_perms(dice);
        return;
      }
      if(i == 0) return;
      do {
        dice[cur++] = i;
        bt(i-1,cur);
      }while(cur < 6);
    });
    bt(v, 0);
  }

  debug(all_dice.size());
  vector<float> dice_result(all_dice.size(), 0);

  FOR(i,all_dice.size()) {
    dice_result[i] = solve_beam(all_dice[i], 32 * NN / nn, false, 0);
  }

  vector<int> I(all_dice.size()); iota(all(I),0);
  sort(all(I), [&](int i, int j){ return dice_result[i] > dice_result[j]; });
  debug("START 1: ", TM.elapsed());

  FOR(i, min<int>(32, all_dice.size())) dice_result[I[i]] = solve_beam(all_dice[I[i]], 64 * NN / nn, false, 0);
  sort(all(I), [&](int i, int j){ return dice_result[i] > dice_result[j]; });
  debug("START 2: ", TM.elapsed());

  FOR(i, min<int>(16, all_dice.size())) dice_result[I[i]] = solve_beam(all_dice[I[i]], 128 * NN / nn, false, 0);
  sort(all(I), [&](int i, int j){ return dice_result[i] > dice_result[j]; });
  debug("START 3: ", TM.elapsed());

  // FOR(i, min<int>(8, all_dice.size())) dice_result[I[i]] = solve_beam(all_dice[I[i]], 256 * NN / nn, false, 0);
  // sort(all(I), [&](int i, int j){ return dice_result[i] > dice_result[j]; });
  // debug("START 4: ", TM.elapsed());

  const int K = 8;
  int num_dice = min(K, (int)all_dice.size());

  FOR(i,num_dice) {
    solve_beam(all_dice[I[i]], BEAM_MAX_WIDTH, true, TM.elapsed() + (TL - TM.elapsed()) / 3);
  }

  FORU(i,num_dice,(int)all_dice.size()-1) {
    if(TM.elapsed() > TL) break;
    solve_beam(all_dice[I[i]], BEAM_MAX_WIDTH, true, TL);
  }

  // FOR OPT:
  // { array<int,6> dice;
  //   FOR(i,6) dice[i] = v-(i%v);
  //   solve_beam(dice, BEAM_MAX_WIDTH, true);
  // }

  best_sol.print();
  debug(best_sol.score);
  debug(TM.elapsed());
  debug(niter);
}

int main(int argc, char** argv) {
  (void)argc; (void)argv;

  RNG.reset();
  TM.reset();
  llist = new int[LLIST_SIZE];

  read();

  // ofstream os(argv[1]);
  // os << n << endl;
  // os << v << endl;
  // os << b << endl;
  // FOR(i,n) {
  //   FOR(j,n) os << A[i*n+j] << ' ';
  //   os << endl;
  // }

  solve();

  return 0;
}
