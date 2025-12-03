use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    let p1_score = part1();
    let p2_score = part2();
    println!("Part 1: {}", p1_score);
    println!("Part 2: {}", p2_score);
}

fn part1() {
    let mut p1_total_score = 0;
    let file = File::open("input.txt").expect("File Does Not Exist");
    let reader = io::BufReader::new(file);

    // Read each line from the file
    for line in reader.lines() {
        let line = line.expect("Could not read line");

        let score = match line {
            "A X" => 4,
            "A Y" => 8,
            "A Z" => 3,
            "B X" => 1,
            "B Y" => 5,
            "B Z" => 9,
            "C X" => 7,
            "C Y" => 2,
            "C Z" => 6,
            _ => 0,
        };

        // Determine choice points based on player's choice
        let choice = match player {
            'Y' => 2, // Paper
            'Z' => 3, // Scissors
            _ => 1,   // Rock (X)
        };
    }
    p1_total_score += score;

    return p1_total_score;
}

fn part2() {
    let mut p2_total_score = 0;
    let file = File::open("input.txt").expect("File Does Not Exist");
    let reader = io::BufReader::new(file);

    // Read each line from the file
    for line in reader.lines() {
        let line = line.expect("Could not read line");
        let chars: Vec<char> = line.chars().collect();

        if chars.len() < 3 {
            continue;
        }

        let needed_outcome = chars[2]; // X, Y, or Z
        let opponent_play = chars[0]; // A, B, or C

        // Determine outcome points based on the game rules
        let p2_outcome = match (needed_outcome, opponent_play) {
            ('Y', 'A') => 3, // Draw
            ('Y', 'B') => 3, // Draw
            ('Y', 'C') => 3, // Draw
            ('Z', 'A') => 6, // Win
            ('Z', 'B') => 6, // Win
            ('Z', 'C') => 6, // Win
            _ => 0,          // Lose
        };
        // Determine choice points based on player's choice
        let p2_choice = match (needed_outcome, opponent_play) {
            ('Y', 'A') => 1, // Draw
            ('Y', 'B') => 2, // Draw
            ('Y', 'C') => 3, // Draw
            ('X', 'A') => 2, // Lose
            ('X', 'B') => 3, // Lose
            ('X', 'C') => 1, // Lose
            ('Z', 'A') => 2, // Win
            ('Z', 'B') => 3, // Win
            ('Z', 'C') => 1, // Win
            _ => 0,          // No Matches
        };
        p2_total_score += p2_outcome + p2_choice;
    }

    return p2_total_score;
}
