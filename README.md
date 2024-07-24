# Number Cruncher

## Introduction

Welcome to the Number Cruncher! This Python program is designed to explore the fascinating world of numbers and their properties. Whether you're a math enthusiast, a student, or just curious about numbers, this tool offers a range of mathematical operations to help you understand the underlying structure and characteristics of integers.

## Features

The Number Cruncher provides a comprehensive set of mathematical operations:

1. **Type Check**
   - Determines if a number is prime, composite, or a special case.
   - Useful for understanding the fundamental nature of a number.
   - Example: Checking if 11 is prime (it is!).

2. **Prime Factorization**
   - Breaks down a number into its prime factors.
   - Reveals the building blocks of any integer.
   - Example: 12 factorizes to 2 * 2 * 3.

3. **Prime Power Structure**
   - Represents a number as a product of prime powers.
   - Provides a compact way to view the prime factorization.
   - Example: 12 can be written as 2^2 * 3^1.

4. **Divisors**
   - Lists all positive integers that divide the number without a remainder.
   - Helps in understanding the divisibility properties of a number.
   - Example: The divisors of 12 are 1, 2, 3, 4, 6, and 12.

5. **Multiplicative Combinations**
   - Shows all unique ways to express the number as a product of two factors.
   - Useful for exploring factor pairs and rectangular arrangements.
   - Example: 12 can be expressed as 1 * 12, 2 * 6, and 3 * 4.

## How to Use

1. **Starting the Program**
   - Run the `main()` function to launch the Number Cruncher.
   - You'll be greeted with a welcome message and brief instructions.

2. **Selecting an Action**
   - Choose from the five available operations (type, prime, power, divs, multi).
   - Enter either the number or the name of the action.

3. **Inputting Numbers**
   - Choose to enter individual numbers or generate a range.
   - For individual numbers:
     - Specify how many numbers you want to enter.
     - Input each number (you can use mathematical expressions like 12 * 9 or 6^8).
   - For a range:
     - Enter the start, step, and end values to generate a sequence.

4. **Choosing Display Options**
   - Select how you want to view the results:
     - 'Each': See detailed results for each number individually.
     - 'Block': View results grouped together for all numbers.

5. **Interpreting Results**
   - The program will display the results based on your chosen action and display option.
   - Results are formatted with clear bullet points and separators for easy reading.

## Code Structure

The Number Cruncher is organized into three main classes:

1. **Constants**
   - Stores all constant values used throughout the program.
   - Includes text messages, formatting styles, and bullet point characters.
   - Provides methods for consistent text formatting and error handling.

2. **NumberAnalysis**
   - Contains the core mathematical logic of the program.
   - Implements methods for number classification, prime factorization, divisor calculation, etc.
   - Handles the formatting and presentation of results.

3. **InputHandler**
   - Manages all user input operations.
   - Implements input validation to ensure robust operation.
   - Converts user input into appropriate data types for processing.

## Key Functions

- `number_analysis_hub`: The central function that coordinates the analysis based on user input.
- `classify_number`: Determines whether a number is prime, composite, or a special case.
- `execute_number_action`: Performs the selected mathematical operation on a given number.
- `print_to_single`: Formats and prints results for a single number.
- `print_to_list`: Handles the presentation of results for multiple numbers.
- `create_primes_factors_list`: Generates the list of prime factors for a number.
- `create_prime_by_power_structure`: Converts a list of prime factors into a power representation.
- `create_divisors_list`: Calculates all divisors of a number.
- `calculate_multiplicative_combinations`: Finds all ways to express a number as a product of two factors.

## Error Handling

The Number Cruncher includes comprehensive error handling:
- Invalid inputs are caught and reported with clear error messages.
- The program prompts for re-entry of data when invalid input is detected.
- Specific error messages are provided for different types of input errors (e.g., invalid number, action, or display option).

## Customization

You can easily customize the Number Cruncher:
- Modify the constants in the `Constants` class to change prompts, bullet points, or formatting styles.
- Add new mathematical operations by extending the `NumberAnalysis` class.
- Customize input handling by modifying the `InputHandler` class.

## Performance Considerations

- The program uses efficient algorithms for prime factorization and divisor calculation.
- Large numbers or extensive ranges may require longer processing times.

## Future Enhancements

Potential areas for future development include:
- Graphical user interface (GUI) for easier interaction.
- Additional mathematical operations (e.g., GCD, LCM calculation).
- Ability to save results to a file.
- Integration with plotting libraries to visualize number properties.

## Contributing

Contributions to the Number Cruncher are welcome! If you have ideas for improvements or new features:
1. Fork the repository.
2. Create a new branch for your feature.
3. Implement your changes.
4. Submit a pull request with a clear description of your modifications.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.

## Contact

For questions, suggestions, or issues, please open an issue on the GitHub repository page.

Happy number crunching!
