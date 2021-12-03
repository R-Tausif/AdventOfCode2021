file = open("Day3.txt")
lines = file.read().splitlines()
file.close()

def gamma_epsilon(list_of_lines):
    gamma = ""
    epsilon = ""

    line_length = len(lines[0])
   
    for i in range(line_length):
        one_count = 0
        zero_count = 0
        for line in lines:
            if line[i] == "0":
                zero_count +=1
                
            else:
                one_count +=1        
        if one_count > zero_count:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return gamma[::-1], epsilon[::-1]           # outputs the binary number in reverse order

def binary_to_decimal(my_tuple):
    decimal_value_list = []
    for bin in my_tuple:
        power = 0
        value = 0
        for i in range(len(bin)):
            if bin[i] == "1":
                value += 2**(power)
            power +=1

        decimal_value_list.append(value)
    
    return decimal_value_list[0] * decimal_value_list[1]


gamma_epsilon_result = gamma_epsilon(lines)
decimal_product = binary_to_decimal(gamma_epsilon_result)
print(decimal_product)          # part a
