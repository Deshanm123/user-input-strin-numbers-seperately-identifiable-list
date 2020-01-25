# Online Python compiler (interpreter) to run Python online.
RandomList=[]
for i in range (0,10):
    element=input("enter a element")
    x = element.isnumeric()
    if x:
 
        element=int(element)
        RandomList.insert(2,element)

    else:
        RandomList.insert (2,element)
print(RandomList)
   
        