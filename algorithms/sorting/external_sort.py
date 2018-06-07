'''
used when the data cannot fit into the memory

K路归并算法 (heap, O(nlogk) time)
1. divide the file into k batches
2. sort each batch and save to a temporary file
3. create a min heap of size k and insert the first element of each file
4. while heap is not empty:
   a. extract the smallest element curr in the heap
   b. write its value to output file
   c. find the next elemnt of curr, if it exists insert that element to heap
'''