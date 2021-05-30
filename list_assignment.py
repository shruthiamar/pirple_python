myUniqueList = []
myLeftovers  = []
def listAdd(a):
    if a in myUniqueList:
        addLeftovers(a)
        return False
    else:
        myUniqueList.append(a)
        return True

def addLeftovers(a):
    myLeftovers.append(a)

#Testing the function
print(myUniqueList)
print(listAdd('dog'))
print(listAdd("cat"))
print(myUniqueList)

print(listAdd('dog'))
print(myUniqueList)
print(myLeftovers)
