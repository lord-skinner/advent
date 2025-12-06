package com.example.aoc.day02;

import com.example.aoc.utils.InputUtils;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        List<String> input = InputUtils.readInput("day02.txt");

        System.out.println("--- Day 02 ---");
        System.out.println("Part 1: " + solvePart1(input));
        System.out.println("Part 2: " + solvePart2(input));
    }

    /**
     * Solves Part 1 of the puzzle.
     * An ID is considered invalid if:
     * 1. It has an even number of digits.
     * 2. The first half of the digits is identical to the second half.
     * The method iterates through all IDs in the given ranges and sums up the
     * invalid ones.
     *
     * @param input The input list containing the ranges string.
     * @return The sum of all invalid IDs found in the ranges.
     */
    public static Object solvePart1(List<String> input) {
        if (input == null || input.isEmpty()) {
            return 0L;
        }

        String line = input.get(0);
        String[] ranges = line.split(",");
        long totalSum = 0;

        for (String range : ranges) {
            String[] parts = range.split("-");
            long start = Long.parseLong(parts[0]);
            long end = Long.parseLong(parts[1]);

            for (long i = start; i <= end; i++) {
                if (isInvalidId(i)) {
                    totalSum += i;
                }
            }
        }

        return totalSum;
    }

    /**
     * Checks if an ID is invalid according to Part 1 rules.
     *
     * @param id The ID to check.
     * @return true if the ID has an even length and the first half equals the
     *         second half.
     */
    private static boolean isInvalidId(long id) {
        String s = String.valueOf(id);
        int len = s.length();
        if (len % 2 != 0) {
            return false;
        }
        String firstHalf = s.substring(0, len / 2);
        String secondHalf = s.substring(len / 2);
        return firstHalf.equals(secondHalf);
    }

    /**
     * Solves Part 2 of the puzzle.
     * <p>
     * An ID is considered invalid if it is made only of some sequence of digits
     * repeated at least twice.
     * For example: 123123123 (123 repeated 3 times).
     * <p>
     * The method iterates through all IDs in the given ranges and sums up the
     * invalid ones according to Part 2 rules.
     *
     * @param input The input list containing the ranges string.
     * @return The sum of all invalid IDs found in the ranges.
     */
    public static Object solvePart2(List<String> input) {
        if (input == null || input.isEmpty()) {
            return 0L;
        }

        String line = input.get(0);
        String[] ranges = line.split(",");
        long totalSum = 0;

        for (String range : ranges) {
            String[] parts = range.split("-");
            long start = Long.parseLong(parts[0]);
            long end = Long.parseLong(parts[1]);

            for (long i = start; i <= end; i++) {
                if (isInvalidIdPart2(i)) {
                    totalSum += i;
                }
            }
        }

        return totalSum;
    }

    /**
     * Checks if an ID is invalid according to Part 2 rules.
     *
     * @param id The ID to check.
     * @return true if the ID is formed by a repeating sequence of digits.
     */
    private static boolean isInvalidIdPart2(long id) {
        String s = String.valueOf(id);
        int len = s.length();

        // Try all possible lengths for the repeating sequence
        // The sequence length must be at least 1 and at most len / 2
        for (int seqLen = 1; seqLen <= len / 2; seqLen++) {
            // The total length must be a multiple of the sequence length
            if (len % seqLen == 0) {
                String sequence = s.substring(0, seqLen);
                boolean isRepeating = true;
                for (int i = seqLen; i < len; i += seqLen) {
                    if (!s.substring(i, i + seqLen).equals(sequence)) {
                        isRepeating = false;
                        break;
                    }
                }
                if (isRepeating) {
                    return true;
                }
            }
        }
        return false;
    }
}
