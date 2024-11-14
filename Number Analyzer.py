from typing import Any, List, Dict, Tuple, Union, Optional, Literal, Callable
NumericValue = Union[int, float] ; NumericInput = Union[NumericValue, List[NumericValue]]


class Constants:
    PRIMARY_BULLET = "►"
    SECONDARY_BULLET = "•"
    EXAMPLE_BULLET = "❱"
    INPUT_BULLET = "\n✎ "
    BUTTON_BULLET = "⏩"

    POSITIVE_RESULT_BULLET  = "✅"
    NEGATIVE_RESULT_BULLET = "❎"

    TEXT_STYLES = {
        "header": {
            "bullet_char": "🧮",
            "border_char": "=",
            "side_padding": lambda text: len(text) + 6,
            "button_padding": '\n\n'
        },
        "subheader": {
            "bullet_char":  "⚜",
            "border_char": "⚊",
            "side_padding": lambda text: len(text) + 4,
            "button_padding": '\n'
        },
        "selected": {
            "bullet_char":  "|",
            "border_char": "-",
            "side_padding": lambda text: len(text) + 4,
            "button_padding": '\n'
        },
        "error": {
            "bullet_char": "❌",
            "border_char": "◢  ",
            "side_padding": lambda text: (len(text) // 3) + 3,
            "button_padding": '\n\n'
        }
    }

    WELCOME_MESSAGE = "Welcome to the Number Cruncher!"
    SUBTITLE_MESSAGE = "☛ Let's explore some fascinating math tricks with numbers ☚"

    BACK_KEY = '/'
    # "or return to the previous step by entering the character '{BACK_KEY}"
    EXIT_KEY = '.'

    BUTTON_PROMPT = f'''
  » At any stage of the program you can exit by entering the character '{EXIT_KEY}' 
{INPUT_BULLET} Please enter your choice (1, 2 or the name)

{BUTTON_BULLET} '''

    ACTION_PROMPT = f'''
What would you like to know about your number(s)?
{PRIMARY_BULLET} 1. Type:
  {SECONDARY_BULLET} Find out if a number is special (like prime or even)
    {EXAMPLE_BULLET} Example: Is 12 a prime or a composite (not prime) number?

{PRIMARY_BULLET} 2. Prime:
  {SECONDARY_BULLET} Break down a number into its building blocks
    {EXAMPLE_BULLET} Example: 12 breaks down to 2, 2, and 3

{PRIMARY_BULLET} 3. Power:
  {SECONDARY_BULLET} See how many times each prime factor appears
    {EXAMPLE_BULLET} Example: In 12, 2 appears twice and 3 once

{PRIMARY_BULLET} 4. Divs:
  {SECONDARY_BULLET} Find all numbers that divide evenly into your number
    {EXAMPLE_BULLET} Example: 12 can be divided by 2, 3, 4, and 6

{PRIMARY_BULLET} 5. Multi:
  {SECONDARY_BULLET} Show different ways to multiply to get your number
    {EXAMPLE_BULLET} Example: 12 can be 3 X 4 or 2 X 6

{PRIMARY_BULLET} 6. Exit
{INPUT_BULLET} Please enter your choice (1-6 or the name)

{BUTTON_BULLET} '''

    NUMBER_AMOUNT_PROMPT = f'''
How would you like to input your numbers?
{PRIMARY_BULLET} 1. Numbers
  {SECONDARY_BULLET} Enter a single or multiple numbers
{PRIMARY_BULLET} 2. Range
  {SECONDARY_BULLET} Generate a range of numbers

{BUTTON_PROMPT} '''

    DISPLAY_PROMPT = f'''
How would you like to view your results?
{PRIMARY_BULLET} 1. Each
  {SECONDARY_BULLET} See details for each number individually
{PRIMARY_BULLET} 2. Block
  {SECONDARY_BULLET} View all results grouped together in a block

{BUTTON_PROMPT} '''

    COUNT_PROMPT = f"{INPUT_BULLET} How many numbers do you want to enter?\n\n{BUTTON_BULLET} "

    RANGE_PROMPT = f"{INPUT_BULLET} Enter the {{}} value of the range (you can use math expressions) ({{}}): "
    NUMBERS_INPUT_PROMPT = f"{INPUT_BULLET} Enter {{}} (also use mathematical expressions, e.g., 12 X 9, 6^8. return to the previous number by entering the character '{BACK_KEY})': "

    INVALID_INPUT_MESSAGE = "ERROR: Oops! That's not a valid {}. Let's give it another try"
    RANGE_ZERO_STEP_ERROR = "The step cannot be zero. Please choose a non-zero value"
    RANGE_EMPTY_ERROR = "The range is empty. Please create a valid range"

    PROMPTS_TO_STEPS = {
        "action": ACTION_PROMPT,
        "numbers": NUMBER_AMOUNT_PROMPT,
        "number_count": COUNT_PROMPT,
        "single_or_multiple_numbers": NUMBERS_INPUT_PROMPT,
        "range_start": RANGE_PROMPT.format("start", "default is 0"),
        "range_step": RANGE_PROMPT.format("step", "cannot be 0, default is 1"),
        "range_stop": RANGE_PROMPT.format("end", "required"),
        "display": DISPLAY_PROMPT
    }

    ACTION_AND_DESC = {
        'type': {
            "desc": "number type",
            "func": lambda number, classifier: {f"{classifier.classify_number(number)} numbers": [number]}
        },
        'prime': {
            "desc": "prime factors",
            "func": lambda number, math_ops: math_ops.factorize_into_primes(number)
        },
        'power': {
            "desc": "prime factors with count",
            "func": lambda number, math_ops: math_ops.group_prime_factors_by_power(math_ops.factorize_into_primes(number))
        },
        'divs': {
            "desc": "divisors",
            "func": lambda number, math_ops: math_ops.calculate_divisors(math_ops.group_prime_factors_by_power(math_ops.factorize_into_primes(number)))
        },
        'multi': {
            "desc": "multiplication combinations",
            "func": lambda number, math_ops: math_ops.create_multiples(math_ops.calculate_divisors(math_ops.group_prime_factors_by_power(math_ops.factorize_into_primes(number))))
        }
    }

    DISPLAY_TYPES = {'each', 'block', None}



class NumberClassifier:

    @staticmethod
    def classify_number(number: Any) -> Literal['not applicable for primality', 'is composite', 'is prime', 'is a list', 'is invalid']:
        match number:
            case int() | float():

                if number <= 1 or not number.is_integer():
                    return 'not applicable for primality'

                return NumberClassifier.is_prime_or_composite(number)

            case list() | tuple():
                return 'is a list'

            case _:
                return 'is invalid'


    @staticmethod
    def is_prime_or_composite(number: int) -> str:
        if number % 2 == 0 and number != 2:
            return 'is composite'

        for factor in range(3, int(number ** 0.5) + 1, 2):
            if number % factor == 0:
                MathOperations.smallest_factor = factor
                return 'is composite'

        return 'is prime'



class MathOperations:
    smallest_factor = None

    @classmethod
    def factorize_into_primes(cls, number: int) -> List[int]:
        primary_factors_list = []

        while number % 2 == 0:
            primary_factors_list.append(2)
            number //= 2

        start = cls.smallest_factor if cls.smallest_factor else 3

        for factor in range(start, int(number ** 0.5) + 1, 2):
            while number % factor == 0:
                primary_factors_list.append(factor)
                number //= factor

        if number > 1:
            primary_factors_list.append(number)

        return primary_factors_list


    @staticmethod
    def group_prime_factors_by_power(factors_list: List[int]) -> List[str]:
        factor_frequencies = {}
        for factor in factors_list:
            factor_frequencies[factor] = factor_frequencies.get(factor, 0) + 1

        return [f"{factor}^{count}" for factor, count in factor_frequencies.items()]


    @staticmethod
    def calculate_divisors(prime_factor_powers: List[str]) -> List[int]:
        number_divisors = {1}

        for factor in prime_factor_powers:
            prime, power = map(int, factor.split('^'))
            number_divisors.update({divisor * (prime ** exponent) for divisor in number_divisors for exponent in range(power + 1)})
        
        return sorted(number_divisors)[1:-1]


    create_multiples: Callable[[List[int]], List[str]] = staticmethod(lambda divisors: [f"{divisors[i]} X {divisors[-1-i]}" for i in range(sum(divmod(len(divisors), 2)))])

    # create_multiples: Callable[[List[int]], List[str]] = staticmethod(lambda divisors: [f"{divisors[i]} X {divisors[-1-i]}" for i in range(len(divisors) // 2 + (len(divisors) % 2))])




class NumberAnalysis:

    def number_analysis_hub(self, action: str, numbers: NumericInput, display: Optional[str]) -> str:
        self.action = action
        self.numbers = numbers
        self.display = display
        
        if not self._validate_input():
            return 'Invalid input'

        Printer.print_formatted("header", "Results")
        number_type = NumberClassifier.classify_number(self.numbers)
        if number_type == 'is a list':
            self.process_display()

        else:
            Printer.display_individual_result(self)

        return number_type


    def _validate_input(self) -> bool:
        if self.action not in Constants.ACTION_AND_DESC:
            Printer.print_formatted("error", "action")
            return False
        
        if not self.numbers:
            Printer.print_formatted("error", "It does not contain numbers")
            return False

        if self.display not in Constants.DISPLAY_TYPES:
            Printer.print_formatted("error", "display")
            return False

        return True


    def process_display(self) -> None:
        print(f"Numbers: {Printer.format_object_to_str(self.numbers)}\n")

        match self.display:
            case 'each':
                for number in self.numbers:
                    self.numbers = number
                    Printer.display_individual_result(self)

            case 'block':
                results = self.create_results_dict(self.numbers, self.action)
                Printer.display_grouped_results(results)

            case _:
                Printer.print_formatted("error", "display")




    @staticmethod
    def create_results_dict(list_of_numbers: List[int], action: str) -> Dict[Union[int, str], Union[str, int]]:
        numbers_dict = {}

        action_function = Constants.ACTION_AND_DESC[action]["func"]

        for number in list_of_numbers:
            number_type = NumberClassifier.classify_number(number)

            if action == 'type' and number_type != 'is invalid':
                numbers_dict.setdefault(f"{number_type} numbers", []).append(number)

            elif number_type == 'is composite':
                numbers_dict[number] = action_function(number, MathOperations())

            else:
                numbers_dict.setdefault('Irrelevant', []).append(number)

        return numbers_dict



class Printer:

    @staticmethod
    def print_formatted(style_name: Literal['header', 'subheader', 'selected', 'error'], text: Union[str, Tuple[str, NumericInput]]) -> None:
        style_config = Constants.TEXT_STYLES[style_name]

        match style_name:
            case "error":
                text = Constants.INVALID_INPUT_MESSAGE.format(text)

            case "selected":
                step, select = text
                match select:
                    case str():
                        select = select.capitalize()

                    case list():
                        select = Printer.format_object_to_str(select)
            
                text = f"The selected {step} is: {select}"

        border_line = style_config['border_char'] * style_config["side_padding"](text)

        print(f"\n{border_line}")
        print(style_config['bullet_char'], text, style_config['bullet_char'])
        print(border_line, end=style_config["button_padding"])


    @staticmethod
    def display_individual_result(analysis: NumberAnalysis) -> None:
        action = analysis.action
        number = analysis.numbers
        number_type = NumberClassifier.classify_number(number)

        action_info = Constants.ACTION_AND_DESC[action]
        action_function = action_info["func"]

        bullet = Constants.POSITIVE_RESULT_BULLET if (action == 'type' and number_type != 'is invalid' ) or number_type == 'is composite' \
        else Constants.NEGATIVE_RESULT_BULLET

        print(f"\n{bullet} The number {number}", end="")

        if action == 'type' or number_type != 'is composite':
            print(f" {number_type}")

        else:
            action_results = action_function(number, MathOperations())
            description = action_info["desc"]
            print(f":")
            print(f"   {Constants.SECONDARY_BULLET} Number of {description}: {len(action_results)}")
            print(f"   {Constants.SECONDARY_BULLET} List of {description}: {Printer.format_object_to_str(action_results)}")


    @staticmethod
    def display_grouped_results(results_dict: Dict[Union[int, str], Union[str, int]]) -> None:
        if 'Irrelevant' in results_dict:
            print(f"   {Constants.NEGATIVE_RESULT_BULLET} Irrelevant: {Printer.format_object_to_str(results_dict.pop('Irrelevant'))}\n")
        
        for key, value in results_dict.items():
            print(f"   {Constants.POSITIVE_RESULT_BULLET} {key}: {Printer.format_object_to_str(value)}")


    format_object_to_str: Callable[[Union[list, dict]], str] = staticmethod(lambda obj: str(obj)[1:-1].replace("'", ""))



class UserInput:

    def user_input_hub(self) -> Tuple[str, NumericInput, Optional[str]]:
        self.action = self.get_action()
        Printer.print_formatted("selected", ('action', self.action))

        self.numbers = []
        self.numbers = self.get_numbers()
        Printer.print_formatted("selected", ('numbers' if isinstance(self.numbers, list) else 'number', self.numbers))

        if isinstance(self.numbers, list) and len(self.numbers) > 1:
            self.display = self.get_display()
            Printer.print_formatted("selected", ('display', self.display))
        else:
            self.display = None


        return self.action, self.numbers, self.display


    def get_action(self) -> Literal['type', 'prime', 'power', 'divs', 'multi']:
        Printer.print_formatted("subheader", "Action Selection")

        while True:
            user_input = input(Constants.PROMPTS_TO_STEPS['action']).strip().lower()
            match user_input:
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

                case '6' | 'exit':
                    self.exit_program()

                case _:
                    Printer.print_formatted("error", "action")


    def get_numbers(self) -> Union[NumericInput, str]:
        Printer.print_formatted("subheader", "Number(s) Selection")

        while True:
            user_input = input(Constants.PROMPTS_TO_STEPS['numbers']).strip().lower()

            match user_input:
                case '1' | 'numbers':
                    number_count = self.safe_number_input('number_count',require_natural=True)

                    return self.safe_number_input('single_or_multiple_numbers',multi_count=number_count if number_count > 1 else None)

                case '2' | 'range':     
                    return self.get_range()

                # case Constants.BACK_KEY:
                #     return self.go_back('numbers')


                case Constants.EXIT_KEY:
                    self.exit_program()

                case _:
                    Printer.print_formatted("error", "numbers")


    def get_range(self) -> Union[List[int], int]:
        Printer.print_formatted("subheader", "Range of Numbers")
        while True:
            try:
                self.range_start = self.safe_number_input('range_start', default=0)

                self.range_step = self.safe_number_input('range_step', default=1)
                while self.range_step == 0:
                    Printer.print_formatted("error", Constants.RANGE_ZERO_STEP_ERROR)
                    self.range_step = self.safe_number_input('range_step', default=1)

                self.range_stop = self.safe_number_input('range_stop')

                range_values = list(range(self.range_start, self.range_stop, self.range_step))
                if not range_values:
                    raise ValueError(Constants.RANGE_EMPTY_ERROR)

                return range_values

            except ValueError as err:
                Printer.print_formatted("error", f"range values: {err}")
            except Exception as err:
                Printer.print_formatted("error", err)


    def get_display(self) -> str:
        Printer.print_formatted("subheader", "Display Selection")
        while True:
            display = input(Constants.PROMPTS_TO_STEPS['display']).strip().lower()
            match display:
                case '1' | 'each':
                    return 'each'

                case '2' | 'block':
                    return 'block'

                # case Constants.BACK_KEY:
                #     return self.go_back('display')

                case Constants.EXIT_KEY:
                    self.exit_program()

                case _:
                    Printer.print_formatted("error", "display")


    def safe_number_input(self, current_step: str, require_natural: bool = False, default: Optional[NumericValue] = None, multi_count: Optional[int] = None) -> Union[NumericInput, str]:

            while True:
                if multi_count and len(self.numbers) == multi_count:
                    return self.numbers

                prompt = Constants.PROMPTS_TO_STEPS[current_step]
                if current_step == 'single_or_multiple_numbers':
                    prompt = prompt.format(f"number No. {len(self.numbers) + 1} of {multi_count}") if multi_count else prompt.format("the number")
                
                user_input = input(prompt).strip().upper().replace('X', '*').replace('^', '**')

                if user_input == Constants.BACK_KEY:
                    if self.numbers:
                        self.numbers.pop()
                        continue
                    # else:
                    #     return self.go_back(current_step)
                
                if user_input == Constants.EXIT_KEY:
                    self.exit_program()

                if not user_input and default is not None:
                    return default

                try:
                    if require_natural:
                        number = int(user_input)
                        if number <= 0:
                            raise ValueError
                    else:
                        number = eval(user_input, {}, {})
                        if not isinstance(number, NumericValue):
                            raise ValueError
                    
                    if isinstance(number, float) and number.is_integer():
                        number = int(number)

                    if multi_count:
                        if number not in self.numbers:
                            self.numbers.append(number)
                        else:
                            Printer.print_formatted("error", "Number not entered")

                    else:
                        return number

                except (SyntaxError, NameError, TypeError):
                    Printer.print_formatted("error", "mathematical expression")
                except ValueError:
                    Printer.print_formatted("error", "natural number")
                except Exception as err:
                    Printer.print_formatted("error", err)


    @staticmethod
    def exit_program():
        print('Exiting the program...')
        # raise SystemExit
        exit()


    # def go_back(self, current_step: str) -> None:
    #     steps = list(Constants.PROMPTS_TO_STEPS)
    #     previous_step = steps[steps.index(current_step) - 1] if current_step != 'range_start' else 'numbers'

    #     match current_step:
    #         case 'numbers':
    #             self.action = self.get_action()
    #             return self.get_numbers()

    #         case 'number_count' | 'range_start':
    #             self.numbers = self.get_numbers()

    #         case 'range_step':
    #             self.range_start = self.safe_number_input('range_start', default=0)
    #             return self.safe_number_input('range_step', default=1)

    #         case 'range_stop':
    #             self.range_step = self.safe_number_input('range_step', default=1)
    #             return self.safe_number_input('range_stop')

    #         case 'display':
    #             if hasattr(self, 'range_stop'):
    #                 self.range_stop = self.safe_number_input('range_stop', default=1)
    #                 self.numbers = list(range(self.range_start, self.range_stop, self.range_step))
    #                 while not self.numbers:
    #                     Printer.print_formatted("error", f"Invalid range values: {Constants.RANGE_EMPTY_ERROR}")
    #                     self.range_stop = self.safe_number_input('range_stop', default=1)
    #                     self.numbers = list(range(self.range_start, self.range_stop, self.range_step))

    #             else:
    #                 self.numbers[-1] = self.safe_number_input('single_or_multiple_numbers', multi_count = len(self.numbers) if len(self.numbers) > 1 else None)
    #             return self.get_display()



def main() -> None:
    number_analysis = NumberAnalysis()

    numbers = 64, 101, -9, 'dhdgfg', '456', 203.5, 561**3
    # numbers = 2520
    # numbers = list(range(-2, 13))
    # numbers = [2 ** i - 1 for i in range(-2, 22)]
    # numbers = [-99, 89, 363-54, 8374/4, 101, '200', 'hfhfh', '5/0', 974589//18]

    action = 'type'
    # action = 'prime'
    action = 'power'
    # action = 'divs'
    # action = 'multi'

    display = 'each'
    display = 'block'


    # Printer.print_formatted("header", Constants.WELCOME_MESSAGE)
    # print(Constants.SUBTITLE_MESSAGE)
    # input_handler = UserInput()
    # while True:
    #     action, numbers, display = input_handler.user_input_hub()
    #     number_analysis.number_analysis_hub(action, numbers, display)

    number_analysis.number_analysis_hub(action, numbers, display)

if __name__ == '__main__':
    main()
