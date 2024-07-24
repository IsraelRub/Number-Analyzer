from typing import Any, List, Dict, Tuple, Union, Optional, Callable


class Constants:
    MAIN_BULLET = "►"
    SUB_BULLET = "•"
    RESULT_BULLET = "✅"
    EXAMPLE_BULLET = "❱"
    INPUT_BULLET = "✎"

    TEXT_STYLES = {
        "header": {
            "border_char": "▂",
            "bullet_char": "✨",
            "side_padding": 4
        },
        "subheader": {
            "border_char": "⚊",
            "bullet_char":  "❖",
            "side_padding": 2
        },
        "error": {
            "border_char": "◢",
            "bullet_char": "❌",
            "text_prefix": "ERROR: "
        }
    }

    WELCOME_MESSAGE = "Welcome to the Number Cruncher!"
    SUBTITLE_MESSAGE = f"{TEXT_STYLES['subheader']['bullet_char']} Let's explore some fascinating math tricks with numbers {
        TEXT_STYLES['subheader']['bullet_char']}"

    ACTION_PROMPT = f'''\nWhat math trick do you want to try with your numbers?
{MAIN_BULLET} 1. type:
  {SUB_BULLET} Find out if a number is prime, composite, or something special
    {EXAMPLE_BULLET} Example: Check if 11 is prime

{MAIN_BULLET} 2. prime:
  {SUB_BULLET} Break down a number into its prime building blocks
    {EXAMPLE_BULLET} Example: See that 12 = 2, 2, 3

{MAIN_BULLET} 3. power:
  {SUB_BULLET} See how a number is built from prime numbers (multiplicative structure)
    {EXAMPLE_BULLET} Example: See that 12 = 2^2 , 3^1

{MAIN_BULLET} 4. divs:
  {SUB_BULLET} List all the numbers that divide evenly into your number
    {EXAMPLE_BULLET} Example: Find that divide 12 = 2, 3, 4, 6

{MAIN_BULLET} 5. multi:
  {SUB_BULLET} Show all the ways to multiply numbers to get your number
    {EXAMPLE_BULLET} Example: See that 12 = 2 X 6, 3 X 4

{INPUT_BULLET} Please enter your choice (1-5 or the corresponding word): '''

    NUMBER_AMOUNT_PROMPT = f'''\nHow would you like to input your numbers?
{MAIN_BULLET} 1. Number
  {SUB_BULLET} Enter a single or multiple numbers
{MAIN_BULLET} 2. Range
  {SUB_BULLET} Create an automatic range of numbers

{INPUT_BULLET} Please enter your choice (1-3 or the corresponding word): '''

    DISPLAY_PROMPT = f'''\nHow would you like to view your results?
{MAIN_BULLET} 1. Each
  {SUB_BULLET} See details for each number individually
{MAIN_BULLET} 2. Block
  {SUB_BULLET} View all results grouped together

{INPUT_BULLET} Please enter your choice (Choose a number or name): '''

    ACTION_AND_DESC = {
        'type':  None,
        'prime': "prime factors",
        'power': "prime factors by power",
        'divs':  "divisors",
        'multi': "multiplicative combinations"
    }

    DISPLAY_TYPES = {'each', 'block', None}

    ENTER_RANGE_PROMPT = f"{
        INPUT_BULLET} Enter the {{}} of the range (you can use math expressions): "
    NUMBER_INPUT_PROMPT = f"{
        INPUT_BULLET} Enter {{}} (feel free to use math expressions, e.g., 12 X 9, 6^8): "
    INVALID_INPUT_MESSAGE = "Oops! That's not a valid {}. Let's give it another"

    RANGE_ZERO_STEP_ERROR = "The step cannot be zero. Please choose a non-zero value"
    RANGE_EMPTY_ERROR = "The range is empty. Please ensure the start, end, and step create a valid range"

    @staticmethod
    def print_formatted(text: str, style_name: str = "header") -> None:

        style_config = Constants.TEXT_STYLES[style_name]
        formatted_text = f"{style_config.get('text_prefix', '')}{text}"
        total_line_length = len(formatted_text) + style_config.get("side_padding", 0) * 2

        if style_name == "error":
            border_line = f"{style_config['border_char']}  " * ((total_line_length // 3) + 2)
        else:
            border_line = style_config['border_char'] * total_line_length

        print(f"\n{border_line}")
        print(f"{style_config['bullet_char']} {
              formatted_text} {style_config['bullet_char']}")
        print(border_line)

    @staticmethod
    def handle_error(error_message: str) -> None:
        Constants.print_formatted(error_message, "error")


class NumberAnalysis:
    def __init__(self):
        self.smallest_factor = None

    def number_analysis_hub(self, numbers: Any, action: str, display: Optional[str] = None) -> str:
        if action not in Constants.ACTION_AND_DESC:
            Constants.print_formatted("Enter a valid action", "error")
            return "Invalid action"

        if display not in Constants.DISPLAY_TYPES:
            Constants.print_formatted("Enter a valid display", "error")
            return "Invalid display"

        number_type = self.classify_number(numbers)

        match number_type:
            case 'is a list':
                self.print_to_list(numbers, action, display)
                return number_type

        self.print_to_single(numbers, action)
        return number_type

    def classify_number(self, number: Any) -> str:
        if isinstance(number, (int, float)):
            if not (number).is_integer() or number <= 1:
                return 'not applicable for primality'
            if number % 2 == 0 and number != 2:
                return 'is composite'
            for factor in range(3, int(number ** 0.5) + 1, 2):
                if (number % factor) == 0:
                    self.smallest_factor = factor
                    return 'is composite'
            return 'is prime'
        if isinstance(number, list):
            return 'is a list'

        return 'is invalid'

    def create_action_results_dict(self, numbers: Union[int, List[int]], action: str) -> Dict[str, Any]:
        numbers_dict = {}
        not_relevants_dict = {}

        for number in numbers:
            number_type = self.classify_number(number)

            if number_type == 'is composite':
                result = self.execute_number_action(number, action)
                numbers_dict[number] = result

            else:
                not_relevants_dict.setdefault('Irrelevant', []).append(number)

        return not_relevants_dict | numbers_dict

    def create_type_dict(self, list_of_numbers: List[int]) -> Dict[str, List[int]]:
        type_dict = {}
        for number in list_of_numbers:
            number_type = self.classify_number(number)
            type_dict.setdefault(f"{number_type} numbers", []).append(number)
        return type_dict

    def execute_number_action(self, number: int, action: str) -> Union[List[int], str]:
        match action:
            case 'prime':
                return self.create_primes_factors_list(number)

            case 'power':
                return self.create_prime_by_power_structure(self.create_primes_factors_list(number))

            case 'divs':
                return self.create_divisors_list(self.create_prime_by_power_structure(self.create_primes_factors_list(number)))

            case 'multi':
                return self.calculate_multiplicative_combinations(self.create_divisors_list(self.create_prime_by_power_structure(self.create_primes_factors_list(number))))
        return f"{Constants.RESULT_BULLET} Invalid action: {action} {Constants.RESULT_BULLET}"

    def print_to_single(self, number: int, action: str) -> str:
        number_type = self.classify_number(number)

        if action == 'type' or number_type != 'is composite':
            print(f"\n{Constants.RESULT_BULLET} The number {
                  number} {number_type}")
            return number_type

        description = Constants.ACTION_AND_DESC[action]
        action_results = self.execute_number_action(number, action)
        print(f"\n{Constants.RESULT_BULLET} For the number {number}:")
        print(f"  {Constants.SUB_BULLET} Number of {
              description}: {len(action_results)}")
        print(f"  {Constants.SUB_BULLET} List of {description}: {
              self.object_to_str(action_results)}")

        return number_type

    def print_to_list(self, list_of_numbers: List[int], action: str, display: str) -> None:

        if len(list_of_numbers) > 1:
            Constants.print_formatted("Results", "header")
            print(f"Numbers: {self.object_to_str(list_of_numbers)}\n")

            match display:
                case 'each':
                    for number in list_of_numbers:
                        self.print_to_single(number, action)

                case 'block':

                    results = self.create_action_results_dict(
                        list_of_numbers, action) if action != 'type' else self.create_type_dict(list_of_numbers)
                    for key, value in results.items():
                        print(f"\t{Constants.RESULT_BULLET} {
                              key}: {self.object_to_str(value)}")

                case _:
                    Constants.print_formatted("Enter a valid display", "error")

        elif len(list_of_numbers) == 1:
            self.print_to_single(list_of_numbers[0], action)

        else:
            Constants.print_formatted("It does not contain numbers", "error")
        return

    def create_primes_factors_list(self, number: int) -> List[int]:
        factors_list = []
        while number % 2 == 0:
            factors_list.append(2)
            number //= 2
        start = self.smallest_factor if self.smallest_factor else 3
        for factor in range(start, int(number ** 0.5) + 1, 2):
            while number % factor == 0:
                factors_list.append(factor)
                number //= factor
        if number > 1:
            factors_list.append(number)
        return factors_list

    create_prime_by_power_structure: Callable[[List[int]], List[str]] = staticmethod(
        lambda factors_list: [f"{factor}^{factors_list.count(factor)}" for factor in set(factors_list)])

    @staticmethod
    def create_divisors_list(multiplicative_structure: List[str]) -> List[int]:
        divisors = {1}
        for factor in multiplicative_structure:
            prime, power = map(int, factor.split('^'))
            temp_divisors = set()
            for i in range(power + 1):
                temp_divisors.update(
                    {divisor * prime ** i for divisor in divisors})
            divisors = temp_divisors
        return sorted(divisors)[1:-1]

    calculate_multiplicative_combinations: Callable[[List[int]], List[str]] = staticmethod(
        lambda divisors: [f"{divisors[i]} X {divisors[-1-i]}" for i in range(1, len(divisors) // 2 + (len(divisors) % 2))])

    object_to_str: Callable[[Union[list, dict]], str] = staticmethod(
        lambda obj: str(obj)[1:-1].replace("'", ""))


class InputHandler:
    @staticmethod
    def get_user_input() -> Tuple[Union[int, float, List[Union[int, float]]], str, Optional[str]]:
        action = InputHandler.get_action()
        numbers = InputHandler.get_numbers()
        display = InputHandler.get_display() if isinstance(numbers, list) else None
        return numbers, action, display

    @staticmethod
    def safe_number_input(prompt: str) -> Union[int, float]:
        while True:
            user_input = input(prompt).upper().replace(
                'X', '*').replace('^', '**')
            try:
                return eval(user_input) if isinstance(user_input, float) and not user_input.is_integer() else int(eval(user_input))
            except:
                Constants.print_formatted(
                    Constants.INVALID_INPUT_MESSAGE.format("number"), "error")

    @staticmethod
    def get_action() -> str:
        Constants.print_formatted("Action Selection", "subheader")
        while True:
            action = input(Constants.ACTION_PROMPT).strip().lower()
            match action:
                case '1' | 'type':
                    return 'type'

                case '2' | 'prime':
                    return 'prime'

                case '3' | 'power':
                    return 'power'

                case '4' | 'divs':
                    return 'divs'

                case '5' | 'multi':
                    return 'multi'

                case _:
                    Constants.print_formatted(Constants.INVALID_INPUT_MESSAGE.format("action"), "error")

    @staticmethod
    def get_numbers() -> Union[int, float, List[int]]:
        Constants.print_formatted("Number Selection", "subheader")
        while True:
            Selection = input(Constants.NUMBER_AMOUNT_PROMPT).strip().lower()
            match Selection:

                case '1' | 'number':
                    number_count = InputHandler.safe_number_input(f"{Constants.INPUT_BULLET} How many numbers do you want to enter? ")                    

                    match number_count:
                        case 1:
                            return InputHandler.safe_number_input(Constants.NUMBER_INPUT_PROMPT.format("your number"))

                        case _ if number_count > 0 and isinstance(number_count, int):
                            return [InputHandler.safe_number_input(Constants.NUMBER_INPUT_PROMPT.format(f"number {num + 1} of {number_count}")) for num in range(number_count)]
                        
                        case _:
                            Constants.print_formatted(Constants.INVALID_INPUT_MESSAGE.format("nutural number"), "error")


                case '2' | 'range':
                    return InputHandler.get_range()

                case _:
                    Constants.print_formatted(Constants.INVALID_INPUT_MESSAGE.format("number"), "error")

    @staticmethod
    def get_display() -> str:
        Constants.print_formatted("Display Selection", "subheader")
        while True:
            display = input(Constants.DISPLAY_PROMPT).strip().lower()
            match display:
                case '1' | 'each':
                    return 'each'

                case '2' | 'block':
                    return 'block'

                case _:
                    Constants.print_formatted(
                        Constants.INVALID_INPUT_MESSAGE.format("display"), "error")

    @staticmethod
    def get_range() -> Union[int, List[int]]:
        Constants.print_formatted("Range Input", "subheader")
        while True:
            try:
                start_range = InputHandler.safe_number_input(
                    Constants.ENTER_RANGE_PROMPT.format("start"))
                step_range = InputHandler.safe_number_input(
                    Constants.ENTER_RANGE_PROMPT.format("step"))
                if step_range == 0:
                    raise ValueError(Constants.RANGE_ZERO_STEP_ERROR)
                stop_range = InputHandler.safe_number_input(
                    Constants.ENTER_RANGE_PROMPT.format("end"))

                range_values = list(range(start_range, stop_range, step_range))

                if not range_values:
                    raise ValueError(Constants.RANGE_EMPTY_ERROR)

                if len(range_values) == 1:
                    return range_values[0]

                return range_values

            except ValueError as err:
                Constants.print_formatted(
                    f"Invalid input: {err}. Please try again.", "error")


def main() -> None:
    Constants.print_formatted(Constants.WELCOME_MESSAGE, "header")
    print(Constants.SUBTITLE_MESSAGE)

    # numbers = 144
    # numbers = list(range(-2,13))
    numbers = [2 ** i - 1 for i in range(10, 21)]
    # numbers = [-99, 89, 363-54, 8374/4, 101, 200, 'hfhfh', '5/0', 974589//18]

    # action = 'type'
    # action = 'prime'
    action = 'power'
    # action = 'divs'
    # action = 'multi'

    display = 'each'
    # display = 'block'

    input_handler = InputHandler()
    numbers, action, display = input_handler.get_user_input()
    number_analysis = NumberAnalysis()
    number_analysis.number_analysis_hub(numbers, action, display)


if __name__ == '__main__':
    main()
