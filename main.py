def greeting():
    return "Hello! There"


def calculate_pi(n):
    """
    Calculate pi to the nth digit after the decimal point.
    
    Args:
        n: Number of digits after the decimal point
        
    Returns:
        String representation of pi with n digits after decimal point
    """
    try:
        from mpmath import mp
        
        # Set precision high enough to get n digits
        # We need extra precision for intermediate calculations
        mp.dps = n + 10
        
        # Calculate pi using mpmath
        pi_value = mp.pi
        
        # Convert to string and format to exactly n decimal places
        pi_str = str(pi_value)
        
        # Find decimal point
        if '.' in pi_str:
            integer_part, decimal_part = pi_str.split('.')
            # Ensure we have exactly n digits after decimal
            if len(decimal_part) >= n:
                result = f"{integer_part}.{decimal_part[:n]}"
            else:
                result = f"{integer_part}.{decimal_part.ljust(n, '0')}"
        else:
            result = f"{pi_str}.{'0' * n}"
            
        return result
        
    except ImportError:
        # Fallback implementation using Machin's formula if mpmath not available
        from decimal import Decimal, getcontext
        
        # Set precision high enough
        getcontext().prec = n + 50
        
        def arctan(x, num_terms=500):
            """Calculate arctan using Taylor series"""
            x = Decimal(x)
            power = x
            result = power
            for i in range(1, num_terms):
                power *= -x * x
                result += power / (2 * i + 1)
            return result
        
        # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
        one = Decimal(1)
        pi_over_4 = 4 * arctan(one/5) - arctan(one/239)
        pi_value = 4 * pi_over_4
        
        # Format to n decimal places
        pi_str = str(pi_value)
        if '.' in pi_str:
            integer_part, decimal_part = pi_str.split('.')
            if len(decimal_part) >= n:
                result = f"{integer_part}.{decimal_part[:n]}"
            else:
                result = f"{integer_part}.{decimal_part.ljust(n, '0')}"
        else:
            result = f"{pi_str}.{'0' * n}"
            
        return result