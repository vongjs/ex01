def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 16:
        print("You are Severe Thinness.")
    elif 16 <= bmi < 17:
        print("You are Moderate Thinness.")
    elif 17 <= bmi < 18.5:
        print("You are Mild Thinness.")
    elif 18.5 <= bmi < 25:
        print("You are Normal.")
    elif 25 <= bmi < 30:
        print("You are Overweight.")
    elif 30 <= bmi < 35:
        print("You are Obese Class |.")
    elif 35 <= bmi < 40:
        print("You are Obese Class ||.")
    else:
        print("You are Obese Class |||.")


if __name__ == "__main__":
    main()
