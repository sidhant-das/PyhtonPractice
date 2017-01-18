arr=['a','b','c','d','e']
x=arr
print(x)
for el in x:
    print(el,' ',x.index(el))
    arr[arr.index(el)]=x[len(x)-1-x.index(el)]
print(arr)
