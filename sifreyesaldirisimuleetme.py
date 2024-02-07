import hashlib
# yaygın olarak kullanılan şifrelerin varyasyonları
common_passwords = ["password", "password123", "letmein", "qwerty",
                    "123456", "abc123", "admin", "welcome", "monkey", "sunshine"]
password_variations = ["", "123", "1234", "12345", "123456", "!", "@", "#", "$", "%", "^",
                       "&", "*", "(", ")", "-", "_", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "<", ">"]

hashed_password = hashlib.sha256(b"mypass12#@").hexdigest()
# Var olan tüm kombinasyonların deneme
for password in common_passwords:
    for variation in password_variations:
        possible_password = password + variation
        hashed_possible_password = hashlib.sha256(
            possible_password.encode()).hexdigest()
        if hashed_possible_password == hashed_password:
            print(f"Password found: {possible_password}")
            break
    else:
        continue
    break
else:
    print("Password not found")
