
import src.intradev as id

def flipFileLines(inputFilePath, outputFilePath="outputTestFile.txt"):
    # Read whole file and strip existing newlines safely (works even if last line has no newline)
    with open(inputFilePath, "r", encoding="utf-8", new