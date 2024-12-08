use itertools::Itertools;

fn main() {
    let totals: Vec<u64> = include_str!("input.txt")
        .split("\n\n")
        .map(|elf| {
            elf.split('\n')
                .map(|food| food.parse::<u64>().unwrap_or(0))
                .sum()
        })
        .sorted()
        .rev()
        .collect();

    println!("Part 1: {}", totals[0]);
    println!("Part 2: {}", totals.iter().take(3).sum::<u64>());
}
