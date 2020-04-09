# Problem 6: Union and Intersection

For union I first create a deep copy of both lists. I then find the end of the first list and point it to the start of the second.

For intersecion I use a hash map with the key being the node value and the value being the number of occurences. I populate the hash map with the first list and then iterate through the second to find matches.

Time complexity of union: O(n) Reason: The function has three independent loops looping n times


Time complexity of intersection: O(n) Reason: The function loops n times

