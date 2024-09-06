import heapq
import os

class HuffmanCoding:
    #Requires the path of the file
    def __init__(self, path) -> None:
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        #defining comparators less_than and equals
        def __lt__(self,other):
            return self.freq < other.freq
        
        def __eq__(self,other):
            if (other == None):
                return False
            if not isinstance(other, HuffmanCoding.HeapNode):
                return False
            return self.freq == other.freq

    #Compression

    #Calculates the frequency of the character    
    def make_frequency_dict(self,text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency
    
    #Create the priority queue
    def make_heap(self, frequency):
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)
    
    #Build huffman tree and save the root node in heap
    def merge_nodes(self):
        while(len(self.heap)>1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)
    
    def make_codes_helper(self, root, current_code):
        if(root == None):
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    #Make nodes for the characters and save them
    def make_codes(self):
        #Case for single unique character
        if len(self.heap) == 1:
            root = self.heap[0]
            self.codes[root.char] = "0"
            self.reverse_mapping["0"] = root.char
        else:
            root = heapq.heappop(self.heap)
            current_code = ""
            self.make_codes_helper(root, current_code)
    
    #Encode the text by replacing the characters 
    def get_encoded_text(self,text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text
    
    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"
        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def get_byte_array(self, padded_encoded_text):
        if(len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)
        
        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte,2))
        return b
    
    def compress(self):
        try:
            #Check if the file is empty
            if os.stat(self.path).st_size == 0:
                raise ValueError("Input File is Empty")
            
            filename, file_extension = os.path.splitext(self.path)
            output_path = filename + ".bin"
            with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
                text = file.read()
                text = text.rstrip()
                frequency = self.make_frequency_dict(text)
                self.make_heap(frequency)
                self.merge_nodes()
                encoded_text = self.get_encoded_text(text)
                padded_encoded_text = self.pad_encoded_text(encoded_text)
                b = self.get_byte_array(padded_encoded_text)
                output.write(bytes(b))
            print("File Compressed Successfully")
            return output_path
        except FileNotFoundError:
            print(f"Error: The file '{self.path}' was not found.")
        except Exception as e:
            print(f"Error: {str(e)}")

    #Functions for decompression

    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)
        padded_encoded_text = padded_encoded_text[8:] 
        encoded_text = padded_encoded_text[:-1*extra_padding]
        return encoded_text

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""
        
        for bit in encoded_text:
            current_code += bit
            if(current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""
        return decoded_text


    def decompress(self, input_path):
        try:
            filename, file_extension = os.path.splitext(input_path)
            output_path = filename + "_decompressed" + ".txt"
        
            with open(input_path, 'rb') as file, open(output_path, 'w') as output:
                bit_string = ""
                byte = file.read(1)
                while(len(byte) > 0):
                    byte = ord(byte)
                    bits = bin(byte)[2:].rjust(8, '0')
                    bit_string += bits
                    byte = file.read(1)
            
                encoded_text = self.remove_padding(bit_string)
                decompressed_text = self.decode_text(encoded_text)
                output.write(decompressed_text)

            print("Decompressed")
            return output_path
        except FileNotFoundError:
            print(f"Error: The file '{input_path}' was not found.")
        except Exception as e:
            print(f"Error: {str(e)}")