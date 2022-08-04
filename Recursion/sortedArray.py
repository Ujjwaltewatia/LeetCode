#check whether given array is sorted or not
arr=[1,2,3,4,5,44,6]

def sorted(arr,index=0):
    
    if index==len(arr)-1:
        return True
    
    if arr[index]>arr[index+1]:
        return False
    index+=1
    return sorted(arr,index)

print(sorted(arr))
