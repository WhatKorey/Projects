import string

def check_password_strength(password):
    length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([length, has_upper, has_lower, has_number, has_special])

    if score == 5:
        return "Strong password 💪"
    elif score >= 3:
        return "Moderate password 😐"
    else:
        return "Weak password ⚠️"


user_password = input("Enter a password to check: ")
print(check_password_strength(user_password))
