
numbers = [15, 83, 4, 62, 29, 77, 41, 93, 11, 50]

def largest_value(numbers, startpos):
    current = numbers[startpos]

    print(f"CALL: startpos={startpos}, current={current}")

    # Base case
    if startpos == len(numbers) - 1:
        print(f"BASE CASE: Returning {current}")
        return current

    # Recursive call
    largest_remaining = largest_value(numbers, startpos + 1)

    # Compare the values
    print(f"COMPARE: {current} vs {largest_remaining}")

    if current < largest_remaining:
        print(f"RETURN: {largest_remaining} is larger")
        return largest_remaining
    else:
        print(f"RETURN: {current} is larger")
        return current

print("\nFINAL ANSWER:", largest_value(numbers, 0))
