def numSteps(num):
    steps=0
    return helper(num,steps)

def helper(num,steps):
    if num==0:
        return steps
    
    if num%2==0:
        num=num/2
        steps+=1
    else:
        num=num-1
        steps+=1
    
    return helper(num,steps)

print(numSteps(8))
