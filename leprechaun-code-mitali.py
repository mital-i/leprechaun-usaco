li = []

n = int(input())
for i in range(n):
    line = [int(i) for i in input().split()]
    line = line + line + line
    li.append(line)

li = li+li+li

def prefix_sum(li, n): 
    temp_sum = 0
    max_sum = -99999999999999
    counter = n
    for i in range(len(li)):
        temp_sum += li[i]
        counter+=1
        #print(temp_sum)
        if li[i] > temp_sum:
            temp_sum = li[i]
            #print()
            #print(temp_sum)
            #print()
        if counter >= n: 
            counter = 0
            temp_sum = li[i]
            
        #print(i, li, counter, temp_sum, max_sum)
        max_sum = max(max_sum, temp_sum)
    
    return max_sum

def find_max_sum(li, n): 
    max_sum = -99999999999999
    #horizontal max 
    for i in li: 
        max_sum = max(max_sum, prefix_sum(i, n))
    
    #vertical max
    for i in range(n*3):
        temp_li = []
        for j in range(n*3):
            temp_li.append(li[j][i])
        max_sum = max(max_sum, prefix_sum(temp_li, n))
        
    #diagonal left to right max 
    for i in range(n*3): 
        temp_li = []
        for j in range(n*3):
            if(j+i>=n*3): 
                break
            else:
                temp_li.append(li[j][j+i])
        if (len(temp_li) >= n): 
            max_sum = max(max_sum, prefix_sum(temp_li, n))
        
    for i in range(1, n*3):
        temp_li = []
        for j in range(n*3): 
            if(j+i>=n*3): 
                break
            else:
                temp_li.append(li[j+i][j])
        if (len(temp_li) >= n): 
            max_sum = max(max_sum, prefix_sum(temp_li, n))
        
    #diagonal right to left max
    for i in range(n*3-1, -1, -1): 
        temp_li = []
        for j in range(n*3):
            if(i-j<0): 
                break
            else:
                temp_li.append(li[j][i-j])
        if (len(temp_li) >= n): 
            max_sum = max(max_sum, prefix_sum(temp_li, n))
            
    for i in range(n*3-1, -1, -1): 
        temp_li = []
        for j in range(1, n*3):
            #print(j, i-j+1)
            if(i-j<0): 
                break
            else:
                temp_li.append(li[j][i-j+1])
        if (len(temp_li) >= n): 
            max_sum = max(max_sum, prefix_sum(temp_li, n))

    return max_sum
    
print(find_max_sum(li, n))
