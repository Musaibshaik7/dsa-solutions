def traverse(arr):
    for i in range(len(arr)):
        print(arr[i])
    '''or
    for x in arr:
    print(x)'''

def ins_val_at_pos(arr):
    print("add value at pos")
    pos=int(input("enter position:"))
    value=int(input("enter value:"))
    print(f"before:{arr}")
#   or   arr.insert(pos,value)
#     print(arr)
    if pos>=0 and pos<=len(arr):
        arr2=arr[0:pos]
        arr2.append(value)
      
        for el in range(pos,len(arr)):
            arr2.append(arr[el])
      
        print("after:",arr2)
        return arr2
    else:
        print("out of range")
        return arr
#without second array
def insert_arr(arr):

    pos=int(input("enter position:"))
    if pos>=0 and pos<=len(arr):
        value=int(input("enter value:"))
        arr.append(None)

        i=len(arr)-2
        while(i>=pos):
            arr[i+1]=arr[i]
            i-=1
        arr[pos]=value
        print(arr)

def delete_at_pos(arr):
    pos=int(input("enter pos:"))
    if pos>=0 and pos<len(arr):
        i=pos
        while(i<len(arr)-1):
            arr[i]=arr[i+1]
            i+=1
        del arr[i]
        print(arr)

def reverse_arr(arr):
    # i=0
    # n=len(arr)
    # while(i<n//2):
    #     temp=arr[n-i-1]
    #     arr[n-i-1]=arr[i]
    #     arr[i]=temp
        
    #     i+=1
    # print(arr)
    #or
    right=0
    left=len(arr)-1
    while right <left :
        temp=arr[right]
        arr[right]=arr[left]
        arr[left]=temp
        left-=1
        right+=1
        print(arr)
     

def frequency_count(arr):
    for el in arr:
        temp=el
        count=0
        i=0
        while(i<len(arr)):
            if(temp==arr[i]):
                count+=1
            i+=1
        print(f"{el}:{count}")



#main()
arr=[10,54,44,32,25,62,36]
traverse(arr)
arr=ins_val_at_pos(arr)
insert_arr(arr)
delete_at_pos(arr)
reverse_arr(arr)
frequency_count(arr)
