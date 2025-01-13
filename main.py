from string import ascii_uppercase

class Encrypiton:
    def __init__(self, shift_count: None):
        self.__SHIFT = shift_count if shift_count != None else 0
        # self.__character_dict = {}
        self.__setup_characters()

    def __setup_character(self) -> None:
        self.characters_dict = {}
        for char in ascii_uppercase:
            self.characters_dict[char] = None # change this!



if __name__ == "__main__":
    myEncryptionApp = Encrypiton()
    myEncryptionApp.SHIFT = 2
    plain_text = "Hello user"
    print(plain_text)
    encrypted_text = myEncryptionApp.encrypt()
    print(encrypted_text)

    decrypted_text = myEncryptionApp.decrypt(encrypted_text, 2) # the second argument is not necessary. If it's present, then the decryption proccess will use it to shift, otherwise it's going to use the default value (Encryption.SHIFT)
    print(decrypted_text)