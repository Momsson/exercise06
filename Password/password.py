def analyze_password(
    password,
    min_length=8,
    require_digit=True,
    require_upper=True,
    require_symbol=False,
    banned_words=None
):

    if banned_words is None:
        banned_words = ['heslo', 'password', '1234']

    symbols = "!@#$%^&*()-_=+[]{};:,.?"

    missing_rules = []
    active_rules = 0
    passed_rules = 0

    # kontrola délky
    active_rules += 1
    if len(password) >= min_length:
        passed_rules += 1
    else:
        missing_rules.append("min_length")

    # číslice
    if require_digit:
        active_rules += 1
        if any(c.isdigit() for c in password):
            passed_rules += 1
        else:
            missing_rules.append("digit")

    # velké písmeno
    if require_upper:
        active_rules += 1
        if any(c.isupper() for c in password):
            passed_rules += 1
        else:
            missing_rules.append("upper")

    # symbol
    if require_symbol:
        active_rules += 1
        if any(c in symbols for c in password):
            passed_rules += 1
        else:
            missing_rules.append("symbol")

    # banned words
    active_rules += 1
    password_lower = password.lower()

    if any(word in password_lower for word in banned_words):
        missing_rules.append("banned_word")
    else:
        passed_rules += 1

    score_percent = int((passed_rules / active_rules) * 100)
    is_strong = passed_rules == active_rules

    return is_strong, score_percent, missing_rules


# ======================
# INPUT OD UŽIVATELE
# ======================

password = input("Zadej heslo: ")

result = analyze_password(password)

print("\nVýsledek analýzy:")
print("Silné heslo:", result[0])
print("Score:", result[1], "%")
print("Chybějící pravidla:", result[2])