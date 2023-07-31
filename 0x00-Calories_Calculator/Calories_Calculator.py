age = int(input("age: "))
weigth = float(input("weigth: "))
heigth = float(input("heigth: "))
gender = input("Gender: ")

def male(age, weigth, heigth):
    BMR_male = ((weigth * 10) + (heigth * 6.25) - (age * 5) + 5)
    return BMR_male

BMR_male = male(age,weigth,heigth)

def female(age, weigth, heigth):
    BMR_female = ((weigth * 10) + (heigth * 6.25) - (age * 5) - 161)
    return BMR_female

BMR_female = female(age, weigth, heigth)

if gender.lower() == "male":
    print()
    print(f"{round(BMR_male,2)}")
    print()
    TDEE_male = input(f"Sedentary: little or no exercise\n"
                      f"Light: exercise 1-3 times/week\nModerate: exercise 4-5 times/week\n"
                      f"Active: exercise 6 times/week\n"
                      f"Very Active: very intense exercise daily, or physical job\n").strip().capitalize()
    print()
    if TDEE_male == "Sedentary":
        print(f"{round(BMR_male * 1.2,2)}")
    elif TDEE_male == "Light":
        print(f"{round(BMR_male * 1.35,2)}")
    elif TDEE_male == "Moderate":
        print(f"{round(BMR_male * 1.5,2)}")
    elif TDEE_male == "Active":
        print(f"{round(BMR_male * 1.7,2)}")
    elif TDEE_male == "Very Active":
        print(f"{round(BMR_male * 1.9,2)}")
    print()

elif gender.lower() == "female":
    print()
    print(f"{round(BMR_female,2)}")
    print()
    TDEE_female = input(f"Sedentary: little or no exercise\n"
                        f"Light: exercise 1-3 times/week\n"
                        f"Moderate: exercise 4-5 times/week\n"
                        f"Active: exercise 6 times/week\n"
                        f"Very Active: very intense exercise daily, or physical job\n").strip().capitalize()
    print()
    if TDEE_female == "Sedentary":
        print(f"{round(BMR_female * 1.2,2)}")
    elif TDEE_female == "Light":
        print(f"{round(BMR_female * 1.35,2)}")
    elif TDEE_female == "Moderate":
        print(f"{round(BMR_female * 1.5,2)}")
    elif TDEE_female == "Active":
        print(f"{round(BMR_female * 1.7,2)}")
    elif TDEE_female == "Very Active":
        print(f"{round(BMR_female * 1.9,2)}")
    print()
else:
    print()
    print("\033[31m Sorry! there is only two genders\033[0m")
    exit()
