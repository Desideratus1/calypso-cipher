from fnmatch import translate
from importers.json_importer import JsonImporter
import os

class Translator:

    def __init__(self, cipher_file, encrypt_or_decrypt, input_file, output_file):
        file_extension = os.path.splitext(cipher_file)[1]
        if file_extension == ".json":
            self.cipher = JsonImporter.get_cipher_from_file(cipher_file)
        self.input_file = input_file
        self.output_file = output_file
        self.output_text = None
        self.type = encrypt_or_decrypt

    def get_cipher(self):
        return self.cipher

    def get_input_text(self):
        contents = self.input_file.read()
        return contents

    def translate(self):
        text = self.get_input_text()
        print(self.type)
        if self.type == "D" or self.type == "d":
            for cipher_part in self.cipher:
                text = text.replace(cipher_part["translate"], cipher_part["phrase"])
        else:
            for cipher_part in self.cipher:
                text = text.replace(cipher_part["phrase"], cipher_part["translate"])
        self.output_text = text

    def print_to_file(self):
        if not self.output_text:
            self.translate()
        self.output_file.write(self.output_text)

    def get_output_text(self):
        if not self.output_text:
            self.translate()
        return self.output_text