import math
import string

def password_entropy(password):
    charset = 0
    if any(c in string.ascii_lowercase for c in password):
        charset += 26
    if any(c in string.ascii_uppercase for c in password):
        charset += 26
    if any(c in string.digits for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += 32
    entropy = len(password) * math.log2(charset) if charset else 0
    return entropy

password = input("Enter password: ")
entropy = password_entropy(password)
print(f"Password Entropy: {entropy:.2f} bits")
if entropy < 50:
    print("Strength: Weak")
elif entropy < 80:
    print("Strength: Moderate")
else:
    print("Strength: Strong")