
# is_two is defining a single parameter
def is_two(number):
    # checking if number equals 2 or two. If there is a match then the return is True. Otherwise return is False
    return number == 2 or str(number.lower()) == 'two'

def is_two(string):
    return string == 2 or string == '2'




# is_vowel is defining a single parameter
def is_vowel(input):
    # Next, we are defining a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Next, we are converting input to lowercase and checking if its in vowel list. Returns True or False
    return input.lower() in vowels


# is_consonant is defining a single parameter
def is_consonant(input):
    # Utilizing is_vowel, we are using 'not' to check if input is letter other than vowel. Returns True or False.
    return not is_vowel(input)



# cap_consonant is defining a single string
def cap_consonant(string):
    # Checking to see if the first letter of string is a consonant using is_consonant function
    if is_consonant(string[0]):
        # If the first letter is a consonant, we are capitalizing first letter of string
        return str.capitalize(string)
    # If the first letter is NOT a consonant, we are simply sending back the string as is
    return string



# Takes in 2 arguments, tip_percentage and bill_total
def calculate_tip(tip_percentage, bill_total):
    # reminding user to enter percentage as a decimal
    '''
    Enter tip_percentage as a decimal between 0 and 1
    '''
    # We are multiplying tip_percentage and bill_total to calculate tip amount
    return tip_percentage * bill_total





# takes in 2 arguments, discount_percentage and original_price
def apply_discount(discount_percentage, original_price):
    # reminding user to enter percentage as a decimal
    '''
    Enter discount_percentage as a decimal between 0 and 1
    '''
    # We are taking the original price then subtracting discount amount to get price after the discount is applied
    return original_price - (original_price * discount_percentage)




# taking in 1 argument
def handle_commas(input):
    # First, we are replacing any commas with nothing eliminating all comma's
    # Then we are converting the string to a number using int()
    return int(input.replace(",",""))





# taking in 1 argument
def get_letter_grade(input):
    # We are then checking a series of grade ranges.
    # Once our input matches a range, we return the assosiated letter.
    if input > 89:
        return 'A'
    elif input > 79:
        return 'B'
    elif input > 69:
        return 'C'
    elif input > 59:
        return 'D'
    else:
        return 'F'





# taking in 1 argument
def remove_vowels(input):
    # We created a list of vowels
    vowels = 'aeiouAEIOU'
    # Used list of comprehension to create a new list of character from the input string
    # Only included letters that are not in the vowel string we created
    # joined the list of consonants back together in a string using join() method
    return ''.join([char for char in input if char not in vowels])


def remove_vowels(string):
    new_string = ''
    for char in string:
        if not is_vowel(char):
            new_string += char
    return new_string







# Taking in 1 argument
def normalize_name(input):
    # Removes invalid characters
    name = ''.join(char for char in input if char.isalnum() or char == ' ')
    # Removes leading and trailing white space
    name = name.strip()
    # Converts to lowercase
    name = name.lower()
    # Replaces spaces with underscores
    name = name.replace(' ', '_')
    # Removes leading underscores
    while name.startswith('_'):
        name = name[1:]
    # Returns final name
    return name


def normalize_name(string):
    string = string.strip().lower().replace(' ','')
    
    new_string = ''
    
    for char in string:
        if char.isalpha() or char.isdigit() or char == '_':
            new_string += char
    new_string = new_string.strip('_')
    
    return new_string










# takes in a list of numbers argument
def cumulative_sum(inputs):
    # We created an empty list to hold our cumulative sums
    cumulative_sums = []
    # created a variable to to track total_sum
    total_sum = 0
    # loop through each input in the list of inputs 
    for input in inputs:
        # add the current input to the total_sum
        total_sum += input
        # Append the current total sum to the list of cumulative sums
        cumulative_sums.append(total_sum)
    # Returned the list of cumulative sums
    return cumulative_sums












