# Murat Demiray

list = [1,2,3,4,5,'Malcom in the Middle','a','b','c','d','e']

l = len(list)  #length of list

if l % 2 == 0 : # equal half - if you remove middle this will work
    first = list[0:int(l/2)]
    second =  list[int(l/2):l]
    list = second + first
else:           # not equal half - this works when there is a middle element
    first = list[0:int(l/2)]
    second =  list[int((l+1)/2):l]
    middle = list[int((l)/2):int((l+1)/2)]
    list = second + middle + first

print (list)