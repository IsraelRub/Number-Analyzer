from typing import Any, List, Dict, Tuple, Union, Optional, Callable, Literal
Number = Union[int, float]


class Constants:
    PRIMARY_BULLET = "►"
    SECONDARY_BULLET = "•"
    EXAMPLE_BULLET = "❱"
    INPUT_BULLET = "✎ "
    BUTTON_BULLET = "⏩"

    POSITIVE_RESULT_INDICATOR = "✅"
    NEGATIVE_RESULT_INDICATOR = "❎"

    TEXT_STYLES = {
        "header": {
            "border_char": "=",
            "bullet_char": "🧮",
            "side_padding": 6
        },
        "subheader": {
            "border_char": "⚊",
            "bullet_char":  "⚜",
            "side_padding": 4
        },
        "error": {
            "border_char": "◢  ",
            "bullet_char": "❌",
            "side_padding": 3
        }
    }

    WELCOME_MESSAGE = "Welcome to the Number Cruncher!"
    SUBTITLE_MESSAGE = "☛ Let's explore some fascinating math tricks with numbers ☚"

    EXIT_KEYWORD = '.'
    EXIT_BUTTON = f"\n  » Remember, at any stage of the program it is possible to exit by entering the character '.': \n\n{
        BUTTON_BULLET} "

    ACTION_PROMPT = f'''\nWhat would you like to know about your number(s)?
{PRIMARY_BULLET} 1. Number Type:
  {SECONDARY_BULLET} Find out if a number is special (like prime or even)
    {EXAMPLE_BULLET} Example: Is 12 a prime or a composite (not prime) number?

{PRIMARY_BULLET} 2. Prime Factors:
  {SECONDARY_BULLET} Break down a number into its building blocks
    {EXAMPLE_BULLET} Example: 12 breaks down to 2, 2, and 3

{PRIMARY_BULLET} 3. Prime Power:
  {SECONDARY_BULLET} See how many times each prime factor appears
    {EXAMPLE_BULLET} Example: In 12, 2 appears twice and 3 once

{PRIMARY_BULLET} 4. Divisors:
  {SECONDARY_BULLET} Find all numbers that divide evenly into your number
    {EXAMPLE_BULLET} Example: 12 can be divided by 2, 3, 4, and 6

{PRIMARY_BULLET} 5. Multiplications:
  {SECONDARY_BULLET} Show different ways to multiply to get your number
    {EXAMPLE_BULLET} Example: 12 can be 3 X 4 or 2 X 6

{PRIMARY_BULLET} 6. Exit

  » At any stage of the program it is possible to exit by entering the character '.'

{INPUT_BULLET} Please enter your choice (1-6 or the name):

{BUTTON_BULLET} '''

    NUMBER_AMOUNT_PROMPT = f'''\nHow would you like to input your numbers?
{PRIMARY_BULLET} 1. Numbers
  {SECONDARY_BULLET} Enter a single or multiple numbers
{PRIMARY_BULLET} 2. Range
  {SECONDARY_BULLET} Generate a range of numbers
 {EXIT_BUTTON}

{INPUT_BULLET} Please enter your choice (1, 2 or the name): '''

    DISPLAY_PROMPT = f'''\nHow would you like to view your results?
{PRIMARY_BULLET} 1. Each
  {SECONDARY_BULLET} See details for each number individually
{PRIMARY_BULLET} 2. Block
  {SECONDARY_BULLET} View all results grouped together in a block
 {EXIT_BUTTON}

{INPUT_BULLET} Please enter your choice (1, 2 or the name): '''

    ACTION_AND_DESC = {
        'type': {
            "desc": "number type",
            "func": lambda number, classifier, math_ops: {f"{classifier.classify_number(number)} numbers": [number]}
        },
        'prime': {
            "desc": "prime factors",
            "func": lambda number, classifier, math_ops: math_ops.factorize_into_primes(number)
        },
        'power': {
            "desc": "prime factors with count",
            "func": lambda number, classifier, math_ops: math_ops.group_prime_factors_by_power(math_ops.factorize_into_primes(number))
        },
        'divs': {
            "desc": "divisors",
            "func": lambda number, classifier, math_ops: math_ops.calculate_divisors(math_ops.group_prime_factors_by_power(math_ops.factorize_into_primes(number)))
        },
        'multi': {
            "desc": "multiplication combinations",
            "func": lambda number, classifier, math_ops: math_ops.generate_factor_pairs(math_ops.calculate_divisors(math_ops.group_prime_factors_by_power(math_ops.factorize_into_primes(number))))
        }
    }
    DISPLAY_TYPES = {'each', 'block', None}

    INVALID_INPUT_MESSAGE = "Oops! That's not a valid {}. Let's give it another try."
    NUMBERS_INPUT_PROMPT = f"{
        INPUT_BULLET} Enter {{}} (feel free to use math expressions, e.g., 12 X 9, 6^8): "
    ENTER_RANGE_PROMPT = f"{
        INPUT_BULLET} Enter the {{}} value of the range (you can use math expressions) ({{}}) :"

    PROMPTS = {
        'start_range': ENTER_RANGE_PROMPT.format("start", "default is 0"),

        'step_range': ENTER_RANGE_PROMPT.format("step", "cannot be 0, default is 1"),

        'end_range': ENTER_RANGE_PROMPT.format("end", "required"),

        'count': "How many numbers do you want to enter? "
    }

    RANGE_ZERO_STEP_ERROR = "The step cannot be zero. Please choose a non-zero value."
    RANGE_EMPTY_ERROR = "The range is empty. Please ensure that the start, end, and step values create a valid range."

    NUMBERS_COUNT_PROMPT = f"{
        INPUT_BULLET} How many numbers do you want to enter? "


class NumberClassifier:

    smallest_factor = None

    def classify_number(self, number: Any) -> Literal[
            'not applicable for primality', 'is composite', 'is prime', 'is a list', 'is invalid']:

        match number:
            case int() | float():

                if number <= 1 or not number.is_integer():
                    return 'not applicable for primality'

                if self._is_even_composite(number):
                    return 'is composite'

                if self._is_odd_composite(number):
                    return 'is composite'

                return 'is prime'

            case list() | tuple():
                return 'is a list'

            case _:
                return 'is invalid'

    _is_even_composite: Callable[[
        int], bool] = lambda self, number: number % 2 == 0 and number != 2

    def _is_odd_composite(self, number: int) -> bool:

        for factor in range(3, int(number ** 0.5) + 1, 2):

            if number % factor == 0:
                MathOperations.smallest_factor = factor
                return True

        return False


class MathOperations:
    smallest_factor = None

    @classmethod
    def factorize_into_primes(cls, number: int) -> List[int]:
        factors_list = []

        while number % 2 == 0:
            factors_list.append(2)
            number //= 2

        start = cls.smallest_factor if cls.smallest_factor else 3

        for factor in range(start, int(number ** 0.5) + 1, 2):
            while number % factor == 0:
                factors_list.append(factor)
                number //= factor

        if number > 1:
            factors_list.append(number)

        return factors_list

    group_prime_factors_by_power: Callable[[List[int]], List[str]] = staticmethod(
        lambda factors_list: [f"{factor}^{factors_list.count(factor)}" for factor in set(factors_list)])

    @staticmethod
    def calculate_divisors(prime_factor_powers: List[str]) -> List[int]:
        divisors = {1}

        for factor in prime_factor_powers:
            prime, power = map(int, factor.split('^'))
            temp_divisors = set()

            for i in range(power + 1):
                temp_divisors.update(
                    {divisor * prime ** i for divisor in divisors})
            divisors = temp_divisors

        return sorted(divisors)[1:-1]

    generate_factor_pairs: Callable[[List[int]], List[str]] = staticmethod(
        lambda divisors: [f"{divisors[i]} X {divisors[-1-i]}" for i in range(len(divisors) // 2 + (len(divisors) % 2))])


class NumberAnalysis:
    def __init__(self):
        self.classifier: NumberClassifier = NumberClassifier()
        self.math_ops: MathOperations = MathOperations()

    def set_all(self, numbers, action, display) -> None:
        self.numbers: Any = numbers
        self.action: Literal['type', 'prime',
                             'power', 'divs', 'multi'] = action
        self.display: Literal['each', 'block'] = display if display else None

    def set_single_number(self, number: any) -> None:
        self.numbers = number

    def number_analysis_hub(self) -> str:
        if not self._validate_input():
            return "Invalid input"

        number_type = self.classifier.classify_number(self.numbers)

        if number_type == 'is a list':
            self.process_list()
        else:
            Printer.display_individual_result(self)

        return number_type

    def _validate_input(self) -> bool:
        if self.action not in Constants.ACTION_AND_DESC:
            Printer.print_formatted("error", "action")
            return False

        if self.display not in Constants.DISPLAY_TYPES:
            Printer.print_formatted("error", "display")
            return False

        return True

    def create_action_results_dict(self, numbers: Union[int, List[int]], action: str) -> Dict[str, Any]:
        numbers_dict = {}
        not_relevants_dict = {}

        selected_action_function = Constants.ACTION_AND_DESC[action]["func"]

        for number in numbers:
            number_type = self.classifier.classify_number(number)

            if number_type == 'is composite':
                result = selected_action_function(
                    number, self.classifier, self.math_ops)
                numbers_dict[number] = result
            else:
                not_relevants_dict.setdefault('Irrelevant', []).append(number)

        return not_relevants_dict | numbers_dict

    def create_type_dict(self, list_of_numbers: List[int]) -> Dict[str, List[int]]:
        type_dict = {}
        for number in list_of_numbers:
            number_type = self.classifier.classify_number(number)
            type_dict.setdefault(f"{number_type} numbers", []).append(number)
        return type_dict

    def process_list(self) -> None:
        list_of_numbers = self.numbers
        action = self.action
        display = self.display

        if len(list_of_numbers) > 1:
            Printer.print_formatted("header", "Results")
            print(f"Numbers: {
                  Printer.format_object_to_str(list_of_numbers)}\n")

            match display:
                case 'each':
                    for number in list_of_numbers:
                        self.set_single_number(number)
                        Printer.display_individual_result(self)

                case 'block':
                    if action == 'type':
                        results = self.create_type_dict(list_of_numbers)
                        Printer.display_grouped_results(
                            results, style_type=True)

                    else:
                        results = self.create_action_results_dict(
                            list_of_numbers, action)
                        Printer.display_grouped_results(results)

                case _:
                    Printer.print_formatted("error", "display")

        elif len(list_of_numbers) == 1:
            self.set_single_number(list_of_numbers[0])
            Printer.display_individual_result(self)

        else:
            Printer.print_formatted("error", "It does not contain numbers")


class Printer:
    positive_indicator = Constants.POSITIVE_RESULT_INDICATOR
    negative_indicator = Constants.NEGATIVE_RESULT_INDICATOR

    @staticmethod
    def print_formatted(style_name: str, text: str) -> None:
        style_config = Constants.TEXT_STYLES[style_name]

        if style_name == "error":
            text = f"ERROR: {Constants.INVALID_INPUT_MESSAGE.format(text)}"
            border_line = style_config['border_char'] * \
                ((len(text)) // 3 + style_config["side_padding"])
        else:
            border_line = style_config['border_char'] * \
                (len(text) + style_config["side_padding"])

        print(f"\n{border_line}")
        print(style_config['bullet_char'], text, style_config['bullet_char'])
        print(f"{border_line}\n")

    @classmethod
    def get_result_indicator(cls, number: Union[int, str], number_type: str, style_type) -> str:
        if (style_type and "invalid" not in number_type) \
                or number_type == 'is composite' \
                or isinstance(number, int):
            return cls.positive_indicator
        else:
            return cls.negative_indicator

    @classmethod
    def display_individual_result(cls, analysis: NumberAnalysis) -> None:
        single_number = analysis.numbers
        action = analysis.action
        number_type = analysis.classifier.classify_number(single_number)

        if action == 'type' or number_type == 'is composite':
            selected_action_function = Constants.ACTION_AND_DESC[action]["func"]
            action_results = selected_action_function(
                single_number, analysis.classifier, analysis.math_ops)

        indicator = cls.get_result_indicator(
            single_number, number_type, action == 'type')

        if action == 'type':
            print(f"\n{indicator} The number {single_number} {number_type}")
        elif number_type != 'is composite':
            print(f"\n{indicator} The number {single_number} {number_type}")
        else:
            description = Constants.ACTION_AND_DESC[action]["desc"]
            print(f"\n{indicator} For the number {single_number}:")
            print(f"   {Constants.SECONDARY_BULLET} Number of {
                  description}: {len(action_results)}")
            print(f"   {Constants.SECONDARY_BULLET} List of {
                  description}: {cls.format_object_to_str(action_results)}")

    @classmethod
    def display_grouped_results(cls, results: Dict[str, Any], style_type=False) -> None:
        for key, value in results.items():
            bullet = cls.get_result_indicator(key, key, style_type)
            print(f"   {bullet} {key}: {Printer.format_object_to_str(value)}")

    format_object_to_str: Callable[[Union[list, dict]], str] = staticmethod(
        lambda obj: str(obj)[1:-1].replace("'", ""))


class InputHandler:

    @staticmethod
    def exit_program() -> None:
        print("Exiting the program...")
        # raise SystemExit
        exit()

    @staticmethod
    def user_input_hub() -> Tuple[Union[Number, List[Union[Number]]], str, Optional[str]]:
        action = InputHandler.get_action()
        numbers = InputHandler.get_numbers()
        display = InputHandler.get_display() if isinstance(
            numbers, list) and len(numbers) > 1 else None

        return numbers, action, display

    @staticmethod
    def safe_number_input(input_type: str) -> Union[Number]:
        prompt_message = Constants.PROMPTS.get(input_type, input_type)

        while True:
            user_input = input(prompt_message).strip(
            ).upper().replace('X', '*').replace('^', '**')

            if user_input == Constants.EXIT_KEYWORD:
                InputHandler.exit_program()

            try:
                if "range" in input_type:
                    match input_type:

                        case 'start_range':
                            return int(user_input) if user_input else 0

                        case 'step_range':
                            if user_input == '0':
                                raise ValueError(
                                    Constants.RANGE_ZERO_STEP_ERROR)

                            return int(user_input) if user_input else 1

                        case 'end_range':
                            return int(user_input)

                if input_type == "count":
                    user_input = int(user_input)
                    if user_input > 0:
                        return user_input
                    else:
                        raise ValueError

                computed_number = eval(user_input, {}, {})

                if not isinstance(computed_number, (int, float)):
                    raise ValueError("Input must evaluate to a number")

                return int(computed_number) if computed_number.is_integer() else computed_number

            except (SyntaxError, NameError, TypeError):
                Printer.print_formatted("error", "mathematical expression")
            except ValueError:
                Printer.print_formatted("error", "natural number")
            except Exception as err:
                Printer.print_formatted("error", err)

    @staticmethod
    def get_action() -> Literal['type', 'prime', 'power', 'divs', 'multi']:
        Printer.print_formatted("subheader", "Action Selection")
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

                case '6' | 'exit' | Constants.EXIT_KEYWORD:
                    InputHandler.exit_program()

                case _:
                    Printer.print_formatted("error", "action")

    @staticmethod
    def get_numbers() -> Union[Number, List[Union[Number]], str]:
        Printer.print_formatted("subheader", "Number Selection")

        while True:
            selection = input(Constants.NUMBER_AMOUNT_PROMPT.format(
                "action")).strip().lower()
            match selection:
                case '1' | 'numbers':
                    return InputHandler.get_single_or_multiple_numbers()
                case '2' | 'range':
                    return InputHandler.get_range()

                case Constants.EXIT_KEYWORD:
                    InputHandler.exit_program()
                case _:
                    Printer.print_formatted("error", "numbers")

    @staticmethod
    def get_single_or_multiple_numbers() -> Union[Number, List[Union[Number]], str]:
        while True:
            number_count = InputHandler.safe_number_input("count")

            if number_count == 1:
                return InputHandler.safe_number_input(Constants.NUMBERS_INPUT_PROMPT.format("the number"))
            else:
                return [InputHandler.safe_number_input(Constants.NUMBERS_INPUT_PROMPT.format(f"number {num + 1} of {number_count}")) for num in range(number_count)]

    @staticmethod
    def get_range() -> Union[List[int], int, str]:
        Printer.print_formatted("subheader", "Range Input")
        while True:
            start_range = InputHandler.safe_number_input("start_range")
            step_range = InputHandler.safe_number_input("step_range")
            stop_range = InputHandler.safe_number_input("end_range")

            range_values = list(range(start_range, stop_range, step_range))

            if not range_values:
                Printer.print_formatted("error", Constants.RANGE_EMPTY_ERROR)
                continue

            return range_values[0] if len(range_values) == 1 else range_values

    @staticmethod
    def get_display() -> Literal['each', 'block']:

        Printer.print_formatted("subheader", "Display Selection")
        while True:
            display = input(Constants.DISPLAY_PROMPT.format(
                "numbers")).strip().lower()
            match display:
                case '1' | 'each':
                    return 'each'

                case '2' | 'block':
                    return 'block'

                case Constants.EXIT_KEYWORD:
                    InputHandler.exit_program()

                case _:
                    Printer.print_formatted("error", "display")


def main() -> None:
    Printer.print_formatted("header", Constants.WELCOME_MESSAGE)
    print(Constants.SUBTITLE_MESSAGE)

    numbers = 10140, 101, -9
    # numbers = list(range(-2, 13))
    # numbers = [2 ** i - 1 for i in range(-2, 21)]
    # numbers = [-99, 89, 363-54, 8374/4, 101, 200, 'hfhfh', '5/0', 974589//18]

    action = 'type'
    # # action = 'prime'
    # # action = 'power'
    # action = 'divs'
    action = 'multi'

    # display = 'each'
    display = 'block'

    number_analysis = NumberAnalysis()

    # number_analysis.set_all(numbers, action, display)
    # number_analysis.number_analysis_hub()

    input_handler = InputHandler()
    while True:
        numbers, action, display = input_handler.user_input_hub()
        number_analysis.set_all(numbers, action, display)
        number_analysis.number_analysis_hub()


if __name__ == '__main__':
    main()
