use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn day01() -> Result<(), Box<dyn std::error::Error>> {

    let lines = read_lines("data/day01.txt")?;
    let (mut col1, mut col2) = (vec![], vec![]);

    for line in lines.flatten() {
        let v = line
            .split_whitespace()
            .map(|l| l.to_owned().parse::<i32>().unwrap())
            .collect::<Vec<_>>();
        col1.push(v[0].clone());
        col2.push(v[1].clone());
    }

    col1.sort();
    col2.sort();

    let result: u32 = col1.iter().zip(col2.iter()).map(|(c1, c2)| (c2-c1).abs() as u32).sum();
    println!("Day 01 | Part 1: {result}  | {status}", status=if result == 1223326{"Correct"}else{"Wrong"});
    let result: u32 = col1.iter().map(|c1| (*c1 as u32) * (col2.iter().filter(|c2| *c2 == c1).count() as u32)).sum();
    println!("       | Part 2: {result} | {status}", status=if result == 21070419{"Correct"}else{"Wrong"});
    Ok(())
}

fn day02() -> Result<(), Box<dyn std::error::Error>> {

    fn is_safe(levels:Vec<i32>) -> bool {
        let diff: Vec<_> = (0..levels.len()-1).map(|i| (levels[i+1] - levels[i]).abs() as u32).collect();
        let mut sorted_levels = levels.clone();
        sorted_levels.sort();
        let mut sorted_levels_reverse = sorted_levels.clone();
        sorted_levels_reverse.reverse();
        let diff_min = diff.iter().min().unwrap();
        let diff_max = diff.iter().max().unwrap();

        return (levels == sorted_levels || levels == sorted_levels_reverse)
            && (*diff_min >= 1 && *diff_max <= 3)
    }

    let lines = read_lines("data/day02.txt")?;
    let mut unsafe_levels = vec![];
    let mut result = 0;
    for line in lines.flatten() {
        let levels = line
            .split_whitespace()
            .map(|l| l.to_owned().parse::<i32>().unwrap())
            .collect::<Vec<_>>();
        let safe = is_safe(levels.clone());
        if safe { result += 1 } else { unsafe_levels.push(levels)}
    }
    println!("Day 02 | Part 1: {result}      | {status}", status=if result == 524 {"Correct"}else{"Wrong"});

    for levels in unsafe_levels {
        for i in 0..levels.len(){
            let mut leave_one_out = levels[..i].to_owned();
            leave_one_out.extend(&levels[i+1..]);
            if is_safe(leave_one_out){result += 1; break}
        }
    }
    println!("       | Part 2: {result}      | {status}", status=if result == 569 {"Correct"}else{"Wrong"});

    Ok(())
}

// The output is wrapped in a Result to allow matching on errors.
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    day01()?;
    day02()?;
    Ok(())
}