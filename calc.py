Absolutely! Here's the Python script to calculate the average of a list, ready to be saved as `calc.py`.


# calc.py

def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list): A list of numerical values (integers or floats).

    Returns:
        float: The average of the numbers in the list.
               Returns 0 if the list is empty to prevent division by zero errors.
    """
    if not numbers:  # Check if the list is empty
        print("Warning: The list is empty. Returning 0 as the average.")
        return 0.0
    
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average

# --- Example Usage ---
if __name__ == "__main__":
    # Test cases
    list1 = [10, 20, 30, 40, 50]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list3 = [2.5, 3.5, 4.0]
    empty_list = []
    single_element_list = [100]

    print(f"List 1: {list1}")
    print(f"Average of List 1: {calculate_average(list1):.2f}\n")

    print(f"List 2: {list2}")
    print(f"Average of List 2: {calculate_average(list2):.2f}\n")

    print(f"List 3: {list3}")
    print(f"Average of List 3: {calculate_average(list3):.2f}\n")

    print(f"Empty List: {empty_list}")
    print(f"Average of Empty List: {calculate_average(empty_list):.2f}\n")

    print(f"Single Element List: {single_element_list}")
    print(f"Average of Single Element List: {calculate_average(single_element_list):.2f}\n")

    # You can also get input from the user (optional)
    # user_input = input("Enter numbers separated by spaces to calculate their average: ")
    # try:
    #     user_numbers = [float(x) for x in user_input.split()]
    #     print(f"Average of your numbers: {calculate_average(user_numbers):.2f}")
    # except ValueError:
    #     print("Invalid input. Please enter numbers only.")



**To save and run this code:**

1.  **Open a text editor** (like Notepad, VS Code, Sublime Text, or even a simple IDE).
2.  **Copy the entire code block** above.
3.  **Paste it** into the text editor.
4.  **Save the file** as `calc.py` in a directory of your choice.
5.  **Open a terminal or command prompt**, navigate to the directory where you saved `calc.py`.
6.  **Run the script** using the command: `python calc.py`

This script defines a function `calculate_average` that takes a list of numbers and returns their average. It also includes some example usage within the `if __name__ == "__main__":` block, which means these examples will run automatically when you execute the script directly.