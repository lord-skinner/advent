package com.example.aoc.day01;

import com.example.aoc.utils.InputUtils;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        List<String> input = InputUtils.readInput("day01.txt");

        System.out.println("--- Day 01 ---");
        System.out.println("Part 1: " + solvePart1(input));
        System.out.println("Part 2: " + solvePart2(input));
    }

    /**
     * Part 1: Count how many times the dial lands on position 0 after each complete
     * rotation.
     * The dial has 100 positions (0-99) and starts at position 50.
     * We process each rotation instruction and only count if we END on position 0.
     */
    public static Object solvePart1(List<String> input) {
        int currentPosition = 50;
        int zeroCount = 0;
        int totalPositions = 100;

        for (String line : input) {
            char direction = line.charAt(0);
            int distance = Integer.parseInt(line.substring(1));

            // Apply the full rotation at once using modulo for circular wrapping
            if (direction == 'R') {
                currentPosition = (currentPosition + distance) % totalPositions;
            } else if (direction == 'L') {
                currentPosition = (currentPosition - distance) % totalPositions;
                // Handle negative modulo in Java (e.g., -1 % 100 = -1, not 99)
                if (currentPosition < 0) {
                    currentPosition += totalPositions;
                }
            }

            // Count only if we land exactly on 0 after the rotation
            if (currentPosition == 0) {
                zeroCount++;
            }
        }

        return zeroCount;
    }

    /**
     * Part 2: Count EVERY time the dial passes through position 0, not just when it
     * lands there.
     * OPTIMIZED VERSION: Uses mathematical floor division instead of iterating
     * through each click.
     * 
     * Time Complexity: O(n) where n = number of input lines (vs O(n×m) for
     * iterative approach)
     * 
     * Key insight: When rotating k clicks from position p:
     * - Right: We pass through 0 exactly ⌊(p + k) / 100⌋ times
     * - Left: More complex due to edge cases:
     * - If starting at 0: we hit 0 every 100 clicks (not counting the start)
     * - If k >= p: we hit 0 after p clicks, then every 100 clicks after that
     * - If k < p: we never hit 0
     * 
     * Example: position 95, rotate right 110 clicks
     * - Calculation: (95 + 110) / 100 = 2 (integer division)
     * - We pass through 0 at: click 5 (position 0) and click 105 (position 0 again)
     */
    public static Object solvePart2(List<String> input) {
        int position = 50;
        int zeroCount = 0;

        for (String line : input) {
            char direction = line.charAt(0);
            int clicks = Integer.parseInt(line.substring(1));

            if (direction == 'R') {
                // Calculate how many times we pass through 0 during right rotation
                // Floor division: (position + clicks) / 100
                zeroCount += (position + clicks) / 100;

                // Update final position
                position = (position + clicks) % 100;
            } else { // direction == 'L'
                // For left rotation, handle edge cases carefully
                if (position == 0) {
                    // Starting at 0, going left: we hit 0 again every 100 clicks
                    // (Don't count the starting position)
                    zeroCount += clicks / 100;
                } else if (clicks >= position) {
                    // We will cross 0
                    // First hit after 'position' clicks, then every 100 clicks
                    zeroCount += 1 + (clicks - position) / 100;
                }
                // else: clicks < position, we never hit 0

                // Update final position
                position = (position - clicks) % 100;
                if (position < 0) {
                    position += 100;
                }
            }
        }

        return zeroCount;
    }
}
