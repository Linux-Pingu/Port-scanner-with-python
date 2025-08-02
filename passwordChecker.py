import re

def check_password_strength(password):
    # Minimum password length
    min_length = 8

    # Initialize strength level
    strength = 0
    feedback = []

    # Check length
    if len(password) >= min_length:
        strength += 1
    else:
        feedback.append("Password is too short (minimum 8 characters)")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter")

    # Check for digits
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one number")

    # Check for special characters
    if re.search(r"[\W_]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character (e.g., !@#$)")

    # Determine strength level
    if strength == 5:
        return "Very Strong "
    elif strength >= 4:
        return "Strong ✅"
    elif strength >= 3:
        return "Moderate ⚠️"
    else:
        return "Weak ❌\n" + "\n".join(feedback)


# Example usage
if name == "__main__":
    user_password = input("Enter a password to check: ")
    result = check_password_strength(user_password)
    print(f"\nPassword Strength: {result}")


# Linux-Pingu
