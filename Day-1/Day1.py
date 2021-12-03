file = open("Day1.txt")
lines = file.read().splitlines()
file.close()

def count_increases(depth_array):
    prev_count = int(depth_array[0])
    increase_in_count = 0
    for i in range(1,len(depth_array)):
        if int(depth_array[i]) > prev_count:
            increase_in_count +=1
        prev_count = int(depth_array[i])    
    return increase_in_count



def count_increases_three_measurement(depth_array):
    count = 0
    prev_total = 0
    for i in range(1,len(depth_array)-2):
        new_total = int(depth_array[i]) + int(depth_array[i+1]) + int(depth_array[i+2]) 
    
        if (new_total > prev_total):
            count += 1
        prev_total = new_total
        
    return count-1


print(count_increases(lines))
print(count_increases_three_measurement(lines))   
            
