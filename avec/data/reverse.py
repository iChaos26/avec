"""
Possible implementation with list.reverse()

    def reverse(self, data):
        return self.data.reverse()

but hackerrank does not permit built in function that shorttens the way:

 Using slicing, e.g. array = array[::-1], is a neat trick and very Pythonic, but a little obscure for newbies maybe. 
 Using the reverse() method is a good way to go in day to day coding because it is easily readable.

 However, if you need to reverse a list in place as in an interview question,
 you will likely not be able to use built in methods like these. 
 The interviewer will be looking at how you approach the problem rather than the depth of Python knowledge, 
 an algorithmic approach is required. The following example, using a classic swap, might be one way to do it:-
 
 def reverse_in_place(lst):      # Declare a function
    size = len(lst)             # Get the length of the sequence
    hiindex = size - 1
    its = size/2                # Number of iterations required
    for i in xrange(0, its):    # i is the low index pointer
        temp = lst[hiindex]     # Perform a classic swap
        lst[hiindex] = lst[i]
        lst[i] = temp
        hiindex -= 1            # Decrement the high index pointer
    print "Done!"

# Now test it!!
array = [2, 5, 8, 9, 12, 19, 25, 27, 32, 60, 65, 1, 7, 24, 124, 654]

print array                    # Print the original sequence
reverse_in_place(array)        # Call the function passing the list
print array                    # Print reversed list


**The result:**
[2, 5, 8, 9, 12, 19, 25, 27, 32, 60, 65, 1, 7, 24, 124, 654]
Done!
[654, 124, 24, 7, 1, 65, 60, 32, 27, 25, 19, 12, 9, 8, 5, 2]

from: https://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python
"""

def reversePrint(llist):
    
    if llist is None:
        return
    else:
        out = []
        node = llist
        
        while node != None:
            out.append(node.data)
            node = node.next
            
        print("\n".join(map(str, out[::-1])))

#!without hackerrank
def ReversePrint(head):
    if head is None:
        return
    else:
        out = []
        node = head
        
        while node != None:
            out.append(node.data)
            node = node.next
            
        print("\n".join(map(str, out.reverse())))
