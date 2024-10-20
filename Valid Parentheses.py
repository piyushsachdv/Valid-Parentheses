class Solution:
    def is_valid(self, s):
        # Create a mapping of closing brackets to their corresponding opening brackets
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        # Initialize a stack to keep track of opening brackets
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the topmost element from the stack if it's not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched correctly
        return not stack

    # Adding the isValid attribute
    isValid = is_valid  # This creates an alias for the method

# Example usage
solution = Solution()
s = "({[]})"  # Example of a valid string
result = solution.isValid(s)  # Using the new attribute
print("The string '" + s + "' is valid: " + str(result))

s2 = "([)]"  # Example of an invalid string
result2 = solution.isValid(s2)  # Using the new attribute
print("The string '" + s2 + "' is valid: " + str(result2))
