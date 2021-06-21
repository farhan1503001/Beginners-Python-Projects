def binary_search(arr,number):
    low=0
    high=len(arr)-1
    mid=0
    while(low<=high):
        mid=int((low+high)/2)
        if number>arr[mid]:
            low=mid+1
        elif number<arr[mid]:
            high=mid-1
        else:
            return mid
    
    return -1
def binary_search_rec(arr,low,high,number):
    if low<=high:
        mid=int((low+high)/2)
        if number>arr[mid]:
            binary_search_rec(arr,mid+1,high,number)
        elif number<arr[mid]:
            binary_search_rec(arr,low,mid-1,number)
        else:
            return mid
    else:
        return -1

arr = [2,89,100,23,4,35]
arr.sort()
print(arr)
number=int(input('Enter the value to be searched: '))
result=binary_search(arr,number)
if result==-1:
    print('Value not found')
else:
    print('value found at index : ',result)

result1=binary_search_rec(arr,0,len(arr)-1,number)
if result1==-1:
    print('Value not found')
else:
    print("Value found at index ",result1)
