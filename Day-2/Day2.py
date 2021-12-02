file = open("Day2.txt")
lines = file.read().splitlines()

def submarine_position(list_of_instructions):
    horizontal_position = 0
    vertical_position = 0
    aim = 0 
    depth = 0

    for i in range(len(list_of_instructions)):
        instruction = list_of_instructions[i].split()[0]
        value = int(list_of_instructions[i].split()[1])
        
        if instruction == "forward":
            horizontal_position += value
            depth +=  aim * value
        elif instruction == "down":
            vertical_position += value
            aim += value
        elif instruction == "up":
            vertical_position -= value
            aim -= value
            
    print(horizontal_position * vertical_position)      # part a
    print(horizontal_position * depth)                  # part b


submarine_position(lines)