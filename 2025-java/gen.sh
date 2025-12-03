#!/bin/bash

# Configuration
GROUP_ID="com/example/aoc"
SRC_DIR="src/main/java/$GROUP_ID"
RES_DIR="src/main/resources"

echo "🚀 Starting Advent of Code Setup..."

# 1. Create the Utils Class (To handle file reading cleanly)
UTILS_DIR="$SRC_DIR/utils"
mkdir -p "$UTILS_DIR"

cat <<EOF > "$UTILS_DIR/InputUtils.java"
package com.example.aoc.utils;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.ArrayList;

public class InputUtils {
    public static List<String> readInput(String fileName) {
        try {
            return Files.readAllLines(Paths.get("src/main/resources/" + fileName));
        } catch (Exception e) {
            System.err.println("Error reading file: " + fileName);
            e.printStackTrace();
            return new ArrayList<>();
        }
    }
}
EOF
echo "✅ Created InputUtils.java"

# 2. Loop through Days 1 to 25
for i in {1..25}; do
    # Pad the number with a zero (e.g., 1 becomes 01)
    DAY=$(printf "%02d" $i)
    
    # Define paths
    DAY_PKG_DIR="$SRC_DIR/day$DAY"
    mkdir -p "$DAY_PKG_DIR"
    mkdir -p "$RES_DIR"
    
    # Create empty input file in resources
    touch "$RES_DIR/day$DAY.txt"
    
    # Create the Solution.java file
    cat <<EOF > "$DAY_PKG_DIR/Solution.java"
package com.example.aoc.day$DAY;

import com.example.aoc.utils.InputUtils;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        List<String> input = InputUtils.readInput("day$DAY.txt");
        
        System.out.println("--- Day $DAY ---");
        System.out.println("Part 1: " + solvePart1(input));
        System.out.println("Part 2: " + solvePart2(input));
    }

    public static Object solvePart1(List<String> input) {
        return "TODO";
    }

    public static Object solvePart2(List<String> input) {
        return "TODO";
    }
}
EOF
    echo "   - Generated Day $DAY"
done

echo "🎉 Setup Complete! Happy Coding!"