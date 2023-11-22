def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]


input_str_1 = "A man, a plan, a canal: Panama"
output_1 = is_palindrome(input_str_1)
print(output_1)  

input_str_2 = "race a car"
output_2 = is_palindrome(input_str_2)
print(output_2)  

input_str_3 = " "
output_3 = is_palindrome(input_str_3)
print(output_3)  

input_str_4 = " Nitin "
output_4 = is_palindrome(input_str_4)
print(output_4)

input_str_5 = " Harish "
output_5 = is_palindrome(input_str_5)
print(output_5)



