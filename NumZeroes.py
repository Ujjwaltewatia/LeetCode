def numZero(num,count=0):
    if num==0:
        return count
    
    rem=num%10
    if rem==0:
        count+=1
        
    return numZero(num//10,count)
