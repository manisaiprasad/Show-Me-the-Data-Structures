# Problem 3: Huffman Coding

I used a min heap to allow for easy merging of the frequency nodes. I used heapq library to make the addition and removal of nodes.

The time complexity of encode() is O(nlogn) 

Reason: make_frequency_dict takes O(n) time, min_heapify_dict takes O(n) time, merge_nodes takes O(logn), make_codes takes O(n), get_encoded_text takes O(n). These all result in a complexity of nlogn

The time complexity of decode() is O(n) Reason: There is a for loop going through each character in the encoded_text
