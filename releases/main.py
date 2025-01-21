from string import ascii_uppercase
import yaml
import os

translations_file = r'releases/translations.yaml'
if not os.access(translations_file, os.R_OK):
    translations_file = r'translations.yaml'

def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

def read_translations_yaml(file_path=translations_file):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            # Load the full YAML content
            full_content: dict = yaml.safe_load(file)

        default_lang = full_content["default_lang"]
        available_langs = list(full_content.keys())[1:]
    except Exception as e:
        print("An error occured while reading the translations.yaml file:", e)
        exit()

    return (default_lang, available_langs, full_content)

default_lang, available_langs, full_content = read_translations_yaml()

def invalid_language_code(language_code):

    if language_code in full_content:
        # language_code = default_lang
        return True
    else:
        return False

def get_language_choice(language_code: str) -> dict:
    cls()
    global default_lang
    global available_langs
    global full_content

    if default_lang not in available_langs:
        raise ValueError("The selected default language is unavailable. Check the translations.yaml for more information.")

    if invalid_language_code(default_lang):
        return full_content[language_code]
    else:
        raise ValueError(f"Language '{language_code}' not found in the translations file.")
    
LANGUAGE = get_language_choice(default_lang)

def change_language():
    global LANGUAGE
    inp_lang = input(LANGUAGE["input_change_lang"]).lower()
    
    if invalid_language_code(inp_lang):
        LANGUAGE = get_language_choice(inp_lang)

        with open(translations_file, 'r', encoding="utf-8") as file:
            file_lines = file.readlines()

        if file_lines:
            file_lines[0] = file_lines[0][:-3] + inp_lang + "\n"

        with open(translations_file, 'w', encoding='utf-8') as file:
            file.writelines(file_lines)
    else:
        raise ValueError(f"Language '{inp_lang}' not found in the translations file.")



def invalid_input() -> None:
    print(LANGUAGE["invalid_input"])
    exit()

def wait_respond():
    input(LANGUAGE["input_wait_respond"])

def left_shift(lst, n):
    # This code has been with chatGPT generated
    n = n % len(lst)  # Ensure n is within the bounds of the list length
    return lst[n:] + lst[:n]

def get_shifted_dict():
    shifting_num = input(LANGUAGE["input_shift_amount"])
    if shifting_num.isdigit() and shifting_num in [str(num) for num in range(len(ascii_uppercase))]:
        shifting_num = int(shifting_num)

        clear_row = list(ascii_uppercase)
        krypto_row = left_shift(clear_row, shifting_num)

        the_row = {clear:krypto for clear, krypto in zip(clear_row, krypto_row)}
    else:
        invalid_input()
    return the_row

def encrypt_cleartext():
    klartext = input(LANGUAGE["input_plaintext"] + "\n")
    shifted_dict = get_shifted_dict()
    krypto_text = ""
    for char in klartext:
        if char.upper() in ascii_uppercase:
            krypto_text += shifted_dict[char.upper()]
        else:
            krypto_text += char
    print(LANGUAGE["encrypted_text"])
    print(krypto_text)


def decrypt_kryptotext():
    kryptotext = input(LANGUAGE["input_decrypted_text"] + "\n")
    shifted_dict = get_shifted_dict()
    shifted_dict = {b:a for a, b in shifted_dict.items()}
    cleartext = ""
    for char in kryptotext:
        if char.upper() in ascii_uppercase:
            cleartext += shifted_dict[char.upper()]
        else:
            cleartext += char.upper()
    print(LANGUAGE["decrypted_text"])
    print(cleartext)

def show_caesar_cipher_disk():
    # Short notice: the above code is written with chatGPT - it's not my code, unfortunately, because I couldn't.
    import matplotlib.pyplot as plt
    import numpy as np

    shift = input(LANGUAGE["input_inner_disc_shift"])
    if not shift.isdigit() and shift in range(26):
        invalid_input()

    # !!! DO NOT CHANGE THE ORDER OF THE LETTERS !!!
    # THEY HAVE BRUTEFORCED TO FIND THE BEST ORDER
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

def refresh_options():
    global options
    options = [(1, LANGUAGE["opt_encrypt_plaintext"]),
            (2, LANGUAGE["opt_decrypt_text"]),
            (3, LANGUAGE["opt_show_disc"]),
            (4, LANGUAGE["opt_change_lang"]),
            (5, LANGUAGE["opt_exit"])
            ]
refresh_options()

while True:
    cls()
    for i, opt in options:
        print(f"{i}.  {opt}")
    opt = input("=> ")

    if opt.isdigit() and opt in [str(i[0]) for i in options]:
        if opt == "5":
            print("Bye")
            exit()
        elif opt == "1":
            encrypt_cleartext()
            wait_respond()
        elif opt == "2":
            decrypt_kryptotext()
            wait_respond()
        elif opt == "3":
            show_caesar_cipher_disk()
        elif opt == "4":
            change_language()
            refresh_options()
            continue
        else:
            invalid_input()
    else:
        invalid_input()
