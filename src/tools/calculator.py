# src/tools/calculator.py

def calculate(expression: str) -> str:
    """
    Calculates the result of a given mathematical expression and returns it as a string.
    Example: "2+2*5" -> "12"
    """
    try:
        # The 'eval' function executes a string as Python code.
        # It's generally safe for simple math operations but should be used with caution,
        # as it can execute arbitrary code if the input is not sanitized.
        # For our controlled use case, it's acceptable.
        result = str(eval(expression))
        return f"Calculation result: {result}"
    except Exception as e:
        return f"Error during calculation: {str(e)}. Please enter a valid mathematical expression (e.g., '5*2+1')."
