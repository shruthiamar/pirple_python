
def equal(a,b,c):
    if int(a) == int(b) or int(b) == int(c) or int(c) == int(a):
        return True
    else:
        return False

print(equal('1','3','5'))
print(equal(1,1,2))
