#include <bits/stdc++.h>
#define DEBUG(x) do { std::cerr << __LINE__ << " " << __func__ <<  " " << x << std::endl; } while (0)
#define D1(x) std::cerr <<  "! " << x << std::endl;
#define D2(x,y) std::cerr <<  "! " << x << " " << y << std::endl;
#define D3(x,y,z) std::cerr <<  "! " << x << " " << y << " " << z << std::endl;
#define D4(x,y,z,a) std::cerr <<  "! " << x << " " << y << " " << z << " " << a << std::endl;
#define D5(x,y,z,a,b) std::cerr <<  "! " << x << " " << y << " " << z << " " << a << " " << b << std::endl;
#define D11(x,y,z,a,b,c,d,e,f,g,h) std::cerr <<  "! " << x << " " << y << " " << z << " " << a << " " << b << " " << c << " " << d << " " << e << " " << f << " " << g << " " << h << std::endl;

#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REPR(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) std::begin(x), std::end(x)
using namespace std;

static constexpr int INF = 1<<30;

// #define NDEBUG

static std::vector<std::string> split(const std::string &s, char delim) {
  std::vector<std::string> elems;
  std::stringstream ss(s);
  std::string item;
  while (getline(ss, item, delim)) {
    if (!item.empty()) {
      elems.push_back(item);
    }
  }
  return elems;
}

struct XorShift {
  unsigned int x, y, z, w;
  double nL[65536];
  XorShift() { init(); }
  void init()
  {
    x = 314159265; y = 358979323; z = 846264338; w = 327950288;
    double n = 1 / (double)(2 * 65536);
    for (int i = 0; i < 65536; i++) {
      nL[i] = log(((double)i / 65536) + n);
    }
  }
  inline unsigned int next() { unsigned int t=x^x<<11; x=y; y=z; z=w; return w=w^w>>19^t^t>>8; }
  inline double nextLog() { return nL[next()&0xFFFF]; }
  inline int nextInt(int m) { return (int)(next()%m); } // [0, m)
  int nextInt(int min, int max) { return min+nextInt(max-min+1); } // [min, max]
  inline double nextDouble() { return (double)next()/((long long)1<<32); } // [0, 1]
};
XorShift rng;

template <typename T>
inline void rough_shuffle(vector<T>& lv) {
    int n = lv.size();
    for (int i = n; i > 0; --i) {
        int id = rng.nextInt(i);
        swap(lv[id], lv[i-1]);
    }
}

std::size_t calc_hash(std::vector<int> const& vec) {
  std::size_t seed = vec.size();
  for(auto& i : vec) {
    seed ^= i + 0x9e3779b9 + (seed << 6) + (seed >> 2);
  }
  return seed;
}

struct Timer {
  const double LIMIT; // FIXME: 時間制限(s)
  Timer() : LIMIT(0.95) { reset(); }
  Timer(double limit) : LIMIT(limit) { reset(); }
	chrono::system_clock::time_point start;
	void reset() {
		start = chrono::system_clock::now();
	}
 
	double get() {
		auto end = chrono::system_clock::now();
		return chrono::duration_cast<chrono::milliseconds>(end - start).count()/1000.0;
	}
};

// ------------- Constants ------------
int N, V;
double B;
int grid_[30*30];
int ncount_[10]; // ncount_[i]:=数字iがgrid_に何回登場するか

vector<vector<int>> dice_ = {
{0,1,2,3,4,5},
{2,3,1,0,4,5},
{1,0,3,2,4,5},
{3,2,0,1,4,5},
{5,4,0,1,3,2},
{0,1,4,5,3,2},
{4,5,1,0,3,2},
{1,0,5,4,3,2},
{2,3,5,4,1,0},
{5,4,3,2,1,0},
{3,2,4,5,1,0},
{4,5,2,3,1,0},
{1,0,2,3,5,4},
{2,3,0,1,5,4},
{0,1,3,2,5,4},
{3,2,1,0,5,4},
{5,4,1,0,2,3},
{1,0,4,5,2,3},
{4,5,0,1,2,3},
{0,1,5,4,2,3},
{3,2,5,4,0,1},
{5,4,2,3,0,1},
{2,3,4,5,0,1},
{4,5,3,2,0,1},
};
vector<vector<int>> trans_ = {
{1,3,21,11},
{2,0,16,6},
{3,1,9,23},
{0,2,4,18},
{5,7,13,3},
{6,4,22,10},
{7,5,1,15},
{4,6,8,20},
{9,11,19,7},
{10,8,14,2},
{11,9,5,17},
{8,10,0,12},
{13,15,11,21},
{14,12,18,4},
{15,13,23,9},
{12,14,6,16},
{17,19,15,1},
{18,16,10,22},
{19,17,3,13},
{16,18,20,8},
{21,23,7,19},
{22,20,12,0},
{23,21,17,5},
{20,22,2,14},
};


// up, down, left, right
static constexpr short UP = 0;
static constexpr short DOWN = 1;
static constexpr short LEFT = 2;
static constexpr short RIGHT = 3;
int DX[4] = {0, 0, -1, 1};
int DY[4] = {-1, 1, 0, 0};
vector<vector<short>> orders_ = {
  {0,1,2,3},
  {0,1,3,2},
  {0,2,1,3},
  {0,2,3,1},
  {0,3,1,2},
  {0,3,2,1},
  {1,2,3,0},
  {1,3,2,0},
  {2,1,3,0},
  {2,3,1,0},
  {3,1,2,0},
  {3,2,1,0},
  {2,3,0,1},
  {3,2,0,1},
  {1,3,0,2},
  {3,1,0,2},
  {1,2,0,3},
  {2,1,0,3},
  {3,0,1,2},
  {2,0,1,3},
  {3,0,2,1},
  {1,0,2,3},
  {2,0,3,1},
  {1,0,3,2},
};


// TOP, BOTTOM
static constexpr short TOP = 0;
static constexpr short BOTTOM = 1;

int to_[30*30*32][4];
int dist_[30*30][30*30];
int dir_[30*30][30*30];
int i3_2_[30*30*32];
inline int y_(int id3) { return id3/(32*N); }
inline int x_(int id3) { return (id3/32)%N; }
inline int d_(int id3) { return id3%32; }
inline int i2_(int id3) { 
  return id3 >> 5;
  // assert(i3_2_[id3] == (id3 >> 5));
  // return i3_2_[id3];
} // id3 -> id2

struct Pos {
  short x = -1, y = -1, d = -1;
  Pos() {}
  Pos(int i): x(x_(i)), y(y_(i)), d(d_(i)) {}
  Pos(short x, short y): x(x), y(y) {}
  Pos(short x, short y, short d): x(x), y(y), d(d) {}
  bool eq(const Pos &other) const {
    return (other.x == x) && (other.y == y);
  }
  bool operator == (const Pos &other) const { 
    return (other.x == x) && (other.y == y) && (other.d == d);
  }
  bool operator != (const Pos &other) const { 
    return !((*this) == other);
  }
  short distance(const Pos &other) const {
    return abs(x-other.x)+abs(y-other.y);
  }
  Pos to(short dir) const {
    // assert(d != -1);
    return Pos(x+DX[dir],y+DY[dir], trans_[d][dir]);
  }

  int id3() const { return y*N*32+x*32+d; }
  int id2() const { return y*N+x; }

  friend std::ostream& operator<<(std::ostream& os, const Pos &p) {
    os << "(" << p.x << "," << p.y << "," << p.d << ")";
    return os;
  }
};

int getDir(const Pos &cur, const Pos &nex) {
  // cur -> nexの方向を返す
  if (cur.x > nex.x) return LEFT;
  if (cur.x < nex.x) return RIGHT;
  if (cur.y > nex.y) return UP;
  if (cur.y < nex.y) return DOWN;
  return -1;
}

bool outside(const Pos &p) {
  if (p.x < 0 || p.x >= N) return true;
  if (p.y < 0 || p.y >= N) return true;
  return false;
}
// update(), calcScore(), revert(), write()を実装する
// using grid_t = vector<int>;
using grid_t = int[900];

static constexpr int MAX_DEPTH = 13;
vector<char> dir2c = {'A', 'v', '<', '>'};
void show(const grid_t &grid) {
  REP(y,N) {
    REP(x,N) {
      int cur = Pos(x,y).id2();
      int nex = grid[cur];
      if (nex == -1) {
        cerr << '.';
        continue;
      }
      int dir = dir_[cur][i2_(nex)];
      cerr << dir2c[dir];
    }
    cerr << '\n';
  }
  cerr << '\n';
}

struct State {
  vector<int> dice;
  // Pos start, goal;
  int start, goalI2;  // id2
  grid_t grid;
  int score = -INF;
  // backup
  vector<int> bpos;
  int bscore;
  int blen;
  int bsrc, btarget;
  int bid;
  int btype;
  int bdid, bv;
  int bstart, bgoal, bgridgoal, bgridstart;
  State(): dice(6), bpos(MAX_DEPTH+2) {
    REP(i,N*N) grid[i] = -1;
  }

  int update5() {
    // startを前ににずらす
    btype = 5;
    bscore = score;
    Pos sp(start);
    Pos gp(goalI2%N, goalI2/N);
    bstart = start;
    bgoal = goalI2;
    goalI2 = sp.id2();
    bgridstart = grid[goalI2];
    start = grid[goalI2];
    // cerr << Pos(start) << bp << endl;

    int goal2start = dir_[goalI2][i2_(start)];
    grid[goalI2] = to_[grid[bgoal]][goal2start];

    int diff = 0;
    // 変更前のgoal地点のscore
    int dbef = dice[dice_[d_(bstart)][BOTTOM]];
    int v = grid_[goalI2];
    if (abs(v) == dbef) diff -= v;
    int daft = dice[dice_[d_(grid[bgoal])][BOTTOM]];
    if (abs(v) == daft) diff += v;
    // cerr << v << dbef << daft << endl;
    
    score += diff;
    return diff;
  }

  int update4() {
    // startをgoal方向ににずらす
    btype = 4;
    bscore = score;
    Pos gp(goalI2%N, goalI2/N);
    Pos sp(start);
    Pos bp;
    int goal;
    REP(dir,4) {
      int bx = gp.x+DX[dir];
      int by = gp.y+DY[dir];
      bp = Pos(bx,by);
      if (outside(bp)) continue;
      int bid = bp.id2();
      if (grid[bid] != -1 && i2_(grid[bid]) == goalI2) {
        // cerr << bp << gp << endl;
        goal = grid[bid];
        break;
      }
    }
    bstart = start;
    bgoal = goalI2;
    int id;
    bool ok = false;
    int goal2start = dir_[gp.id2()][sp.id2()];
    REP(d,24) {
      id = Pos(gp.x,gp.y,d).id3();
      if (to_[id][goal2start] == start) { ok = true; break; }
    }
    // cerr << Pos(start) << bp << endl;
    goalI2 = bp.id2();

    int start2goal = dir_[sp.id2()][gp.id2()];
    Pos nsp = sp.to(start2goal);
    start = nsp.id3();
    bgridgoal = grid[bgoal];
    grid[bgoal] = bstart;

    int diff = 0;
    // 変更前のgoal地点のscore
    int dbef = dice[dice_[d_(goal)][BOTTOM]];
    int v = grid_[i2_(goal)];
    if (abs(v) == dbef) diff -= v;
    int daft = dice[dice_[d_(start)][BOTTOM]];
    if (abs(v) == daft) diff += v;
    
    assert(ok);

    // D4(bstart, start, bgoal, goalI2);
    // score = calcScore();
    // assert(diff == score-bscore);
    score += diff;
    return diff;
  }

  int update3() {
    // diceの数字交換
    btype = 3;
    int did = rng.nextInt(5);
    bscore = score;
    bdid = did;
    if (dice[did] == dice[did+1]) return -INF;
    swap(dice[did], dice[did+1]);
    score = calcScore();
    // return (score-bscore)/(N*N*0.8);
    return score-bscore;
  }

  int update6() {
    // diceの数字変更。見込みのあるもののみ選ぶ
    btype = 2;
    int did = rng.nextInt(6);
    bv = dice[did];
    int vmin = max(1, V-5);
    int v = rng.nextInt(vmin, V-1);
    if (v >= bv) v += 1;
    bscore = score;
    bdid = did;
    // calc score
    vector<int> used(10);
    int used2 = 0; // dice[did]が使われた回数
    {
      int cur = start;
      // show(grid);
      while (true) {
        int cur_did = dice_[d_(cur)][BOTTOM];
        int d = dice[cur_did];
        int v = grid_[i2_(cur)];
        // cerr << Pos(cur) << d << v << endl;
        // cerr << cur;
        // REP(i,6) { cerr << dice[dice_[cur.d][i]]; }
        // cerr << " " << d << v << endl;
        if (abs(v) == d)  {
          if (cur_did == did) used2++;
          used[d]++;
        }
        int nex = grid[i2_(cur)];
        assert(nex != -1);
        if (i2_(nex) == i2_(start)) break;
        cur = nex;
      }
    }
    int bestV = -1;
    int bestScore = -INF;
    int remain = ncount_[bv]-used[bv];
    REP3(v,1,V+1) {
      if (v == bv) continue;
      int curRemain = ncount_[v]-used[v];
      int curScore = curRemain*v-remain*bv;
      if (curScore > bestScore) {
        bestScore = curScore;
        bestV = v;
      }
    }
    assert(bestV != -1);
    // return (score-bscore)/(N*N*0.8);
    // return score-bscore;
    dice[did] = bestV;
    score = calcScore();
    // if (bestScore >= 0) {
    //   cerr << score-bscore << " " << bestScore << " " << bv << " " << v << endl;
    // }
    return score-bscore + 0.5*bestScore;
  }

  int update2() {
    // diceの数字変更
    btype = 2;
    int did = rng.nextInt(6);
    int vmin = max(1, V-3);
    int v = rng.nextInt(vmin, V);
    while (v == dice[did]) {
      v = rng.nextInt(vmin, V);
    }
    bscore = score;
    bdid = did;
    bv = dice[did];
    dice[did] = v;
    score = calcScore();
    // return (score-bscore)/(N*N*0.8);
    return score-bscore;
  }

  int clear(int src, int *len, int *target) {
    // clearすることにより減るスコアを返す
    int ret = 0;
    int cur = src;
    REP(i,*len) {
      int nex = grid[i2_(cur)];
      // cerr << Pos(cur) << Pos(nex) << endl;
      assert(nex != -1);
      // cerr << Pos(cur) << Pos(nex) << i << " "<<*len <<endl;
      bpos[i+1] = -1;
      bpos[i] = nex;
      *target = nex;
      int d = dice[dice_[d_(cur)][BOTTOM]];
      int v = grid_[i2_(cur)];
      if (abs(v) == d) ret -= v;
      // cerr << "[cl]" << Pos(cur) << Pos(nex) << endl;
      grid[i2_(cur)] = -1;
      // cerr << i << cur << nex << endl;
      if (i2_(nex) == i2_(start)) {
        // cerr << Pos(cur) << Pos(*target) << Pos(start) << endl;
        assert(i2_(*target) == i2_(start));
        *len = i+1;
        break;
      }
      cur = nex;
    }
    return ret;
  }

  double update1() { 
    btype = 1;
    int len = rng.nextInt(3,MAX_DEPTH-2);
    bgoal = goalI2;
    bstart = start;
    if (grid[goalI2] == start) {
      int gid = rng.nextInt(N*N);
      while(grid[gid] == -1) {
        gid = rng.nextInt(N*N);
      }
      goalI2 = gid;
      start = grid[goalI2];
    }
    int id = rng.nextInt(N*N);
    while(grid[id] == -1 || id == goalI2) {
      id = rng.nextInt(N*N);
    }
    bid = id;
    int cur = grid[id];
    bsrc = cur;
    int target;
    int diff1 = clear(cur, &len, &target);
    // cerr << Pos(x,y) << "->" << Pos(x_(cur), y_(cur)) << "->" << Pos(x_(target), y_(target)) << endl;
    blen = len;
    bscore = score;
    btarget = target;
    // show(grid);
    // cerr << bsrc << target << endl;
    int len2 = dfs(-1, bsrc, target, i2_(target), 0);
    if (len2 == -1) {
      return -INF;
    }
    assert(i2_(grid[goalI2]) == i2_(start));
    // show(grid);
    int diff2 = calcDiffScore(bsrc, target);
    score += diff1+diff2;

    // show(grid);
    // score = calcScore();
    // cerr << score-bscore << " " << diff1+diff2 << " " << diff1 << " " << diff2 << endl;
    // assert(score-bscore == diff1+diff2);

    assert(len > 0 && len2 > 0);
    // double sc = 1.0*diff1/len+1.0*diff2/len2;
    // if (sc > 0 && len < 4) {
    //   D5(diff1, len, diff2, len2, sc);
    // }
    // cerr << (grid[goalI2] == start) << endl;
    return diff1+diff2+(len-len2)*0.5;
  }
  double update(double progress) { 
    int p = rng.nextInt(N*100);
    if (p <= 5) return update6();
    if (p <= 10) return update3();
    if (grid[goalI2] != start) {
      if (p <= 110) return update4();
      if (p <= 220) return update5();
    }
    return update1();
  }

  bool empty(int p) const {
    return grid[i2_(p)] == -1;
  }

  short dfs(int befI2, int cur, int target, int targetI2, int depth) {
    if (!empty(cur)) {
      if (cur == target) {
        if (targetI2 == i2_(start)) {
          goalI2 = befI2;
        }
        // Pos fr = src;
        // while(true) {
        //   Pos nex = grid[fr.y][fr.x];
        //   assert(nex.x != -1);
        //   cerr << nex;
        //   if (nex == target) break;
        //   fr = nex;
        // }
        // cerr << endl;
        return depth;
      }
      else if (targetI2 == i2_(start) && i2_(cur) == i2_(start)) {
        goalI2 = befI2;
        return depth;
      }
      return -1;
    }
    // targetにたどり着けない場合は枝刈り
    if (dist_[i2_(cur)][targetI2] > MAX_DEPTH-depth) return -1;

    int oid = rng.nextInt(24);
    for (short dir: orders_[oid]) {
      int nex = to_[cur][dir];
      if (nex == -1) continue; // outside
      // assert(grid[i2_(cur)] == -1);
      grid[i2_(cur)] = nex;
      short ret = dfs(i2_(cur), nex, target, targetI2, depth+1);
      if (ret != -1) return ret;
      grid[i2_(cur)] = -1;
    }
    return -1;
  }

  int size() {
    // length of current loop
    int len = 0;
    int cur = start;
    while (true) {
      ++len;
      int nex = grid[i2_(cur)];
      assert(nex != -1);
      if (i2_(nex) == i2_(start)) break;
      cur = nex;
    }
    return len; 
  }

  int calcDiffScore(int src, int target) {
    int ret = 0;
    int cur = src;
    while (true) {
      int d = dice[dice_[d_(cur)][BOTTOM]];
      int v = grid_[i2_(cur)];
      // REP(i,6) { cerr << dice[dice_[cur.d][i]]; }
      if (abs(v) == d) ret += v;
      int nex = grid[i2_(cur)];
      assert(nex != -1);
      // cerr << "[ad]" <<  cur << nex << d << v << endl;
      if (i2_(nex) == i2_(target)) break;
      cur = nex;
    }
    return ret;
  }

  int calcScore() { 
    int ret = 0;
    int cur = start;
    // show(grid);
    while (true) {
      int d = dice[dice_[d_(cur)][BOTTOM]];
      int v = grid_[i2_(cur)];
      // cerr << Pos(cur) << d << v << endl;
      // cerr << cur;
      // REP(i,6) { cerr << dice[dice_[cur.d][i]]; }
      // cerr << " " << d << v << endl;
      if (abs(v) == d) ret += v;
      int nex = grid[i2_(cur)];
      assert(nex != -1);
      if (i2_(nex) == i2_(start)) break;
      cur = nex;
    }
    // cerr << endl;
    return ret;
  }

  void revert() {
    if (btype == 1) revert1();
    else if (btype == 2) revert2();
    else if (btype == 3) revert3();
    else if (btype == 4) revert4();
    else if (btype == 5) revert5();
  }

  void revert5() {
    score = bscore;
    start = bstart;
    goalI2 = bgoal;
    grid[i2_(start)] = bgridstart;
  }

  void revert4() {
    score = bscore;
    start = bstart;
    goalI2 = bgoal;
    grid[goalI2] = bgridgoal;
  }

  void revert3() {
    score = bscore;
    swap(dice[bdid], dice[bdid+1]);
  }

  void revert2() {
    score = bscore;
    dice[bdid] = bv;
  }

  void revert1() {
    // show(grid);
    int cur = bsrc;
    while (true) {
      int nex = grid[i2_(cur)];
      grid[i2_(cur)] = -1;
      assert(nex != -1);
      if (i2_(nex) == i2_(btarget)) break;
      cur = nex;
    }
    cur = bsrc;
    assert(bpos[blen] == -1);
    REP(i,blen) {
      // cerr << i << cur << bpos[i] << endl;
      assert(bpos[i] != -1);
      grid[i2_(cur)] = bpos[i];
      cur = bpos[i];
    }
    goalI2 = bgoal;
    start = bstart;
    score = bscore;
    assert(i2_(grid[goalI2]) == i2_(start));
    // show(grid);
  }

  void write() {
    REP(i,6) cout << dice[dice_[d_(start)][i]] << '\n';

    int n = size();
    cout << size() << '\n';
    int cur = start;
    REP(i,n) {
      cout << y_(cur) << " " << x_(cur) << '\n';
      int nex = grid[i2_(cur)];
      // if (i == n-1) assert(nex.eq(start));
      // else assert(!nex.eq(start));
      cur = nex;
    }
  } // write current solution
};

void initState(State &s, vector<int> dice) {
  int v = V;
  s.dice = dice;
  s.start = Pos(0,0,0).id3();
  int cur = s.start;
  for (int dir: {RIGHT, DOWN, LEFT, UP}) {
    REP(i,N-N%2-1) {
      int nex = to_[cur][dir];
      Pos p(x_(cur),y_(cur));
      Pos np(x_(nex),y_(nex));
      if (nex == -1) break; // outside
      s.grid[i2_(cur)] = nex;
      s.goalI2 = i2_(cur);
      if (s.grid[i2_(nex)] != -1) break; // not empty
      cur = nex;
    }
  }
  assert(s.grid[s.goalI2] != s.start);
  s.score = s.calcScore();
}

struct SASolver {
  double startTemp = 3;
  double endTemp = 0.001;
  // Timer timer = Timer(2.85);
  Timer timer = Timer(9.55);
  // Timer timer = Timer(29.55);
  State best;
  SASolver() { init(); }
  SASolver(double st, double et): startTemp(st), endTemp(et) { init(); }
  SASolver(double st, double et, double limit): startTemp(st), endTemp(et), timer(limit) { init(); }
  void init() {} // 初期化処理をここに書く

  void solve(State &state) {
    double t;
    best = state;
    int counter = 0;
    vector<int> total(6);
    vector<int> ac(6);
    // best.write();
    while ((t = timer.get()) < timer.LIMIT) // 焼きなまし終了時刻までループ
    {
      double T = startTemp + (endTemp - startTemp) * t / timer.LIMIT;
      double progress = t/timer.LIMIT;
      // assert(0 <= progress && progress <= 1);
      for (int i = 0; i < 100; ++i) { // 時間計算を間引く
        double diff = state.update(progress);
        total[state.btype]++;
        if (diff <= -INF+0.1) {
          state.revert();
          continue;
        }

        // 最初t=0のときは、スコアが良くなろうが悪くなろうが、常に次状態を使用
        // 最後t=timer.LIMITのときは、スコアが改善したときのみ、次状態を使用
        // スコアが良くなった or 悪くなっても強制遷移
        double tr = T*rng.nextLog();
        // cerr << t << " " << T << " " << tr << " " << diff << endl;
        if (diff >= tr)
        {
          ac[state.btype]++;
          if (best.score < state.score) {
            best = state;
            // cerr << "time = " << t << ", counter = " << counter << ", score = " << best.score << '\n';
            // best.write();
          }
        }
        else { state.revert(); }
        ++counter;
      }
    }
    cerr << "counter = " << counter << ", score = " << best.score << " " << best.calcScore() << endl;
    REP3(i,1,6) {
      if (total[i] == 0) continue;
      cerr << i << ":" << 1.0*ac[i]/total[i] << "(" << ac[i] << "/" << total[i] << ")" << endl;
    }
  }
};

struct Solver {
    Solver() {
        reset();
    }
    void reset() {
    }

    void solve() {
        State state; // 開始状態
        initState(state,{V,V-1,V,V-2,V-1,max(2,V-3)});
        SASolver s;
        s.solve(state);
        s.best.write();
        // show(s.best.grid);
        int score = s.best.calcScore();
        cerr << "score=" << score << " " << score*B << endl;
    }

    void readInput() {
      cin >> N >> V >> B;

      REP(r,N) REP(c,N) {
        cin >> grid_[r*N+c];
      }
      REP(i,10) ncount_[i] = 0;
      REP(r,N) REP(c,N) {
        int did = grid_[r*N+c]; 
        if (did < 0) continue;
        ncount_[did]++;
      }
      // REP(i,10) cerr << i << " " << ncount_[i] << endl;
    }

};

void initPos() {
  REP(i,30*30*32) REP(dir,4) to_[i][dir] = -1;
  REP(i,30*30) REP(j,30*30) dist_[i][j] = INF;
  REP(i,30*30) REP(j,30*30) dir_[i][j] = -1;
  REP(y,N) REP(x,N) {
    Pos p(x,y,0);
    int id2 = p.id2();
    REP(d,24) {
      p.d = d;
      int id3 = p.id3();
      assert(y_(id3) == y);
      assert(x_(id3) == x);
      assert(d_(id3) == d);
      i3_2_[id3] = (id3 >> 5);
      REP(dir,4) {
        Pos np = p.to(dir);
        if (outside(np)) continue;
        to_[id3][dir] = np.id3();
      }
    }
    REP(ny,N) REP(nx,N) {
      Pos np(nx,ny,0);
      int nid2 = np.id2();
      dist_[id2][nid2] = p.distance(np);
      dir_[id2][nid2] = getDir(p,np);
    }
  }
}

int main() 
{
  Solver solver;
  solver.readInput();
  initPos();
  solver.solve();

}