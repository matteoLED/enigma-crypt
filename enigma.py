import random




class Rotor:
    def __init__(self, wiring, notch_positions):
        self.wiring = wiring
        self.notch_positions = notch_positions
        self.position = 0

    def rotate(self):
        self.position = (self.position + 1) % 26

    def encrypt_forward(self, letter):
        letter_idx = (ord(letter) - ord('A') - self.position) % 26
        encrypted_letter_idx = self.wiring[letter_idx]
        encrypted_letter = chr((encrypted_letter_idx + self.position) % 26 + ord('A'))
        return encrypted_letter

    def encrypt_backward(self, letter):
        letter_idx = (ord(letter) - ord('A') - self.position) % 26
        encrypted_letter_idx = self.wiring.index(letter_idx)
        encrypted_letter = chr((encrypted_letter_idx + self.position) % 26 + ord('A'))
        return encrypted_letter

class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, letter):
        letter_idx = ord(letter) - ord('A')
        reflected_letter_idx = self.wiring[letter_idx]
        reflected_letter = chr(reflected_letter_idx + ord('A'))
        return reflected_letter

class EnigmaMachine:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    def encrypt_letter(self, letter):
        for rotor in self.rotors:
            letter = rotor.encrypt_forward(letter)
        letter = self.reflector.reflect(letter)
        for rotor in reversed(self.rotors):
            letter = rotor.encrypt_backward(letter)
        return letter

    def rotate_rotors(self):
        for i, rotor in enumerate(self.rotors):
            if rotor.position in rotor.notch_positions:
                rotor.rotate()
                if i < len(self.rotors) - 1:
                    self.rotors[i + 1].rotate()

# Exemple d'utilisation
def main():
    rotor1 = Rotor([4, 10, 12, 5, 6, 25, 9, 24, 16, 20, 8, 17, 23, 7, 22, 19, 14, 2, 15, 13, 18, 11, 21, 3, 0, 1], [16])
    rotor2 = Rotor([0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 21, 6, 25, 13, 15, 24, 14, 4, 5, 16], [4])
    rotor3 = Rotor([1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14], [21])
    reflector = Reflector([24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19])

    message = input("Entrez le message à chiffrer : ").upper()
    encrypted_message = ""

    for letter in message:
        if letter.isalpha():
            rotor1.position = random.randint(0, 25)
            rotor2.position = random.randint(0, 25)
            rotor3.position = random.randint(0, 25)

            enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector)

            encrypted_letter = enigma.encrypt_letter(letter)
            encrypted_message += encrypted_letter
        else:
            encrypted_message += letter

    print("Message chiffré:", encrypted_message)

if __name__ == "__main__":
    main()