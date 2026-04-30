#Problem 1

def problem_1():
    print("--- Problem 1: Compound Interest ---")
    principal = float(input("Principal: "))
    rate = float(input("Rate: "))
    years = int(input("Years: "))
    
    current_balance = principal

for year in range(1, years + 1):
    current_balance = current_balance * (1 + rate / 100)
    print (f"Year {year}: ${current_balance:.2f}")

    total_interest = current_balance - principal 
    print(f"Total Interest earned: ${current_balance:.2f}")




# Pronlem 2

def caesar_encode(text, shift):
    result = ""

    for ch in text:
        if not ch.isalpha():
            result += ch
        else:
         start = ord('A') if ch.isupper() else ord('a')

        shifted_char = chr((ord(ch) - start + shift) % 26 + start)
        result += shifted_char

    return result

def test_problem_2():
    print ("--- Problem 2: Ceasar Cipher ---")
    print(ceaser_encode("Hello, World!", 3))
    print(ceaser_encode("abc xyz", 2))
    print(ceaser_encode("Python 3"))