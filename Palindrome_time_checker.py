"""
Alongside determining whather an input is palindrome or not, 
the program calcultes the time taken for the process to be completed
"""
from time import perf_counter
input_string = input(
    'Please enter anything,the program will check wheather it\'s a palindrome or not.\n')
start = perf_counter()
if input_string == input_string[::-1]:
    print("This is a palindrome.")
else:
    print('This is not a palindrome.')
end = perf_counter()
print(f"Taken time = {end-start}")
