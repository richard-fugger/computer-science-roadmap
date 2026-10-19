# Day 3 - Practical Exercises
#
# 1. Write a function that raises ValueError(...) when given a negative value.
#
# 2. Create your own custom exception and raise it deliberately.
#
# 3. Use try/except/else/finally once, and then describe when each block was executed.

class InvalidInputData(Exception):
    pass

def calculate_bmi_v1(weight: float, size_in_m: float) -> float:
    if weight <= 0 or size_in_m <= 0:
        raise ValueError(f"weight or size must be greater than 0. Weight: {weight}, Size: {size_in_m}")
    return weight / (size_in_m * size_in_m)

def calculate_bmi_v2(weight: float, size_in_m: float) -> float:
    if weight <= 0 or size_in_m <= 0:
        raise InvalidInputData(f"weight or size must be greater than 0. Weight: {weight}, Size: {size_in_m}")
    return weight / (size_in_m * size_in_m)


def main():
    try:
        bmi = calculate_bmi_v2(69, 1.79)
    except InvalidInputData as error:
        print(error)

    else: print(bmi)

    finally: print("BMI calculation finished.")

if __name__ == "__main__":
    main()