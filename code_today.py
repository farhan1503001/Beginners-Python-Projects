
def find_occurances(numbers,x):
    count=0
    low=0
    high=len(numbers)
    mid=int((low+high)/2)
    index=0
    flag=False
    while(low<=high):
        if x==numbers[mid]:
            index=mid
            count=count+1
        elif x>numbers[mid]:
            low=mid+1
        else:
            high=mid-1    
    return count


numbers=[1, 2, 2, 3, 3, 3]
x=3

value=find_occurances(numbers,x)
print(value)



