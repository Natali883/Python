def display_quote():
    quote = "“Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.”\nBill Gates"
    print(quote)

display_quote()


def display_even_numbers(num1, num2):
    start = min(num1, num2)
    end = max(num1, num2)
    
    for i in range(start, end):
        if i % 2 == 0:
            print(i)

display_even_numbers(3, 10)


def draw_square(side_length, symbol, filled):
    if filled:
        for i in range(side_length):
            for j in range(side_length):
                print(symbol, end=' ')
            print()
    else:
        for i in range(side_length):
            for j in range(side_length):
                if i == 0 or i == side_length - 1 or j == 0 or j == side_length - 1:
                    print(symbol, end=' ')
                else:
                    print(' ', end=' ')
            print()


def min_of_five_numbers(num1, num2, num3, num4, num5):
    return min(num1, num2, num3, num4, num5)

result = min_of_five_numbers(10, 5, 8, 12, 3)
print(result) 


def product_in_range(start, end):
    if start > end:
        start, end = end, start
        
    result = 1
    for i in range(start, end+1):
        result *= i
    return result

result = product_in_range(2,5)
print(result) 


def count_digits(num):
    return len(str(num))

number = 3456
print(count_digits(number)) 

def is_palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    else:
        return False

print(is_palindrome(123321))  
print(is_palindrome(546645))  
print(is_palindrome(421987))  


