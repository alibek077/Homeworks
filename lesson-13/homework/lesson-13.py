from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import re
from zoneinfo import ZoneInfo
import time




#1 Age Calculator



def calculate_age(birth_str):
    birth_date = datetime.strptime(birth_str, "%d.%m.%Y").date()
    today = datetime.today().date()
    age = relativedelta(today, birth_date)
    return age

birth_input = input("\n#1 Enter your birthdate (dd.mm.yyyy): ")
age = calculate_age(birth_input)
print(f"You are {age.years} years, {age.months} months, and {age.days} days old.")




 #2 Days Until Next Birthday


def days_until_birthday(birth_str):
    birth_date = datetime.strptime(birth_str, "%d.%m.%Y").date()
    today = date.today()
    next_birthday = birth_date.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    return (next_birthday - today).days

birth_input = input("\n#2 Enter your birthdate (dd.mm.yyyy): ")
days = days_until_birthday(birth_input)
print(f"Your next birthday is in {days} days.")



 #3 Meeting Scheduler

def schedule_meeting(current_str, hours, minutes):
    current_dt = datetime.strptime(current_str, "%d.%m.%Y %H:%M")
    duration = timedelta(hours=hours, minutes=minutes)
    end_dt = current_dt + duration
    return end_dt

current_input = input("\n#3 Enter current date and time (dd.mm.yyyy HH:MM): ")
hours = int(input("Enter meeting duration (hours): "))
minutes = int(input("Enter meeting duration (minutes): "))
end_time = schedule_meeting(current_input, hours, minutes)
print(f"The meeting will end at: {end_time.strftime('%d.%m.%Y %H:%M')}")






 #4 Timezone Converter



def convert_timezone(datetime_str, from_tz_str, to_tz_str):
    naive_dt = datetime.strptime(datetime_str, "%d.%m.%Y %H:%M")
    from_dt = naive_dt.replace(tzinfo=ZoneInfo(from_tz_str))
    to_dt = from_dt.astimezone(ZoneInfo(to_tz_str))
    return to_dt

datetime_input = input("\n#4 Enter date and time (dd.mm.yyyy HH:MM): ")
from_timezone = input("Enter your current timezone (e.g. Asia/Tashkent): ")
to_timezone = input("Enter target timezone (e.g. Europe/London): ")
converted = convert_timezone(datetime_input, from_timezone, to_timezone)
print(f"Converted time: {converted.strftime('%d.%m.%Y %H:%M (%Z)')}")




 #5 Countdown Timer


def countdown_timer(future_str):
    future_time = datetime.strptime(future_str, "%d.%m.%Y %H:%M:%S")
    while True:
        now = datetime.now()
        if future_time <= now:
            print("\n Time is up!")
            break
        remaining = future_time - now
        print(f"\rTime left: {remaining}", end="")
        time.sleep(1)

future_input = input("\n#5 Enter a future date and time (dd.mm.yyyy HH:MM:SS): ")
countdown_timer(future_input)



#6 Email Validator


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

email_input = input("\n#6 Enter your email address: ")
if is_valid_email(email_input):
    print("Valid email address.")
else:
    print("Invalid email address.")




#7 Phone Number Formatter


def format_phone_number(number_str):
    digits = ''.join(filter(str.isdigit, number_str))
    formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    return formatted

phone_input = input("\n#7 Enter a 10-digit phone number: ")
formatted_number = format_phone_number(phone_input)
print(f"Formatted number: {formatted_number}")




 #8 Password Strength Checker


def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    long_enough = len(password) >= 8

    if all([has_upper, has_lower, has_digit, long_enough]):
        return " Strong password."
    else:
        return "Weak password. Must be at least 8 characters long and contain uppercase, lowercase, and digit."

password_input = input("\n#8 Enter your password: ")
result = check_password_strength(password_input)
print(result)




#9 Word Finder

def find_word_occurrences(text, word):
    positions = []
    start = 0
    while True:
        index = text.lower().find(word.lower(), start)
        if index == -1:
            break
        positions.append(index)
        start = index + len(word)
    return positions

sample_text = """
Python is a powerful language. Many developers love Python because Python is simple and readable.
"""
search_word = input("\n#9 Enter a word to search for: ")
positions = find_word_occurrences(sample_text, search_word)
print(f"The word '{search_word}' was found at positions: {positions}")





#10 Date Extractor

def extract_dates(text):
    pattern = r'\b\d{2}\.\d{2}\.\d{4}\b'
    return re.findall(pattern, text)

user_text = input("\n#10 Enter a text with dates (e.g., 30.07.2025): ")
found_dates = extract_dates(user_text)
print(f"Found dates: {found_dates}")
