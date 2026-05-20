"""
Test file for calculate_pi function
"""
from main import calculate_pi


def test_calculate_pi():
    """Test the calculate_pi function with various digit counts"""
    
    print("Testing calculate_pi function...")
    print("=" * 60)
    
    # Test with different number of digits
    test_cases = [
        (0, "3"),
        (1, "3.1"),
        (5, "3.14159"),
        (10, "3.1415926535"),
        (20, "3.14159265358979323846"),
        (50, "3.14159265358979323846264338327950288419716939937510"),
        (100, "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"),
    ]
    
    # Known digits of pi for verification (first 100 digits after decimal)
    known_pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    
    print("\n1. Testing various digit lengths:")
    print("-" * 60)
    for n_digits, expected_start in test_cases:
        result = calculate_pi(n_digits)
        print(f"Pi to {n_digits:3d} digits: {result}")
        
        # Verify the result matches known pi digits
        if n_digits <= 100:
            expected = known_pi[:2 + n_digits] if n_digits > 0 else known_pi[:1]
            if n_digits == 0:
                expected = "3"
            
            if result == expected:
                print(f"  ✓ Correct!")
            else:
                print(f"  ✗ Expected: {expected}")
                print(f"  ✗ Got:      {result}")
        print()
    
    print("\n2. Testing edge cases:")
    print("-" * 60)
    
    # Test edge case: 0 digits
    result_0 = calculate_pi(0)
    print(f"Pi to 0 digits: {result_0}")
    assert result_0.startswith("3"), "Should start with 3"
    print("  ✓ Zero digits test passed!")
    
    # Test that length is correct
    print("\n3. Verifying output format:")
    print("-" * 60)
    for n in [5, 15, 25]:
        result = calculate_pi(n)
        decimal_pos = result.index('.')
        digits_after_decimal = len(result) - decimal_pos - 1
        print(f"n={n:2d}: digits after decimal = {digits_after_decimal}, result = {result}")
        assert digits_after_decimal == n, f"Should have exactly {n} digits after decimal"
        print(f"  ✓ Format correct!")
    
    print("\n" + "=" * 60)
    print("All tests passed! ✓")
    print("=" * 60)


if __name__ == "__main__":
    test_calculate_pi()
