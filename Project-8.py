# Project-8 : NumPy Analyzer

import numpy as np


class DataAnalytics:
    TITLE = "NumPy Analyzer"        # Constant

    def __init__(self, array):          # Constructer
        self.__array = np.array(array)  # Private

    # ---------- Class methods ----------
    @classmethod
    def show_welcome(cls):
        print(f"Welcome to the {cls.TITLE}!")
        print("=" * 40)

    @classmethod
    def show_goodbye(cls):
        print(f"\nThank you for using the {cls.TITLE}! Goodbye!")

    @classmethod
    def create_array(cls):
        print("\nSelect the type of array to create : ")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = cls.ask_choice(3)

        print()
        if choice == "1":
            shape = (cls.ask_whole_number("Enter the number of elements : "),)
        elif choice == "2":
            rows = cls.ask_whole_number("Enter the number of rows : ")
            columns = cls.ask_whole_number("Enter the number of columns : ")
            shape = (rows, columns)
        else:
            depths = cls.ask_whole_number("Enter the number of depths : ")
            rows = cls.ask_whole_number("Enter the number of rows : ")
            columns = cls.ask_whole_number("Enter the number of columns : ")
            shape = (depths, rows, columns)

        if min(shape) < 1:
            raise ValueError("Sizes must be greater than zero.")

        size = int(np.prod(shape))  # total number of elements
        text = input(f"Enter {size} elements for the array separated by space : ")
        array = cls.__make_array(text, shape)

        cls.show("Array created successfully : ", array)
        return cls(array)

    # ---------- Static methods ----------
    @staticmethod
    def show(title, value):
        print(f"\n{title}:")
        print(value)

    @staticmethod
    def ask_choice(count):
        """Ask for a menu choice from 1 to count."""
        choice = input("Enter your choice : ").strip()
        if not choice.isdigit() or not 1 <= int(choice) <= count:
            raise ValueError("Invalid choice. Please try again.")
        return choice

    @staticmethod
    def ask_whole_number(prompt):
        try:
            return int(input(prompt))
        except ValueError:
            raise ValueError("Please enter a whole number.")

    @staticmethod
    def ask_number(prompt):
        numbers = DataAnalytics.read_numbers(input(prompt))
        if len(numbers) != 1:
            raise ValueError("Please enter a single number.")
        return numbers[0]

    @staticmethod
    def read_numbers(text):
        """Convert text like '10 20 30' into a list of numbers."""
        numbers = []
        for i in text.split():
            try:
                num = float(i)
            except ValueError:
                raise ValueError(f"'{i}' is not a valid number.")
            if num.is_integer():
                num = int(num)  # keep 10 as 10, not 10.0
            numbers.append(num)
        return numbers

    @staticmethod
    def read_index(prompt):
        """Read a whole number. Just pressing Enter means 'all'."""
        text = input(prompt).strip()
        if text == "":
            return slice(None)
        try:
            return int(text)
        except ValueError:
            raise ValueError("Please enter a whole number or press Enter.")

    @staticmethod
    def read_range(prompt):
        """Turn text like '0:2' into a slice. '1:' and ':2' also work."""
        parts = input(prompt).replace(" ", "").split(":")
        if len(parts) != 2:
            raise ValueError("Range must look like start:end (example 0:2).")
        try:
            start = int(parts[0]) if parts[0] != "" else None
            end = int(parts[1]) if parts[1] != "" else None
        except ValueError:
            raise ValueError("Range must use whole numbers (example 0:2).")
        return slice(start, end)

    @staticmethod
    def __make_array(text, shape):
        """Private: turn text into a NumPy array with the given shape."""
        numbers = DataAnalytics.read_numbers(text)
        size = int(np.prod(shape))
        if len(numbers) != size:
            raise ValueError(f"Expected {size} elements but got {len(numbers)}.")
        return np.array(numbers).reshape(shape)

    # ---------- Private methods (internal calculations) ----------
    def __calculate(self, choice, second):
        """Do the chosen math operation. Returns its name and the result."""
        array = self.__array

        if choice == "1":
            return "Addition", array + second
        if choice == "2":
            return "Subtraction", array - second
        if choice == "3":
            return "Multiplication", array * second
        if choice == "4":
            if (second == 0).any():
                raise ValueError("Cannot divide by zero.")
            return "Division", array / second
        if choice == "5":
            return "Dot Product", np.sum(array * second)
        return "Matrix Multiplication", np.matmul(array, second)

    def __make_mask(self, choice, value):
        """Return True/False for every element, based on the chosen condition."""
        array = self.__array

        if choice == "1":
            return array > value
        if choice == "2":
            return array < value
        if choice == "3":
            return array >= value
        if choice == "4":
            return array <= value
        if choice == "5":
            return array == value
        return array != value

    def __correlation(self, second):
        """Correlation coefficient between this array and another array."""
        first = self.__array.flatten()
        second = second.flatten()

        if first.std() == 0 or second.std() == 0:
            raise ValueError("Correlation is undefined when all values are equal.")
        return np.corrcoef(first, second)[0, 1]

    # ---------- Option 1 : Indexing and slicing (after creating an array) ----------
    def array_operations(self):
        while True:
            print("\nChoose an operation : ")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            try:
                choice = self.ask_choice(3)
                if choice == "1":
                    self.indexing()
                elif choice == "2":
                    self.slicing()
                else:
                    break
            except (ValueError, IndexError) as error:
                print(f"\nError: {error}")

    def indexing(self):
        """Get an element, a row or a column. Press Enter to select 'all'."""
        array = self.__array
        print()

        if array.ndim == 1:
            element = self.read_index("Enter the element index (Enter for all) : ")
            result = array[element]
        elif array.ndim == 2:
            row = self.read_index("Enter the row index (Enter for all rows) : ")
            column = self.read_index("Enter the column index (Enter for all columns) : ")
            result = array[row, column]
        else:
            depth = self.read_index("Enter the depth index (Enter for all depths) : ")
            row = self.read_index("Enter the row index (Enter for all rows) : ")
            column = self.read_index("Enter the column index (Enter for all columns) : ")
            result = array[depth, row, column]

        self.show("Indexing Result", result)

    def slicing(self):
        """Get a part (slice) of the array."""
        array = self.__array
        print()

        if array.ndim == 1:
            part = self.read_range("Enter the range (start:end) : ")
            result = array[part]
        elif array.ndim == 2:
            rows = self.read_range("Enter the row range (start:end) : ")
            columns = self.read_range("Enter the column range (start:end) : ")
            result = array[rows, columns]
        else:
            depths = self.read_range("Enter the depth range (start:end) : ")
            rows = self.read_range("Enter the row range (start:end) : ")
            columns = self.read_range("Enter the column range (start:end) : ")
            result = array[depths, rows, columns]

        self.show("Sliced Array", result)

    # ---------- Option 2 : Mathematical operations ----------
    def math_operations(self):
        array = self.__array

        print("\nChoose a mathematical operation : ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")
        choice = self.ask_choice(6)

        if choice in ("5", "6") and array.ndim != 2:
            raise ValueError("Dot product and matrix multiplication need a 2D array.")

        # Read the second array
        print()
        if choice == "6":
            columns = self.ask_whole_number(
                "Enter the number of columns of the second array : "
            )
            if columns < 1:
                raise ValueError("Columns must be greater than zero.")
            shape = (array.shape[1], columns)  # its rows must match our columns
            label = "the second array elements"
        else:
            shape = array.shape
            label = "the same-size array elements"

        size = int(np.prod(shape))
        text = input(f"Enter {label} ({size} elements separated by space) : ")
        second = self.__make_array(text, shape)

        # Calculate and show the result
        name, result = self.__calculate(choice, second)
        self.show("Original Array", array)
        self.show("Second Array", second)
        self.show(f"Result of {name}", result)

    # ---------- Option 3 : Combine or split arrays ----------

    def combine_or_split(self):
        array = self.__array

        print("\nChoose an option : ")
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = self.ask_choice(2)

        print()
        if choice == "1":       # Combine Array
            others = []  # all the extra arrays to combine
            while True:
                text = input(
                    f"Enter the elements of another array to combine "
                    f"({array.size} elements separated by space) : "
                )
                others.append(self.__make_array(text, array.shape))

                again = input("Combine one more array? (y/n) : ").strip().lower()
                if again != "y":
                    break

            combined = np.concatenate([array] + others, axis=0)

            self.show("Original Array", array)
            number = 2
            for other in others:
                title = "Second Array" if number == 2 else f"Array {number}"
                self.show(title, other)
                number += 1

            if array.ndim > 1:
                self.show("Combined Array (Vertical Stack)", combined)
            else:
                self.show("Combined Array", combined)

        else:       # Split Array
            parts = self.ask_whole_number("Enter the number of parts to split into : ")
            if parts < 1 or parts > len(array):
                raise ValueError(f"Parts must be between 1 and {len(array)}.")

            self.show("Original Array", array)
            pieces = np.array_split(array, parts)
            for number, piece in enumerate(pieces, 1):
                self.show(f"Part {number}", piece)

    # ---------- Option 4 : Search, sort or filter ----------
    def search_sort_filter(self):
        print("\nChoose an option : ")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        choice = self.ask_choice(3)

        if choice == "1":
            self.search_value()
        elif choice == "2":
            self.sort_array()
        else:
            self.filter_values()

    def search_value(self):
        array = self.__array
        value = self.ask_number("\nEnter the value to search : ")
        self.show("Original Array", array)

        positions = np.argwhere(array == value)  # one row per match
        if len(positions) == 0:
            print(f"\nValue {value} was not found in the array.")
            return

        print()
        for i in positions:
            print(f"Value {value} found at index {i.tolist()}")

    def sort_array(self):
        array = self.__array

        print("\nChoose the sort order : ")
        print("1. Ascending")
        print("2. Descending")
        choice = self.ask_choice(2)

        sorted_array = np.sort(array)  # sorts every row (last axis)
        if choice == "2":
            sorted_array = np.flip(sorted_array, axis=-1)  # reverse each row

        self.show("Original Array", array)
        self.show("Sorted Array", sorted_array)
        if array.ndim > 1:
            print("(Sorting applied row-wise.)")

    def filter_values(self):
        array = self.__array

        print("\nChoose a condition:")
        print("1. Greater than")
        print("2. Less than")
        print("3. Greater than or equal to")
        print("4. Less than or equal to")
        print("5. Equal to")
        print("6. Not equal to")
        choice = self.ask_choice(6)
        value = self.ask_number("\nEnter the value : ")

        mask = self.__make_mask(choice, value)
        result = array[mask]  # keeps only the elements where mask is True

        self.show("Original Array", array)
        if len(result) == 0:
            print("\nNo values match the condition.")
        else:
            self.show("Filtered Values", result)

    # ---------- Option 5 : Aggregates and statistics ----------
    def aggregates_and_statistics(self):
        array = self.__array

        print("\nChoose an aggregate/statistical operation : ")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation Coefficient")
        choice = self.ask_choice(9)

        second = None  # only used for the correlation coefficient

        match choice:
            case "1":
                label, result = "Sum of Array", np.sum(array)
            case "2":
                label, result = "Mean of Array", np.mean(array)
            case "3":
                label, result = "Median of Array", np.median(array)
            case "4":
                label, result = "Standard Deviation of Array", np.std(array)
            case "5":
                label, result = "Variance of Array", np.var(array)
            case "6":
                label, result = "Minimum of Array", np.min(array)
            case "7":
                label, result = "Maximum of Array", np.max(array)
            case "8":
                percent = self.ask_number("\nEnter the percentile (0-100) : ")
                label = f"{percent}th Percentile of Array"
                result = np.percentile(array, percent)
            case "9":
                print()
                text = input(
                    f"Enter the elements of another array "
                    f"({array.size} elements separated by space) : "
                )
                second = self.__make_array(text, array.shape)
                label = "Correlation Coefficient between Arrays"
                result = self.__correlation(second)

        self.show("Original Array", array)
        if second is not None:
            self.show("Second Array", second)
        print(f"\n{label}: {result}")


# ---------- Main program ----------
analyzer = None  # no array yet
DataAnalytics.show_welcome()

while True:
    print("Choose an option :")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")

    try:
        choice = DataAnalytics.ask_choice(6)

        if choice in ("2", "3", "4", "5") and analyzer is None:
            raise ValueError("Please create an array first (option 1).")

        match choice:
            case "1":
                analyzer = DataAnalytics.create_array()
                analyzer.array_operations()
            case "2":
                analyzer.math_operations()
            case "3":
                analyzer.combine_or_split()
            case "4":
                analyzer.search_sort_filter()
            case "5":
                analyzer.aggregates_and_statistics()
            case "6":
                DataAnalytics.show_goodbye()
                break
    except (ValueError, IndexError) as error:
        print(f"\nError : {error}")

    print()
