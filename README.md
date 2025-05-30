# Compression Tool

A Python implementation of Huffman Coding for lossless data compression, created in response to [John Crickett's Coding Challenge](https://codingchallenges.fyi/challenges/challenge-huffman): *Build Your Own Compression Tool*.

## Overview

This project demonstrates a basic implementation of Huffman Coding—a widely used algorithm for efficient lossless compression. The tool provides both compression and decompression functionality using binary encoding based on character frequencies.

## Description

This is a simple implementation of a Huffman Coding compression tool.

## Installation

To clone the repository locally:

```bash
git clone https://github.com/bkandh30/compression-tool.git
```

## Features

### Compression

1. Constructs a frequency dictionary from the input text.
2. Builds a priority queue using character frequencies.
3. Creates a Huffman Tree by repeatedly merging the two lowest-frequency nodes.
4. Assigns binary codes to each character via tree traversal.
5. Encodes the input text by replacing each character with its corresponding binary code.
6. Adds padding to the final bit stream if its length is not a multiple of 8.
7. Prepends the padding information to the bit stream.
8. Writes the encoded data to a binary output file.

### Decompression

1. Reads the binary input file.
2. Extracts and removes the padding bits based on stored metadata.
3. Decodes the binary stream by mapping valid Huffman codes back to their respective characters.
4. Writes the decompressed output to a text file.

## License

This project is open-source and available under the [MIT License](LICENSE).
