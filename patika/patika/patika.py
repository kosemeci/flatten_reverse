#ilk alıştırma 
input1= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output1=[]
def flatten(x):
    for i in x:
        if  isinstance(i,list):
            flatten(i)
        else:
            output1.append(i)
    return output1
print(flatten(input1))

#**********************************************************************************

#ikinci alıştırma

input2= [[1, 2], [3, 4], [5, 6, 7]]
output2=[]
def tersi(x):
    for i in x:
        if isinstance(i,list):
            tersi(i)
        else:
            output2.append(i)        
    return output2[::-1]
print(tersi(input2))
