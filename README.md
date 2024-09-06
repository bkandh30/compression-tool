# compression-tool

This is my python solution to John Crickett's Coding Challenge: [Build Your Own Compression Tool](https://codingchallenges.fyi/challenges/challenge-huffman)

## Description

This is a simple implementation of a Huffman Coding compression tool.

## How to install

```
git clone https://github.com/bkandh30/compression-tool.git
```

## Compression Implementation

- Build frequency dictionary.
- Build priority queue.
- Build HuffmanTree by selecting 2 minimum nodes and merging them.
- Assign codes to characters by traversing the tree from root.
- Encode the input text by replacing characters with it's binary code.
- If overall length of final encoded bit streams is not multiple of 8, add some padding to the text.
- Store this padding information at the start of the overall encoded bit stream.
- Write the result to an output binary file.

## Decompression Implementation

- Read the binary file.
- Read the padding information. Remove the padded bits.
- Decode the bits - read the bits and replace the valid Huffman Code bits with the character values.
- Save the decoded data into output file.
