use std::io::prelude::*;
use tools::*;

fn main() {
    if std::env::args().len() != 2 {
        eprintln!("Usage: {} seeds.txt", std::env::args().nth(0).unwrap());
        return;
    }
    if !std::path::Path::new("in").exists() {
        std::fs::create_dir("in").unwrap();
    }
    let f = std::env::args().nth(1).unwrap();
    let f = std::fs::File::open(&f).unwrap_or_else(|_| {
        eprintln!("no such file: {}", f);
        std::process::exit(1)
    });
    let f = std::io::BufReader::new(f);
    let mut id = 0;
    for line in f.lines() {
        let line = line.unwrap();
        let line = line.trim();
        if line.len() == 0 {
            continue;
        }
        let seed = line.parse::<u64>().unwrap_or_else(|_| {
            eprintln!("parse failed: {}", line);
            std::process::exit(1);
        });
        let input = gen(seed, None, None);
        let mut w =
            std::io::BufWriter::new(std::fs::File::create(format!("in/{:04}.txt", id)).unwrap());
        write!(w, "{}", input).unwrap();
        id += 1;
    }
}
