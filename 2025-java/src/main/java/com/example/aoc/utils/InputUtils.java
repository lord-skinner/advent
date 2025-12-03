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
