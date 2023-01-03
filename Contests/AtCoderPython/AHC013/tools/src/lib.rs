#![allow(non_snake_case, unused_macros)]

use std::collections::{HashMap, HashSet};

use proconio::{input, marker::*};
use rand::prelude::*;
use svg::node::{
    element::{Line, Rectangle, Text as TextElement, Title},
    Text, Value,
};

#[cfg(target_arch = "wasm32")]
use wasm_bindgen::prelude::*;

#[derive(Clone, Debug)]
pub struct UnionFind {
    par: Vec<usize>,
    size: Vec<usize>,
}

impl UnionFind {
    pub fn new(n: usize) -> Self {
        UnionFind {
            par: (0..n).into_iter().collect(),
            size: vec![1; n],
        }
    }

    pub fn find(&mut self, x: usize) -> usize {
        if self.par[x] == x {
            x
        } else {
            self.par[x] = self.find(self.par[x]);
            self.par[x]
        }
    }

    pub fn unite(&mut self, x: usize, y: usize) {
        let mut x = self.find(x);
        let mut y = self.find(y);
        if self.size[x] < self.size[y] {
            ::std::mem::swap(&mut x, &mut y);
        }
        if x != y {
            self.size[x] += self.size[y];
            self.par[y] = x;
        }
    }

    pub fn same(&mut self, x: usize, y: usize) -> bool {
        self.find(x) == self.find(y)
    }
}

#[derive(Clone, Debug)]
pub struct Input {
    pub n: usize,
    pub k: usize,
    pub grid: Vec<Vec<usize>>,
}

impl std::fmt::Display for Input {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "{} {}", self.n, self.k)?;
        for i in 0..self.n {
            for j in 0..self.n {
                write!(f, "{}", self.grid[i][j])?;
            }
            writeln!(f)?;
        }
        Ok(())
    }
}

pub fn parse_input(f: &str) -> Input {
    let f = proconio::source::once::OnceSource::from(f);
    input! {
        from f,
        n: usize,
        k: usize,
        grid: [Chars; n]
    }
    let grid = grid
        .iter()
        .map(|row| {
            row.iter()
                .map(|&c| c.to_string().parse::<usize>().unwrap())
                .collect()
        })
        .collect();
    Input { n, k, grid }
}

#[derive(Clone, Debug)]
pub struct Output {
    pub moves: Vec<(usize, usize, usize, usize)>,
    pub connects: Vec<(usize, usize, usize, usize)>,
}

fn read<T: Copy + PartialOrd + std::fmt::Display + std::str::FromStr>(
    token: Option<&str>,
    lb: T,
    ub: T,
) -> Result<T, String> {
    if let Some(v) = token {
        if let Ok(v) = v.parse::<T>() {
            if v < lb || ub < v {
                Err(format!("Out of range: {}", v))
            } else {
                Ok(v)
            }
        } else {
            Err(format!("Parse error: {}", v))
        }
    } else {
        Err(format!("Unexpected EOF"))
    }
}

pub fn parse_multi_output(input: &Input, f: &str) -> Result<Vec<Output>, String> {
    let mut outputs = vec![];
    let mut tokens = f.split_whitespace();
    while let Some(num_moves) = tokens.next() {
        let mut moves = vec![];
        let mut connects = vec![];
        let num_moves = read(Some(num_moves), 0, 100 * input.k)?;
        for _ in 0..num_moves {
            let r0 = read(tokens.next(), 0, input.n - 1)?;
            let c0 = read(tokens.next(), 0, input.n - 1)?;
            let r1 = read(tokens.next(), 0, input.n - 1)?;
            let c1 = read(tokens.next(), 0, input.n - 1)?;
            moves.push((r0, c0, r1, c1));
        }

        let num_connects = read(tokens.next(), 0, 100 * input.k - num_moves)?;
        for _ in 0..num_connects {
            let r0 = read(tokens.next(), 0, input.n - 1)?;
            let c0 = read(tokens.next(), 0, input.n - 1)?;
            let r1 = read(tokens.next(), 0, input.n - 1)?;
            let c1 = read(tokens.next(), 0, input.n - 1)?;
            connects.push((r0, c0, r1, c1));
        }
        outputs.push(Output { moves, connects });
    }

    Ok(outputs)
}

pub fn parse_output(input: &Input, f: &str) -> Result<Output, String> {
    let mut output = parse_multi_output(input, f)?;
    if output.is_empty() {
        return Err(format!("no output"));
    }
    Ok(output.remove(0))
}

pub struct Outcome {
    pub n: usize,
    pub grid: Vec<Vec<usize>>,
    pub cables: Vec<(usize, usize, usize, usize)>,
    pub cid: Vec<Vec<usize>>,
}

pub struct Sim {
    n: usize,
    k: usize,
    grid: Vec<Vec<usize>>,
    cables: Vec<(usize, usize, usize, usize)>,
    cable_set: HashSet<(usize, usize, usize, usize)>,
    moves: usize,
    connects: usize,
}

impl Sim {
    pub fn new(input: &Input) -> Self {
        Sim {
            n: input.n,
            k: input.k,
            grid: input.grid.clone(),
            cables: Vec::new(),
            cable_set: HashSet::new(),
            moves: 0,
            connects: 0,
        }
    }

    fn check_inside(&self, r: usize, c: usize, marker: &str) -> Result<(), String> {
        if r >= self.n || c >= self.n {
            Err(format!("invalid coordinate: ({}, {}) ({})", r, c, marker))
        } else {
            Ok(())
        }
    }

    pub fn apply_move(&mut self, r0: usize, c0: usize, r1: usize, c1: usize) -> Result<(), String> {
        let marker = format!("move {}", self.moves);
        self.check_inside(r0, c0, &marker)?;
        self.check_inside(r1, c1, &marker)?;
        if r0.abs_diff(r1) + c0.abs_diff(c1) != 1 {
            return Err(format!(
                "illegal move: ({}, {}) -> ({}, {}) ({})",
                r0, c0, r1, c1, marker
            ));
        }
        if self.grid[r0][c0] == 0 {
            return Err(format!(
                "illegal move: ({}, {}) is empty ({})",
                r0, c0, marker
            ));
        }
        if self.grid[r1][c1] != 0 {
            return Err(format!(
                "illegal move: ({}, {}) is not empty ({})",
                r1, c1, marker
            ));
        }
        self.grid[r1][c1] = self.grid[r0][c0];
        self.grid[r0][c0] = 0;
        self.moves += 1;
        Ok(())
    }

    fn check_identical_cable(
        &mut self,
        r0: usize,
        c0: usize,
        r1: usize,
        c1: usize,
        marker: &str,
    ) -> Result<(), String> {
        if self.cable_set.contains(&(r0, c0, r1, c1)) || self.cable_set.contains(&(r1, c1, r0, c0))
        {
            Err(format!(
                "illegal connect: identical cable exists ({}, {}) - ({}, {}) ({})",
                r0, c0, r1, c1, marker
            ))
        } else {
            self.cable_set.insert((r0, c0, r1, c1));
            self.cable_set.insert((r1, c1, r0, c0));
            Ok(())
        }
    }

    pub fn apply_connect(
        &mut self,
        r0: usize,
        c0: usize,
        r1: usize,
        c1: usize,
    ) -> Result<(), String> {
        let marker = format!("connect {}", self.connects);
        self.check_inside(r0, c0, &marker)?;
        self.check_inside(r1, c1, &marker)?;
        self.check_identical_cable(r0, c0, r1, c1, &marker)?;
        if r0 == r1 && c0 == c1 {
            return Err(format!(
                "illegal connect: same coordinates ({}, {}) - ({}, {}) ({})",
                r0, c0, r1, c1, marker
            ));
        }
        if r0 != r1 && c0 != c1 {
            return Err(format!(
                "illegal connect: not axis-aligned ({}, {}) - ({}, {}) ({})",
                r0, c0, r1, c1, marker
            ));
        }
        if self.grid[r0][c0] == 0 || self.grid[r0][c0] == !0 {
            return Err(format!(
                "illegal connect: computer does not exist on ({}, {}) ({})",
                r0, c0, marker
            ));
        }
        if self.grid[r1][c1] == 0 || self.grid[r1][c1] == !0 {
            return Err(format!(
                "illegal connect: computer does not exist on ({}, {}) ({})",
                r1, c1, marker
            ));
        }

        let (cr0, cr1) = if r0 == r1 {
            (r0, r1)
        } else {
            (r0.min(r1) + 1, r0.max(r1) - 1)
        };
        let (cc0, cc1) = if c0 == c1 {
            (c0, c1)
        } else {
            (c0.min(c1) + 1, c0.max(c1) - 1)
        };

        for r in cr0..=cr1 {
            for c in cc0..=cc1 {
                if self.grid[r][c] == !0 {
                    return Err(format!(
                        "illegal connect: cables cross at ({}, {}) ({})",
                        r, c, marker
                    ));
                }
                if self.grid[r][c] != 0 {
                    return Err(format!(
                        "illegal connect: computer exists on ({}, {}) ({})",
                        r, c, marker
                    ));
                }
            }
        }

        for r in cr0..=cr1 {
            for c in cc0..=cc1 {
                self.grid[r][c] = !0;
            }
        }
        self.cables.push((r0, c0, r1, c1));
        self.connects += 1;
        Ok(())
    }

    pub fn compute_score(&self) -> (i32, String, Outcome) {
        let mut uf = UnionFind::new(self.n * self.n);
        self.cables
            .iter()
            .for_each(|(r0, c0, r1, c1)| uf.unite(r0 * self.n + c0, r1 * self.n + c1));

        let mut pos = Vec::new();
        for r in 0..self.n {
            for c in 0..self.n {
                if self.grid[r][c] != !0 && self.grid[r][c] != 0 {
                    pos.push((r, c));
                }
            }
        }

        let computers = pos.len();
        let mut score = 0;
        for i in 0..computers {
            let (ri, ci) = pos[i];
            for j in i + 1..computers {
                let (rj, cj) = pos[j];
                if uf.same(ri * self.n + ci, rj * self.n + cj) {
                    if self.grid[ri][ci] == self.grid[rj][cj] {
                        score += 1;
                    } else {
                        score -= 1;
                    }
                }
            }
        }

        let mut component_ids = HashMap::new();
        let mut cid = vec![vec![!0; self.n]; self.n];
        for &(r, c) in pos.iter() {
            let p = uf.find(r * self.n + c);
            let sz = component_ids.len();
            let id = component_ids.entry(p).or_insert(sz);
            cid[r][c] = *id;
        }

        for &(r0, c0, r1, c1) in self.cables.iter() {
            let id = cid[r0][c0];
            for r in r0.min(r1)..=r0.max(r1) {
                for c in c0.min(c1)..=c0.max(c1) {
                    cid[r][c] = id;
                }
            }
        }

        let outcome = Outcome {
            n: self.n,
            grid: self.grid.clone(),
            cables: self.cables.clone(),
            cid,
        };
        if self.moves + self.connects > 100 * self.k {
            return (0, format!("too many moves"), outcome);
        }
        (score, String::new(), outcome)
    }
}

pub fn compute_score(input: &Input, output: &Output) -> (i32, String, Outcome) {
    let mut sim = Sim::new(input);
    for &(r0, c0, r1, c1) in output.moves.iter() {
        if let Err(err) = sim.apply_move(r0, c0, r1, c1) {
            return (0, err, sim.compute_score().2);
        }
    }
    for &(r0, c0, r1, c1) in output.connects.iter() {
        if let Err(err) = sim.apply_connect(r0, c0, r1, c1) {
            return (0, err, sim.compute_score().2);
        }
    }
    sim.compute_score()
}

const COUNT: usize = 100;
const MIN_K: usize = 2;
const MAX_K: usize = 5;
const MIN_N: [usize; 6] = [0, 0, 15, 18, 21, 24];
const MAX_N: [usize; 6] = [0, 0, 39, 42, 45, 48];

pub fn gen(seed: u64, k: Option<usize>, n: Option<usize>) -> Input {
    let mut rng = rand_chacha::ChaCha20Rng::seed_from_u64(seed);
    let k_range = (MAX_K - MIN_K + 1) as u64;
    let k = k.unwrap_or((MIN_K as u64 + seed % k_range) as usize);
    let n = n.unwrap_or(rng.gen_range(MIN_N[k] as u64..=MAX_N[k] as u64) as usize);

    let mut pos = Vec::new();
    for i in 0..n {
        for j in 0..n {
            pos.push((i, j));
        }
    }
    pos.shuffle(&mut rng);

    let mut grid = vec![vec![0; n]; n];
    for ci in 0..k {
        for i in 0..COUNT {
            let (r, c) = pos[ci * COUNT + i];
            grid[r][c] = ci + 1;
        }
    }

    Input { n, k, grid }
}

#[cfg(target_arch = "wasm32")]
#[wasm_bindgen]
pub fn generate(seed: u64, k: usize, n: usize) -> String {
    let k = if MIN_K <= k && k <= MAX_K {
        Some(k)
    } else {
        None
    };
    let n = if let Some(k_spec) = k {
        if n >= MIN_N[k_spec] {
            Some(n)
        } else {
            None
        }
    } else {
        None
    };
    gen(seed, k, n).to_string()
}

fn rect<V: Into<Value>>(
    x: V,
    y: V,
    w: V,
    h: V,
    fill: &str,
    opacity: f64,
    title: Option<&str>,
) -> Rectangle {
    let rect = Rectangle::new()
        .set("x", x)
        .set("y", y)
        .set("width", w)
        .set("height", h)
        .set("fill", fill)
        .set("fill-opacity", opacity);
    if let Some(tooltip) = title {
        rect.add(Title::new().add(Text::new(tooltip)))
    } else {
        rect
    }
}

fn line<V: Into<Value>>(x1: V, y1: V, x2: V, y2: V, stroke: &str, stroke_width: usize) -> Line {
    Line::new()
        .set("x1", x1)
        .set("y1", y1)
        .set("x2", x2)
        .set("y2", y2)
        .set("stroke", stroke)
        .set("stroke-width", stroke_width)
}

fn most_frequent(v: &[usize]) -> usize {
    let mut freq = HashMap::new();
    for &x in v.iter() {
        let e = freq.entry(x).or_insert(0);
        *e += 1;
    }
    freq.into_iter().max_by_key(|&(_, count)| count).unwrap().0
}

pub fn vis(input: &Input, output: &Output) -> (i32, String, String) {
    const W: usize = 24;
    const BG_PALETTE: &[&str] = &["#CC0A0A", "#3A0BD6", "#00BFB6", "#73D60B", "#CCBA0C"];
    let (score, error, outcome) = compute_score(input, output);
    let mut doc = svg::Document::new()
        .set("id", "vis")
        .set("viewBox", (-5, -5, W * input.n + 10, W * input.n + 10))
        .set("width", W * input.n + 10)
        .set("height", W * input.n + 10);

    doc = doc.add(rect(
        -5,
        -5,
        (W * input.n + 10) as i32,
        (W * input.n + 10) as i32,
        "white",
        1.0,
        None,
    ));

    let (_c_size, c_repr, c_count, c_perf) = {
        let mut computers_in_cluster = HashMap::new();
        for i in 0..input.n {
            for j in 0..input.n {
                if outcome.cid[i][j] != !0 && outcome.grid[i][j] != !0 {
                    let e = computers_in_cluster
                        .entry(outcome.cid[i][j])
                        .or_insert(vec![]);
                    e.push(outcome.grid[i][j]);
                }
            }
        }
        let mut size = vec![0; computers_in_cluster.len()];
        let mut repr = vec![0; computers_in_cluster.len()];
        let mut count = vec![format!(""); computers_in_cluster.len()];
        let mut perf = vec![0; computers_in_cluster.len()];
        for (cid, computers) in computers_in_cluster.into_iter() {
            size[cid] = computers.len();
            repr[cid] = most_frequent(&computers);
            let mut cnt = vec![0; input.k];
            for &c in computers.iter() {
                cnt[c - 1] += 1;
            }
            count[cid] = format!(
                "{}",
                cnt.iter()
                    .map(|&c| c.to_string())
                    .collect::<Vec<String>>()
                    .join(", ")
            );
            for i in 0..input.k {
                perf[cid] += cnt[i] * (cnt[i] - 1) / 2;
                for j in i + 1..input.k {
                    perf[cid] -= cnt[i] * cnt[j];
                }
            }
        }
        (size, repr, count, perf)
    };

    for i in 0..input.n {
        for j in 0..input.n {
            if outcome.cid[i][j] != !0 {
                let cid = outcome.cid[i][j];
                let color = BG_PALETTE[c_repr[cid] - 1];
                let opacity = (c_perf[cid] as f64 / (80.0 * 79.0 / 2.0))
                    .clamp(0.0, 0.9 * 0.9)
                    .sqrt()
                    + 0.1;
                doc = doc.add(rect(
                    j * W,
                    i * W,
                    W,
                    W,
                    color,
                    opacity.clamp(0.0, 1.0),
                    None,
                ));
            }
        }
    }

    for i in 0..=input.n {
        doc = doc.add(line(0, i * W, W * input.n, i * W, "lightgray", 1));
        doc = doc.add(line(i * W, 0, i * W, W * input.n, "lightgray", 1));
    }

    for r in 0..input.n {
        for c in 0..input.n {
            if outcome.grid[r][c] != 0 {
                const DIR: [(usize, usize); 4] = [(0, !0), (1, 0), (0, 1), (!0, 0)];
                const CORNER: [(usize, usize); 4] = [(0, 0), (1, 0), (1, 1), (0, 1)];
                for (di, &(dr, dc)) in DIR.iter().enumerate() {
                    let rr = r + dr;
                    let cc = c + dc;
                    if rr < input.n && cc < input.n && outcome.cid[r][c] != outcome.cid[rr][cc] {
                        let (dr0, dc0) = CORNER[di];
                        let (dr1, dc1) = CORNER[(di + 1) % 4];
                        doc = doc.add(line(
                            (c + dc0) * W,
                            (r + dr0) * W,
                            (c + dc1) * W,
                            (r + dr1) * W,
                            "dimgray",
                            2,
                        ));
                    }
                }
            }
        }
    }

    for &(r0, c0, r1, c1) in outcome.cables.iter() {
        doc = doc.add(line(
            c0 * W + W / 2,
            r0 * W + W / 2,
            c1 * W + W / 2,
            r1 * W + W / 2,
            "darkgray",
            W / 8,
        ));
    }
    for i in 0..input.n {
        for j in 0..input.n {
            if outcome.grid[i][j] != !0 && outcome.grid[i][j] != 0 {
                let repr = c_repr[outcome.cid[i][j]];
                let color = if outcome.grid[i][j] != !0 && outcome.grid[i][j] != repr {
                    "red"
                } else {
                    "black"
                };
                doc = doc.add(
                    TextElement::new()
                        .add(Text::new(outcome.grid[i][j].to_string()))
                        .set("x", j * W + W / 2)
                        .set("y", i * W + W / 2 + 2)
                        .set("font-size", W - 6)
                        .set("font-family", "sans-serif")
                        .set("fill", color)
                        .set("text-anchor", "middle")
                        .set("dominant-baseline", "middle")
                        .set(
                            "style",
                            "stroke-width: 3; stroke: whitesmoke; paint-order: stroke;",
                        ),
                );
            }
        }
    }
    for i in 0..input.n {
        for j in 0..input.n {
            let tooltip = if outcome.cid[i][j] != !0 {
                format!(
                    "({}, {}) count=[{}] performance={}",
                    i, j, c_count[outcome.cid[i][j]], c_perf[outcome.cid[i][j]]
                )
            } else {
                format!("({}, {})", i, j)
            };
            doc = doc.add(rect(j * W, i * W, W, W, "white", 0.0, Some(&tooltip)));
        }
    }

    (score, error, doc.to_string())
}

#[cfg(target_arch = "wasm32")]
#[wasm_bindgen(getter_with_clone)]
pub struct VisResult {
    pub score: i32,
    pub error: String,
    pub svg: String,
}

#[cfg(target_arch = "wasm32")]
#[wasm_bindgen]
pub fn visualize(input: &str, output: &str, t: usize) -> Result<VisResult, JsError> {
    let input = parse_input(input);
    let output = parse_multi_output(&input, output);

    match output {
        Err(parse_err) => Err(JsError::new(&parse_err)),
        Ok(output) if t < output.len() => {
            let (score, error, svg) = vis(&input, &output[t]);
            Ok(VisResult { score, error, svg })
        }
        Ok(_) => Err(JsError::new("index out of bounds")),
    }
}

#[cfg(target_arch = "wasm32")]
#[wasm_bindgen]
pub fn get_max_turn(input: &str, output: &str) -> Result<usize, JsError> {
    let input = parse_input(input);
    parse_multi_output(&input, output)
        .map(|os| os.len().max(1) - 1)
        .map_err(|parse_err| JsError::new(&parse_err))
}
