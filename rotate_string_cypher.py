
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

#list of alphabetic characters
u = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = len(l)

def rotationalCipher(input, rotation_factor):
    output = []
    for i in input:
        if i in l:
            output.append(l[(l.index(i) + rotation_factor) % n])
        elif i in u:
            output.append(u[(u.index(i) + rotation_factor) % n])
        elif i.isdigit():
            new_digit = (int(i) + rotation_factor)%10
            output.append(str(new_digit))            
        else:
            output.append(i)

    return ''.join(output)

input_1 = "All-convoYs-9-be:Alert1."
rotation_factor_1 = 4
expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
output_1 = rotationalCipher(input_1, rotation_factor_1)
print("Expected: " + expected_1 + " Output: " + output_1)

input_2 = "abcdZXYzxy-999.@"
rotation_factor_2 = 200
expected_2 = "stuvRPQrpq-999.@"
output_2 = rotationalCipher(input_2, rotation_factor_2)
print("Expected: " + expected_2 + " Output: " + output_2)