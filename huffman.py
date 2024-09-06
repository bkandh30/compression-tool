from huffman import HuffmanCoding
import sys

test_file = "sample.txt"

h = HuffmanCoding(test_file)

compressed_file = h.compress()
print(f"Compressed file is: {compressed_file}")

decompressed_file = h.decompress(compressed_file)
print(f"Decompressed file is: {decompressed_file}")