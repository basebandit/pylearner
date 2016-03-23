# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
def dictionary():
    """
    Dictionaries have no concept of order among elements. It is incorrect to say
    that the elements are "out of order", they are simply unordered.
    Dictionary keys are case sensitive.
    """
    #creating a dictionary
    d = {"server":"devmars", "database":"master"}
    print(d)
    print(d['server'])
    
    #modifying a dictionary
    d['database'] = "pubs"
    print(d)
    #Addding an item to a dictionary
    d['uid'] = 'ke'
    print(d)
    
    #Mixing datatypes in dictionaries
    d["retrycount"] = 3
    print(d)
    d[42] = "douglas"
    print(d)
    
    #Deleting items from dictionaries
    #del lets you delete individual items from a dictionary by key
    del d[42]
    print(d)
    #clear deletes all items from a dictionary
    d.clear()
    print(d)
    
    
    
    
if __name__ == "__main__":
    dictionary()
