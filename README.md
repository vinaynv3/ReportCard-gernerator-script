----------------------
Command Line Arguments
----------------------

Example:  ./word-count -b -sort SelectionSort -suf < textfile

-b | -a | -s
  (required) Specifies the type of tree for storing (word, count) pair
  possible trees are Binary search tree, Avl tree, and Splay tree

    -b - Count frequencies using an unbalanced binary search tree 
    -a - Count frequencies using an AVL tree 
    -s - Count frequencies using a splay tree 

-sort SelectionSort | MergeSort | HeapSort
  (optional) Specifies the type of sort.  
  If -sort is omitted, HeapSort is used

-suf
  (optional) Turns on suffix checker

-------------------------
Design Decisions & Issues
-------------------------
Since we stereotype against english majors, let's avoid writing this in an
essay format...

Q.  The original BinarySearchTree::Insert() resolves key collosion by
overwriting the old value with the new value.  How does the modified insert
functions resolve key collosions?

A.  The modified insert functions resolve key collosions by adding the new
value to the old value.  For example, if there exists a key K with a value 3,
and we wanted to insert a key K with value 2, the Insert function would change
the value to 3+2=5.  For our word-count, every key is inserted with a value 1.
However, it's easy to see that the insert functions allow different changes to
be made to the existing key-value tree.
    Consequently, the + operator must be overloaded for the ValueType.  


Q.  What is the relationship between the AVLNode class and the BSTNode class?

A.  The AVLNode is-a BSTNode.  Since the AVLTree inherits and uses many
methods from the BinarySearchTree (which operates on BSTNodes), the nodes used
by the AVLTree must be compatible.
    The difference between AVLNode and its ancestor is that each AVLNode
remembers its height information.   This is because the AVL rotations
frequently compares the height of its subtrees, and it would be inefficent if
we had to recursively calculate such info.



Class Hierachy

		|-------------------------|             |------------|
                |     BinarySearchTree    |--has-a----->|   BSTNode  |
                |-------------------------|             |------------|
                           ^    ^                           ^  ^
                          /      \                          |  |
                       is-a     is-a                        |  |
                        /          \                        |  |
                       /           |--------------|         |  |
                      /            |  SplayTree   |-has-a---|  |
                     /             |--------------|            |
                    /                                        is-a 
                   /                                           |
    |----------------|                                  |------------|
    |     AVLTree    |--has-a-------------------------->| AVLNode    |
    |----------------|                                  |------------|
   



Q.  There is no SplayNode class.  Why does SplayTree use BSTNodes?

A.  The SplayTree class uses BSTNode, while the AVLTree uses AVLNode. The idea
is that AVLTree needs to keep track of the height information. On the other
hand, SplayTree doesn't need to have height information. This is very similar
to BSTNode class, so there's no need to make a SplayNode class.


Q.  What are the similarities and differences between AVLTree rotation methods
and SplayTree rotation methods?  Why are they not methods of BinarySearchTree
class or the node classes?

A.  They are basically the same. However, for the AVLTree rotations, they need
to update the height information while the SplayTree's methods don't. These
methods could have been methods of BinarySearchTree, so that AVLTree and
SplayTree can inherit them; however, BST doesn't use rotation at all. We then
came to the decision of making each of the AVLTree, SplayTree different
rotation methods.


Q.  The Heap class does not allocate any memory--it shares the data.  Why?

A.  It makes it faster =)


Q.  Sort() is currently a method of HeapSort.  The alternative is to define an
external HeapSort() function that is a friend of the Heap class--HeapSort()
still needs to call the PercDown() function.  Why did we choose to make
HeapSort a function inside the Heap class?

A.  We think that our special(ized) Heap should know how to sort itself. :)


-----------------------
Word Frequency Analysis
-----------------------

	

---------
Profiling
---------

A. Our expected performance bottlenecks for the word-count program are...
	+ the Splay operation for SplayTree
	+ the insertHelp function for AVL, and
	+ the PercolateDown operation for Heap
	


  %   cumulative   self              self     total           
 1. time   seconds   seconds    calls  ns/call  ns/call  name    

  1.05      1.55     0.02                             SplayTree<>::Splay()
  4.26      0.45     0.10	                      AVLTree<>::insertHelp()
  1.28      1.76     0.03                             Heap::percDown()



--------------------
Algorithmic Analysis
--------------------

From our "SelectionSortSort vs. HeapSort" plot, we can see that when N is greater than
8000, selectionsort function grows faster than heapsort function. This confroms our knowledge
that heap sort has better performance than selecion sort in terms of time.

We know that both mergesort(f) and heapsort(g)  have O(n logn) runing time.
In our "MergeSort vs. HeapSort" plot, two lines are parallel to each other most of the time.
This shows that f/g = constant, which means that the runing time of the two algorithms are different
by a constant factor.

