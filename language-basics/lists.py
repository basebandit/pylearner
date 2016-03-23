# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

def lists():
    """
    Lists have two methods, extend and append, that look like they do the same thing, but are in fact
    completely different. extend takes a single argument, which is always a list, and adds each of the
    elements of that list to the original list.
    """
    #Creating a list
    li = ["a", "b", "devmars", "z", "example"]
    print(li)
    
    #Accessing list elements
    print(li[0])
    print(li[4])
    print(li[-1])#first from behind
    print(li[-3])#third from behind
    
    #Slicing a list
    print(li[1:3])#start from element at index 1 to but not including element at index 3
    print(li[1:-1])#start from element at index 1 upto but not including the first element from behind
    print(li[0:3])#start from element at index 0 to but not including element at index 3

    #slicing shorthand
    print(li[:3])#start from index 0 upto but not including element at index 3
    print(li[3:])#start from element at index 3 upto the last element including it same as li[3:5]
    print(li[:])#Print the whole list
    
    #li[:n] returns the first n elements
    #li[n:] returns the rest,regardless of the length of the list
    
    #adding elements to a list
    li.append("new")#adds a single element "new" to the end of the list.
    li.insert(2, "new")#inserts a single element "new" into a list at the given 
    li.extend(["two", "elements"])#concatenates lists.You call it with one argument,a list
    
    print(li)
    li.extend(['d', 'e', 'f'])
    print(li)
    li.append(['d', 'e', 'f'])
    print(li)
    print(li[-1])
    
    #searching lists
    print("li.index(\"example\")-> {}".format(li.index("example")))
    print(li.index('new'))
    #print(li.index('c')) Traceback (innermost last):
                        # File "<interactive input>", line 1, in ?
                        # ValueError: list.index(x): x not in list
    """
    index finds the first occurrence of a value in the list and returns the index.
    index finds the first occurrence of a value in the list. In this case, 'new' occurs twice in the list, in li[2]
    and li[6], but index will return only the first index, 2.
    """
    
    
    



if __name__ == "__main__":
    lists()
