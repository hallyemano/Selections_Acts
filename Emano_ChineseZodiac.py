def find_chinese_zodiac_sign(year):
    zodiac_signs = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse",
                    "Sheep"]
    year_difference = year - 1944

    zodiac_index = year_difference % 12
    return zodiac_signs[zodiac_index]

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    zodiac_sign = find_chinese_zodiac_sign(year)
    print(f"The Chinese Zodiac sign for the year {year} is {zodiac_sign}.")






