import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def count_frequencies(filename):
    frequencies = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char in frequencies:
                    frequencies[char] += 1
                else:
                    frequencies[char] = 1
    return frequencies

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(root):
    codes = {}

    def traverse(node, prefix=""):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = prefix
        traverse(node.left, prefix + "0")
        traverse(node.right, prefix + "1")

    traverse(root)
    return codes

def huffman_encode(input_text, codes):
    encoded_text = "".join(codes[char] for char in input_text)
    return encoded_text

def huffman_decode(encoded_text, root):
    decoded_text = []
    node = root

    for bit in encoded_text:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decoded_text.append(node.char)
            node = root

    return "".join(decoded_text)

def main():
    input_file = "input.txt"
    output_file = "encoded.txt"
    decoded_file = "decoded.txt"

    # Step 1: Count frequencies
    frequencies = count_frequencies(input_file)

    # Step 2: Build Huffman tree
    huffman_tree = build_huffman_tree(frequencies)

    # Step 3: Generate Huffman codes
    huffman_codes = generate_huffman_codes(huffman_tree)

    # Step 4: Encode the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        input_text = file.read()
    encoded_text = huffman_encode(input_text, huffman_codes)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(encoded_text)

    # Step 5: Decode the encoded file
    decoded_text = huffman_decode(encoded_text, huffman_tree)
    with open(decoded_file, 'w', encoding='utf-8') as file:
        file.write(decoded_text)

    print("Encoding and decoding completed successfully!")

if __name__ == "__main__":
    main()
