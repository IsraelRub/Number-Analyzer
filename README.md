
[Start] -> [Print Welcome Message]
           |
           v
[Get Action] -> [Get Numbers] -> [Get Display (if list)]
           |
           v
[Number Analysis Hub]
           |
           v
[Is input a list?] --Yes--> [Print to List]
           |                      |
           No                     v
           |             [For each number or block]
           v                      |
[Is input a dict?] --Yes-->       |
           |                      |
           No                     |
           |                      |
           v                      v
[Print to Single] <---------------+
           |
           v
[Classify Number]
           |
           v
[Is number composite?] --No--> [Print Type]
           |
           Yes
           |
           v
[Execute Number Action]
           |
           v
[Create Primes Factors List]
           |
           v
[Create Prime by Power Structure] --(if needed)
           |
           v
[Create Divisors List] --(if needed)
           |
           v
[Calculate Multiplicative Combinations] --(if needed)
           |
           v
[Print Results]
           |
           v
[End]

==========
with class
==========

main()
|
├── InputHandler.get_user_input()
|   |
|   ├── get_action()
|   |
|   ├── get_numbers()
|   |   |
|   |   ├── safe_number_input()  (if user enters '1')
|   |   |
|   |   ├── [safe_number_input() for i in range(...)]  (if user enters a number > 1)
|   |   |
|   |   └── get_range()  (if user enters '0' or 'range')
|   |       └── safe_number_input()  (for start, end, step)
|   |
|   └── get_display()  (if numbers is a list)
|
└── NumberAnalysis.number_analysis_hub(numbers, action, display)
    |
    ├── classify_number(numbers)
    |
    ├── print_to_list()  (if numbers is a list)
    |   |
    |   ├── flatten_list()
    |   |   └── (possible recursion)
    |   |
    |   ├── object_to_str()
    |   |
    |   ├── print_to_single()  (if display='each')
    |   |   |
    |   |   ├── classify_number()
    |   |   |
    |   |   └── execute_number_action()
    |   |       |
    |   |       ├── create_primes_factors_list()
    |   |       |
    |   |       ├── create_prime_by_power_structure()
    |   |       |
    |   |       ├── create_divisors_list()
    |   |       |
    |   |       └── calculate_multiplicative_combinations()
    |   |
    |   └── create_action_results_dict()  (if display='block')
    |       |
    |       ├── classify_number()
    |       |
    |       └── execute_number_action()
    |           |
    |           ├── create_primes_factors_list()
    |           |
    |           ├── create_prime_by_power_structure()
    |           |
    |           ├── create_divisors_list()
    |           |
    |           └── calculate_multiplicative_combinations()
    |
    ├── number_analysis_hub()  (recursion if numbers is a dictionary)
    |
    └── print_to_single()  (if numbers is a single number)
        |
        ├── classify_number()
        |
        └── execute_number_action()
            |
            ├── create_primes_factors_list()
            |
            ├── create_prime_by_power_structure()
            |
            ├── create_divisors_list()
            |
            └── calculate_multiplicative_combinations()

=====================
class with hind type:
=====================

main() -> None
|
├── InputHandler.get_user_input() -> Tuple[Union[int, float, List[Union[int, float]]], str, Optional[str]]
|   |
|   ├── get_action() -> str
|   |
|   ├── get_numbers() -> Union[int, float, List[int]]
|   |   |
|   |   ├── safe_number_input(prompt: str) -> Union[int, float]
|   |   |
|   |   ├── [safe_number_input() for i in range(...)]
|   |   |
|   |   └── get_range() -> Union[int, List[int]]
|   |       └── safe_number_input(prompt: str) -> Union[int, float]
|   |
|   └── get_display() -> str
|
└── NumberAnalysis.number_analysis_hub(numbers: Any, action: str, display: Optional[str] = None) -> str
    |
    ├── classify_number(number: Any) -> str
    |
    ├── print_to_list(list_of_numbers: List[int], action: str, display: str) -> None
    |   |
    |   ├── flatten_list(nested_list: List[Union[T, List[T]]]) -> List[T]
    |   |
    |   ├── object_to_str(obj: Union[list, dict]) -> str
    |   |
    |   ├── print_to_single(number: int, action: str) -> str
    |   |   |
    |   |   ├── classify_number(number: Any) -> str
    |   |   |
    |   |   └── execute_number_action(number: int, action: str) -> Union[List[int], str]
    |   |
    |   └── create_action_results_dict(numbers: Union[int, List[int]], action: str) -> Dict[str, Any]
    |       |
    |       ├── classify_number(number: Any) -> str
    |       |
    |       └── execute_number_action(number: int, action: str) -> Union[List[int], str]
    |
    ├── number_analysis_hub() (recursion if numbers is a dictionary)
    |
    └── print_to_single(number: int, action: str) -> str
        |
        ├── classify_number(number: Any) -> str
        |
        └── execute_number_action(number: int, action: str) -> Union[List[int], str]
            |
            ├── create_primes_factors_list(number: int) -> List[int]
            |
            ├── create_prime_by_power_structure(factors_list: List[int]) -> List[str]
            |
            ├── create_divisors_list(multiplicative_structure: List[str]) -> List[int]
            |
            └── calculate_multiplicative_combinations(divisors: List[int]) -> List[str]


==============
without class:
==============

main()
|
├── get_user_input()
|   |
|   ├── get_action()
|   |
|   ├── get_numbers()
|   |   |
|   |   ├── safe_number_input()  (if user enters '1')
|   |   |
|   |   ├── [safe_number_input() for i in range(...)]  (if user enters a number > 1)
|   |   |
|   |   └── get_range()  (if user enters 'range')
|   |       └── safe_number_input()  (multiple times)
|   |
|   └── get_display()  (if numbers is a list)
|
└── number_analysis_hub(numbers, action, display)
    |
    ├── classify_number(numbers)
    |
    ├── print_to_list()  (if numbers is a list)
    |   |
    |   ├── flatten_list()
    |   |   └── (possible recursion)
    |   |
    |   ├── object_to_str()
    |   |
    |   ├── print_to_single()  (if display='each')
    |   |   |
    |   |   ├── classify_number()
    |   |   |
    |   |   ├── format_action_result()
    |   |   |   |
    |   |   |   ├── create_primes_factors_list()
    |   |   |   |
    |   |   |   ├── create_multiplicative_structure()
    |   |   |   |
    |   |   |   ├── create_divisors_list()
    |   |   |   |
    |   |   |   └── calculate_multiplicative_combinations()
    |   |   |
    |   |   └── object_to_str()
    |   |
    |   └── create_action_results_dict()  (if display='block')
    |       |
    |       ├── classify_number()
    |       |
    |       └── format_action_result()
    |           |
    |           ├── create_primes_factors_list()
    |           |
    |           ├── create_multiplicative_structure()
    |           |
    |           ├── create_divisors_list()
    |           |
    |           └── calculate_multiplicative_combinations()
    |
    ├── number_analysis_hub()  (recursion if numbers is a dictionary)
    |
    └── print_to_single()  (if numbers is a single number)
        |
        ├── classify_number()
        |
        ├── format_action_result()
        |   |
        |   ├── create_primes_factors_list()
        |   |
        |   ├── create_multiplicative_structure()
        |   |
        |   ├── create_divisors_list()
        |   |
        |   └── calculate_multiplicative_combinations()
        |
        └── object_to_str()


================
with hind type:
================

main() -> None
|
├── get_user_input() -> Tuple[Union[int, float, List[Union[int, float]]], str, Optional[str]]
|   |
|   ├── get_action() -> str
|   |
|   ├── get_numbers() -> Union[int, float, List[int]]
|   |   |
|   |   ├── safe_number_input(str) -> Union[int, float]  (if user enters '1')
|   |   |
|   |   ├── [safe_number_input(str) for i in range(...)]  (if user enters a number > 1)
|   |   |
|   |   └── get_range() -> Union[int, List[int]]  (if user enters 'range')
|   |       └── safe_number_input(str) -> Union[int, float]  (multiple times)
|   |
|   └── get_display() -> str  (if numbers is a list)
|
└── number_analysis_hub(Any, str, Optional[str]) -> str
    |
    ├── classify_number(Any) -> str
    |
    ├── print_to_list(List[int], str, str) -> None  (if numbers is a list)
    |   |
    |   ├── flatten_list(List[Union[T, List[T]]]) -> List[T]
    |   |   └── (possible recursion)
    |   |
    |   ├── object_to_str(Union[list, dict]) -> str
    |   |
    |   ├── print_to_single(int, str) -> str  (if display='each')
    |   |   |
    |   |   ├── classify_number(Any) -> str
    |   |   |
    |   |   ├── create_action_results_dict(Union[int, List[int]], str) -> Dict[str, Any]
    |   |   |   |
    |   |   |   ├── classify_number(Any) -> str
    |   |   |   |
    |   |   |   └── format_action_result(int, str) -> Union[List[int], str]
    |   |   |       |
    |   |   |       ├── create_primes_factors_list(int) -> List[int]
    |   |   |       |
    |   |   |       ├── create_multiplicative_structure(List[int]) -> List[str]
    |   |   |       |
    |   |   |       ├── create_divisors_list(List[str]) -> List[int]
    |   |   |       |
    |   |   |       └── calculate_multiplicative_combinations(List[int]) -> List[str]
    |   |   |
    |   |   └── object_to_str(Union[list, dict]) -> str
    |   |
    |   └── create_action_results_dict(Union[int, List[int]], str) -> Dict[str, Any]  (if display='block')
    |       |
    |       ├── classify_number(Any) -> str
    |       |
    |       └── format_action_result(int, str) -> Union[List[int], str]
    |           |
    |           ├── create_primes_factors_list(int) -> List[int]
    |           |
    |           ├── create_multiplicative_structure(List[int]) -> List[str]
    |           |
    |           ├── create_divisors_list(List[str]) -> List[int]
    |           |
    |           └── calculate_multiplicative_combinations(List[int]) -> List[str]
    |
    ├── number_analysis_hub(Any, str, Optional[str]) -> str  (recursion if numbers is a dictionary)
    |
    └── print_to_single(int, str) -> str  (if numbers is a single number)
        |
        ├── classify_number(Any) -> str
        |
        ├── create_action_results_dict(Union[int, List[int]], str) -> Dict[str, Any]
        |   |
        |   ├── classify_number(Any) -> str
        |   |
        |   └── format_action_result(int, str) -> Union[List[int], str]
        |       |
        |       ├── create_primes_factors_list(int) -> List[int]
        |       |
        |       ├── create_multiplicative_structure(List[int]) -> List[str]
        |       |
        |       ├── create_divisors_list(List[str]) -> List[int]
        |       |
        |       └── calculate_multiplicative_combinations(List[int]) -> List[str]
        |
        └── object_to_str(Union[list, dict]) -> str



The provided Python code is a collection of functions designed to perform various operations related to prime number analysis and number type identification. The code offers functionalities such as checking if a number is prime, finding the prime factorization of a number, representing prime factorizations with exponents, classifying numbers based on their types, and printing comprehensive information about the input numbers.

1. `is_number_prime(number)`:
   - This function takes an integer `number` as input and determines whether it is a prime number or not.
   - It iterates through the range of potential factors from 2 to the square root of the given number (inclusive).
   - If any factor within this range evenly divides the number, it means the number is not prime, and the function returns the string `'is not prime'`.
   - If no such factor is found, it implies that the number is prime, and the function returns the string `'is prime'`.

2. `get_number_type(number)`:
   - This function takes a `number` as input, which can be an integer, float, string, list, or dictionary.
   - It determines the type of the input and returns a corresponding string indicating its type.
   - If the input is an integer, float, or string representing a number, it checks if the number is prime, a float or negative number, or not a number at all.
   - For lists and dictionaries, it simply returns the respective strings `'is a list'` or `'is a dict'`.
   - If the input is none of the above types, it returns the string `'is invalid'`.

3. `create_singles_primes_list(number)`:
   - This function takes a `number` (integer or float) as input and returns a list of its prime factors.
   - It iteratively divides the input number by its prime factors, starting with 2 and then checking for odd factors up to the square root of the number.
   - Each prime factor is appended to a list, and the process continues until the number becomes 1.
   - The final list containing all the prime factors of the input number is returned.

4. `create_powers_primes_list(prime_list)`:
   - This function takes a list of prime factors `prime_list` as input and returns a list of prime factors represented with their powers (exponents).
   - It iterates through the input list and counts the consecutive occurrences of each prime factor.
   - If a prime factor appears only once, it is added to the output list as is.
   - If a prime factor appears multiple times consecutively, it is represented as a string with the prime factor raised to the power of the count (e.g., `'2^3'`).

5. `create_singles_primes_dict(numbers)`:
   - This function takes a list of `numbers` (integers, floats, or strings representing numbers) as input and returns a dictionary.
   - The keys of the dictionary are the input numbers, and the values are lists of their prime factors.
   - For each number in the input list, it determines the number type using the `get_number_type` function.
   - If the number is not prime, it computes its prime factors using the `create_singles_primes_list` function and stores them as the value in the dictionary.
   - If the number is prime or of another type (float, negative, list, dict, or not a number), the corresponding string representation is stored as the value.

6. `create_powers_primes_dict(numbers)`:
   - This function is similar to `create_singles_primes_dict`, but instead of storing lists of prime factors as values, it stores lists of prime factors represented with their powers (exponents).
   - It follows the same logic as `create_singles_primes_dict` but uses the `create_powers_primes_list` function to generate the list of prime factors with powers for each non-prime number.

7. `create_types_dict(numbers)`:
   - This function takes a list of `numbers` (integers, floats, strings, lists, or dictionaries) as input and returns a dictionary.
   - The keys of the resulting dictionary are strings representing the types of numbers in the input list (e.g., `'primes'`, `'floats or negative numbers'`, `'lists'`, `'dicts'`, or `'not numbers'`).
   - The values are lists of numbers from the input list that belong to the corresponding type.

8. `function_printer(numbers)`:
   - This function takes `numbers` as input, which can be an integer, float, string, list, or dictionary.
   - It handles different types of inputs and calls other functions to compute and print information about prime factors, powers of prime factors, and types of numbers.
   - For single numbers (integers or floats), it prints the several prime factors, the list of prime factors, and the list of prime factors with powers.
   - For lists, it iterates through each element and calls `function_printer` recursively for each element.
   - Additionally, it prints the dictionaries returned by `create_singles_primes_dict`, `create_powers_primes_dict`, and `create_types_dict` for the input list.
   - For dictionaries, it iterates through each key-value pair and calls `function_printer` recursively for each value.
   - If the input is invalid or an unsupported type, it prints an appropriate message.

9. `input_list()`:
   - This function prompts the user to enter a list of numbers or a range of numbers.
   - If the user enters a digit, it prompts for individual numbers and creates a list of those numbers.
   - If the user enters the word `'range'`, it prompts for start, stop, and step values and creates a list using the `range` function.
   - If the input is invalid, it returns an empty list.

10. `main()`:
    - This is the main function that runs the program.
    - Currently, it creates a list of numbers using the `range` function with specific start, stop, and step values.
    - It then calls the `function_printer` function with the generated list of numbers.

The functions in this code are designed to work together to analyze numbers, find their prime factorizations, determine their types, and provide various representations of the prime factorizations and types of numbers. The `main` function serves as the entry point, and the `function_printer` function orchestrates the execution of other functions based on the input type.

The code provides a comprehensive set of functionalities for prime number analysis and number type identification. It allows users to input numbers or lists of numbers and obtain detailed information about their prime factorizations, with options to represent the factorizations as lists of prime factors or lists of prime factors with powers (exponents). Additionally, the code classifies the input numbers based on their types (prime, float, negative, list, dictionary, or non-number) and provides a dictionary mapping the types to the corresponding numbers.

Overall, this Python code demonstrates a well-structured approach to handling prime number analysis and number type identification tasks, leveraging various functions and data structures to achieve the desired functionality.
'''

'''
def is_number_prime(number):
    """
    Checks if a given number is prime or not.

    Args:
        number (int): The number to be checked for primality.

    Returns:
        str: 'is prime' if the number is prime, 'is not prime' otherwise.

    This function takes an integer number as input and determines whether it is a prime number or not. It does this by iterating through a range of potential factors from 2 to the square root of the number (inclusive). For each factor in this range, it checks if the number is divisible by that factor using the modulo operator (%). If the number is divisible by any factor in this range (i.e., the remainder is zero), it means the number is not prime, and the function immediately returns the string 'is not prime'.

    If the loop completes without finding any factor that divides the number, it implies that the number is prime, and the function returns the string 'is prime'.

    The reason for checking factors only up to the square root of the number is based on the mathematical principle that if a number has a factor greater than its square root, it must also have a corresponding factor less than its square root. This optimization reduces the number of iterations required to determine primality, making the function more efficient.

    For example, if we want to check if the number 21 is prime, the function will iterate through the factors 2, 3, 4, 5, 6, and 7 (the square root of 21 is approximately 4.58). Since 21 is divisible by 3 and 7, the function will return 'is not prime' after encountering the factor 3. On the other hand, if we check the number 17, the function will iterate through the factors 2, 3, 4, and 5 (the square root of 17 is approximately 4.12), and since none of these factors divides 17, it will return 'is prime'.
    """

def get_number_type(number):
    """
    Determines the type of the given value and returns a corresponding string.

    Args:
        number (int/float/str/list/dict): The value to be checked.

    Returns:
        str: A string describing the type of the input value.

    This function takes a value of various types (integer, float, string, list, or dictionary) as input and returns a string describing the type of the input value. It performs different checks and operations based on the type of the input.

    If the input is an instance of int, float, or str, the function converts the input to a string and performs the following checks:

    1. If the string consists entirely of digits, it converts it to an integer and calls the is_number_prime function to check if it's prime or not. If the number is prime, it returns 'is prime'; otherwise, it returns 'is not prime'.

    2. If the string contains a decimal point, it splits the string into two parts (before and after the decimal point) using the split() method. It then checks the following conditions:
        a. If the part after the decimal point consists entirely of zeros, and the part before the decimal point is either a valid integer or a valid positive integer (excluding negative signs), it converts the string to a float and calls the is_number_prime function to check if it's prime or not. If the number is prime, it returns 'is prime'; otherwise, it returns 'is neither prime nor odd'.
        b. If the part after the decimal point does not consist entirely of zeros, it returns 'is neither prime nor odd'.

    3. If the string starts with a negative sign and the remaining part (excluding the negative sign and the decimal point, if present) consists entirely of digits, it returns 'is neither prime nor odd'.

    4. If none of the above conditions are met, it returns 'is invalid'.

    If the input is an instance of list, it returns 'is a list'. If the input is an instance of dict, it returns 'is a dict'. If the input is none of the above types, it returns 'is invalid'.

    This function is used throughout the code to ensure that the operations are performed on the correct type of data and to classify the input values based on their types.
    """

def create_singles_primes_list(number):
    """
    Finds the prime factorization of a given number and returns a list of its prime factors.

    Args:
        number (int/float): The number to be factored into primes.

    Returns:
        list: A list of the prime factors of the input number.

    This function takes a number (int or float) as input and returns a list of its prime factors. It follows these steps:

    1. First, it converts the input number to an integer by casting it to int(float(number)). This step ensures that any fractional part is removed, even if the input is a float.

    2. It initializes an empty list called singles_prime_list to store the prime factors.

    3. It enters a while loop that repeatedly divides the number by 2 and appends 2 to the singles_prime_list until the number is no longer divisible by 2. This step effectively removes all occurrences of the prime factor 2 from the number.

    4. After removing all occurrences of 2, it enters a for loop that iterates over the range of odd numbers from 3 to the square root of the number (inclusive), with a step size of 2. This step is necessary because we've already handled the case of 2 in the previous step.

    5. Inside this loop, it enters another while loop that repeatedly divides the number by the current odd factor and appends that factor to the singles_prime_list until the number is no longer divisible by that factor. This step effectively removes all occurrences of that prime factor from the number.

    6. After the outer loop finishes, if the remaining number is greater than 1, it means that the number itself is a prime factor, so it appends the remaining number to the singles_prime_list.

    7. Finally, it returns the singles_prime_list containing all the prime factors of the input number.

    This function is an efficient way to factorize a number into primes because it only checks factors up to the square root of the number. This optimization is based on the mathematical principle that if a number has a prime factor greater than its square root, it must also have a corresponding prime factor less than its square root.
    """

def create_powers_primes_list(prime_list):
    """
    Takes a list of prime factors and returns a list of prime factors with their powers (exponents).

    Args:
        prime_list (list): A list of prime factors.

    Returns:
        list: A list of the prime factors with their powers.

    This function takes a list of prime factors as input and returns a new list where consecutive occurrences of the same prime factor are represented as a power (exponent). It follows these steps:

    1. It initializes an empty list called powers_primes_list to store the prime factors with their powers.

    2. It initializes a variable i to 0, which will be used as an index to iterate over the input prime_list.

    3. It enters a while loop that continues until i is greater than or equal to the length of the prime_list.

    4. Inside the loop, it counts the number of consecutive occurrences of the current prime factor (prime_list[i]) using the count() method.

    5. If the count is 1, it means the prime factor appears only once, so it appends the prime factor to the powers_primes_list as is.

    6. If the count is greater than 1, it creates a string representation of the prime factor raised to the power of the count (e.g., '2^3' for 2 appearing 3 times consecutively) and appends it to the powers_primes_list.

    7. It then updates the index i by adding the count to it. However, if the count is greater than 1, it subtracts 1 from the count before adding it to i. This step is necessary to skip over the consecutive occurrences of the prime factor that have already been accounted for.

    8. After the loop finishes, it returns the powers_primes_list containing the prime factors with their powers.

    This function provides a compact representation of the prime factors of a number by showing their powers (exponents), making it easier to analyze and work with the prime factorization.
    """

def create_singles_primes_dict(numbers):
    """
    Creates a dictionary mapping each number to a list of its prime factors (without powers).

    Args:
        numbers (list): A list of numbers (int/float/str).

    Returns:
        dict: A dictionary where the keys are the input numbers, and the values are lists of their prime factors (without powers).

    This function takes a list of numbers as input and returns a dictionary where the keys are the numbers from the input list, and the values are lists of their prime factors (without powers). Here's how it works:

    1. It initializes an empty dictionary called primes_dict to store the mapping of numbers to their prime factors.

    2. It iterates over each num in the input list of numbers.

    3. For each num, it calls the get_number_type function to determine the type of the number.

    4. If the number type is 'is not prime', it means the number is not prime, so it calls the create_singles_primes_list function to get the list of prime factors for that number.

    5. It then adds an entry to the primes_dict dictionary, where the key is the num, and the value is the list of prime factors obtained from create_singles_primes_list.

    6. If the number type is anything other than 'is not prime' (e.g., 'is prime', 'is neither prime nor odd', 'is a list', 'is a dict', or 'is invalid'), it adds an entry to the primes_dict dictionary, where the key is the num, and the value is the string representing the number type.

    7. After iterating over all the numbers, it returns the primes_dict dictionary containing the mapping of each number to its prime factors or its type.

    This function provides a convenient way to obtain the prime factorization of multiple numbers in a dictionary format, where the keys are the numbers themselves, and the values are their corresponding prime factors (for non-prime numbers) or their types (for prime numbers or other types).
    """

def create_powers_primes_dict(numbers):
    """
    Creates a dictionary mapping each number to a list of its prime factors with their powers (exponents).

    Args:
        numbers (list): A list of numbers (int/float/str).

    Returns:
        dict: A dictionary where the keys are the input numbers, and the values are lists of their prime factors with powers.

    This function is similar to create_singles_primes_dict, but instead of storing the prime factors without powers, it stores the prime factors with their powers (exponents). Here's how it works:

    1. It initializes an empty dictionary called primes_dict to store the mapping of numbers to their prime factors with powers.

    2. It iterates over each num in the input list of numbers.

    3. For each num, it calls the get_number_type function to determine the type of the number.

    4. If the number type is 'is not prime', it means the number is not prime, so it calls the create_powers_primes_list function with the result of create_singles_primes_list(num) as the argument. This gives the list of prime factors with their powers for that number.

    5. It then adds an entry to the primes_dict dictionary, where the key is the num, and the value is the list of prime factors with powers obtained from create_powers_primes_list.

    6. If the number type is anything other than 'is not prime' (e.g., 'is prime', 'is neither prime nor odd', 'is a list', 'is a dict', or 'is invalid'), it adds an entry to the primes_dict dictionary, where the key is the num, and the value is the string representing the number type.

    7. After iterating over all the numbers, it returns the primes_dict dictionary containing the mapping of each number to its prime factors with powers or its type.

    This function provides a convenient way to obtain the prime factorization of multiple numbers with their powers (exponents) in a dictionary format, where the keys are the numbers themselves, and the values are their corresponding prime factors with powers (for non-prime numbers) or their types (for prime numbers or other types).
    """

def create_types_dict(numbers):
    """
    Creates a dictionary mapping the type of number to a list of all numbers of that type.

    Args:
        numbers (list): A list of numbers (int/float/str/list/dict).

    Returns:
        dict: A dictionary mapping the type of number to a list of all numbers of that type from the input list.

    This function takes a list of numbers as input, where the numbers can be integers, floats, strings, lists, or dictionaries. It returns a dictionary where the keys are strings representing the types of numbers, and the values are lists of all numbers from the input list that belong to that type. Here's how it works:

    1. It initializes an empty dictionary called types_dict to store the mapping of number types to the corresponding numbers.

    2. It iterates over each number in the input list of numbers.

    3. For each number, it calls the get_number_type function to determine the type of the number.

    4. It constructs a string representing the type of the number by appending an 's' to the type string returned by get_number_type (e.g., 'primes', 'floats or negative numbers', 'lists', 'dicts', or 'not numbers').

    5. It uses the setdefault method of the types_dict dictionary to create a new key-value pair if the key (number type) doesn't exist in the dictionary. If the key already exists, it retrieves the existing value (a list).

    6. It appends the current number to the list associated with the corresponding number type in the types_dict dictionary.

    7. After iterating over all the numbers, it returns the types_dict dictionary containing the mapping of number types to the lists of numbers of those types.

    This function provides a convenient way to categorize and group a list of numbers based on their types, which can be useful for further analysis or processing of the numbers based on their types.
    """

def function_printer(numbers):
    """
    Prints information about the input numbers and returns the relevant information based on the type of input.

    Args:
        numbers (int/float/str/list/dict): The numbers to be analyzed and printed.

    Returns:
        bool/list/tuple: Depending on the type of input, it returns True (for successful printing), a list of prime factors, or a tuple containing the list of prime factors and the list of prime factors with powers.

    This function is the main driver that prints information about the input numbers and returns relevant information based on the type of input. Here's how it works:

    1. It calls the get_number_type function to determine the type of the input numbers.

    2. If the number type is 'is invalid', it prints a message indicating that the input is invalid and returns True.

    3. If the number type is 'is neither prime nor odd', it prints a message stating that the number is neither prime nor odd and returns True.

    4. If the number type is 'is prime', it prints a message stating that the number is prime and returns True.

    5. If the number type is 'is a dict', it recursively calls function_printer for each value in the dictionary, passing the value as the new input numbers. This allows the function to handle nested dictionaries.

    6. If the number type is 'is a list', it performs the following:
        a. If the length of the list is greater than 1, it recursively calls function_printer for each element in the list.
        b. After iterating over all elements in the list, it prints the dictionaries returned by create_singles_primes_dict, create_powers_primes_dict, and create_types_dict for the input list.
        c. If the length of the list is 1, it recursively calls function_printer with the single element in the list.
        d. If the list is empty, it prints a message indicating that the list does not contain numbers.
        e. Finally, it returns True.

   def function_printer(numbers):
    # ...
    7. If the number type is 'is not prime', it means the input is a non-prime number, so it performs the following:
        a. It calls create_singles_primes_list to get the list of prime factors for the input number.
        b. It calls create_powers_primes_list with the result from create_singles_primes_list to get the list of prime factors with powers.
        c. It prints the number of prime factors, the list of prime factors, and the list of prime factors with powers.
        d. It returns a tuple containing the list of prime factors and the list of prime factors with powers.

    This function acts as the main interface for printing information about the input numbers. It handles various types of inputs, including single numbers, lists, and dictionaries, and it recursively processes nested data structures. It leverages other functions in the code to compute the prime factorizations and present the information in a clear and organized manner.
    """

def input_list():
    """
    Prompts the user to enter a list of numbers or a range of numbers.

    Returns:
        list: A list of numbers entered by the user or a range of numbers.

    This function prompts the user to enter a list of numbers or a range of numbers through the console. Here's how it works:

    1. It prompts the user to enter the amount of numbers by displaying the message "Enter amount of numbers: ".

    2. If the user's input is a digit, it assumes that the user wants to enter individual numbers. It initializes an empty list called list_input_of_numbers to store the numbers.

    3. It enters a for loop that iterates the specified number of times based on the user's input.
        a. In each iteration, it prompts the user to enter a number by displaying the message "Enter a number: ".
        b. It appends the user's input to the list_input_of_numbers.

    4. After the loop finishes, it returns the list_input_of_numbers containing the user-entered numbers.

    5. If the user's initial input is the string 'range', it assumes that the user wants to enter a range of numbers. It prompts the user to enter the start, stop, and step values for the range.

    6. If all three inputs (start, stop, and step) are digits, it creates a list using the range() function with the specified start, stop, and step values, and returns that list.

    7. If the user's input is invalid (neither a digit nor the string 'range'), it returns an empty list.

    This function provides a convenient way for the user to input a list of numbers or a range of numbers, which can be further processed or analyzed by other functions in the code.
    """

def main():
    """
    The main function that runs the program.

    This function serves as the entry point for the program's execution. It performs the following steps:

    1. It calls the input_list() function to prompt the user to enter a list of numbers or a range of numbers.

    2. It stores the result of input_list() (a list of numbers) in the variable numbers.

    3. It calls the function_printer function, passing the numbers list as an argument.

    The function_printer function is responsible for printing information about the input numbers, including their prime factorizations, prime factorizations with powers, and categorization based on their types.

    By default, the main function uses the user-provided list of numbers or range as input. However, it can be modified to use a predefined list of numbers or read input from a file or any other source, as required.

    This function serves as the central point of execution, coordinating the input collection and subsequent processing and printing of information about the numbers.
    """

if __name__ == '__main__':
    main()
