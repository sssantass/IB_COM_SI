def factorial(n):
    if n==0:
        print("N=0")
        return 1
    print(f"N={n}")
    return n*factorial(n-1)
print(factorial(5))

def mystery(n):
    if n == 1:
        return 1
    return n + mystery(n - 2)

def factorial_recursive(n, depth=0):
    indent = "  " * depth  # Visual spacing based on recursion depth
    
    # 1. WINDING PHASE (Going deeper into calls)
    print(f"{indent}⬇️  Winding: factorial_recursive({n}) called")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Base cases
    if n == 0 or n == 1:
        print(f"{indent}🎯 Base case reached: factorial_recursive({n}) = 1")
        print(f"{indent}⬆️  Unwinding: returning 1")
        return 1
    
    # Recursive step
    result = n * factorial_recursive(n - 1, depth + 1)
    
    # 2. UNWINDING PHASE (Returning back up the call stack)
    print(f"{indent}⬆️  Unwinding: factorial_recursive({n}) calculated {n} * factorial_recursive({n - 1}) = {result}")
    return result

print("=== Execution Trace ===")
final_result = factorial_recursive(5)
print(f"\nFinal Result: {final_result}")