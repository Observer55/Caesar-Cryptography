from string import ascii_uppercase

def invalid_input() -> None:
    # print("Invalid input. Restart the program to retry.")
    print("Ungültige Eingabe. Starten Sie das Programm neu, um es erneut zu versuchen.")
    exit()

def left_shift(lst, n):
    n = n % len(lst)  # Ensure n is within the bounds of the list length
    return lst[n:] + lst[:n]

def get_shifted_dict():
    shifting_num = input("Um wie viel Zahlen ist die Schiebe verschieben? ")
    if shifting_num.isdigit() and shifting_num in [str(num) for num in range(len(ascii_uppercase))]:
        shifting_num = int(shifting_num)

        clear_row = list(ascii_uppercase)
        krypto_row = left_shift(clear_row, shifting_num)

        the_row = {clear:krypto for clear, krypto in zip(clear_row, krypto_row)}
    else:
        invalid_input()
    return the_row

def encrypt_cleartext():
    klartext = input("Schreibe deine Klartext:\n")
    shifted_dict = get_shifted_dict()
    krypto_text = ""
    for char in klartext:
        if char.upper() in ascii_uppercase:
            krypto_text += shifted_dict[char.upper()]
        else:
            krypto_text += char
    print("Verschlüsselte Klartext:")
    print(krypto_text)


def decrypt_kryptotext():
    kryptotext = input("Schreibe die Kryptotext:\n")
    shifted_dict = get_shifted_dict()
    shifted_dict = {b:a for a, b in shifted_dict.items()}
    cleartext = ""
    for char in kryptotext:
        if char.upper() in ascii_uppercase:
            cleartext += shifted_dict[char.upper()]
        else:
            cleartext += char.upper()
    print("Entschlüsselte Geheimtext (Kryptotext):")
    print(cleartext)

def show_caesar_cipher_disk():
    import matplotlib.pyplot as plt
    import numpy as np

    shift = input("Wie viel soll die innere Scheibe verschoben? ")
    if not shift.isdigit() and shift in range(26):
        invalid_input()

    # !!! DO NOT CHANGE THE ORDER OF THE LETTERS !!!
    outer_letters = list("BCDEFGHIJKLMNOPQRSTUVWXYZA")[::-1]
    inner_letters = list("BCDEFGHIJKLMNOPQRSTUVWXYZA")[::-1]
    # popped = outer_letters.pop(0)
    # outer_letters = outer_letters + list(popped)
    # # outer_letters = outer_letters[::-1]

    inner_letters = left_shift(inner_letters, -1 * int(shift))

    # Create a figure and a single subplot
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.set_aspect('equal')

    # Define radius for outer and inner circles
    radius_outer = 1
    radius_inner = 0.8

    # Calculate angles for each letter
    theta = np.linspace(0, 2 * np.pi, len(outer_letters), endpoint=False) + np.pi / 2

    # Draw the outer circle letters
    for i, letter in enumerate(outer_letters):
        x = radius_outer * np.cos(theta[i])
        y = radius_outer * np.sin(theta[i])
        ax.text(x, y, letter, ha='center', va='center', fontsize=14, fontweight='bold')

    # Draw the inner circle letters
    for i, letter in enumerate(inner_letters):
        x = radius_inner * np.cos(theta[i])
        y = radius_inner * np.sin(theta[i])
        ax.text(x, y, letter, ha='center', va='center', fontsize=12)

    plt.subplots_adjust(left=0.35, bottom=0.5, right=1.0, top=0.9, wspace=0.2, hspace=0.2)

    # Remove axes
    ax.axis('off')
    # Display the plot
    plt.show()

options = [(1, "Verschlüsse Klartext"),
           (2, "Entschlüsse Geheimtext (oder Chiffre/Kryptotext)"),
           (3, "Sehe die Cäser Chiffrierscheibe"),
           (4, "Exit")
           ]

for i, opt in options:
    print(f"{i}.  {opt}")
opt = input("=> ")

if opt.isdigit() and opt in [str(i[0]) for i in options]:
    if opt == "4":
        print("Bye")
        exit()
    elif opt == "1":
        encrypt_cleartext()
    elif opt == "2":
        decrypt_kryptotext()
    elif opt == "3":
        show_caesar_cipher_disk()
    else:
        invalid_input()
else:
    invalid_input()
