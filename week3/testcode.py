from arrtree3 import *
v2 = [3,7,11,66,6,1,5,54,9]
h2 = treesimple(v2)
vistree2(h2)

h2.swapv(1,3) #h2 is the tree and i,j are indices of nodes to be swapped
h2.swapv(3,7)

h2.swapv(0,1)
h2.swapv(1,3)
h2.swapv(3,8)

print("==== max heapify and buildMaxHeap ====")
v3=[3,7,5,9,6,1,11,54,66]

max_heapify(v3,1)
build_max_heap(v3)

