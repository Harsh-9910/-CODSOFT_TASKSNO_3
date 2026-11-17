# 🔐 Task 3: Password Generator

![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Type-Command--Line-blue)
![Security](https://img.shields.io/badge/Randomness-secrets%20module-red)

A tool that generates strong, random passwords. You choose the length and the complexity, and the program prints the result.

## 📌 Features

- Password length from **4 to 128** characters
- Three complexity levels
- Uses Python's **`secrets`** module, which is designed for security-sensitive randomness (unlike `random`)
- Guarantees that every character type in the chosen level appears at least once
- Validates all input and lets you generate as many passwords as you like

## 🎚️ Complexity Levels

| Level | Name | Characters used |
|-------|------|-----------------|
| 1 | Low | Letters (`a-z`, `A-Z`) |
| 2 | Medium | Letters + digits |
| 3 | High | Letters + digits + symbols (`!@#$%^&*...`) |

## ▶️ How to Run

```bash
python task3_password_generator.py
```

No external libraries are required.

## 🖥️ Example Session

```
===== PASSWORD GENERATOR =====
Desired password length (4-128): 16

Complexity:
  1. Low (letters only)
  2. Medium (letters + digits)
  3. High (letters + digits + symbols)
Choose complexity (1-3): 3

Generated password: 46=]HZq:lLx|%5mh

Generate another? (y/n): n
Goodbye!
```

> The password is random, so your output will be different every time.

## 🧠 How It Works

1. The user enters a length and a complexity level.
2. The level selects a character set built from the `string` module.
3. `generate_password()` picks each character using `secrets.choice()`.
4. It checks that every character type in the set is present (lowercase, uppercase, digits, symbols as applicable). If not, it generates again.
5. The password is printed on screen.

| Part | Purpose |
|------|---------|
| `LEVELS` | Maps menu choices to a description and a character set |
| `generate_password(length, charset)` | Builds and returns the password |
| `main()` | Handles input, validation and the menu loop |

## 💡 Tips for Strong Passwords

- Use **12 characters or more**
- Prefer the **High** level where the website allows symbols
- Use a different password for every account and store them in a password manager

## 📚 Concepts Used

Functions, dictionaries, generator expressions, `while` loops, input validation, the `string` and `secrets` modules.

## 🔮 Ideas for Improvement

- Password strength meter
- Copy-to-clipboard option
- Option to exclude look-alike characters (`O`, `0`, `l`, `1`)

