from translator import Translator
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description="Translate text using a cypher")
parser.add_argument("cipher_file", metavar="<cipher>", type=str, nargs=1,
                    help="The cipher file")
parser.add_argument("type", metavar="<E|D>", type=str, nargs=1, help="Encrypt (E), or Decrypt (D)")
parser.add_argument("input_file", metavar="<input file>", type=argparse.FileType("r", encoding="utf8"), nargs=1,
                    help="The input file")
parser.add_argument("output_file", metavar="output_file", type=argparse.FileType("w", encoding="utf8"), nargs="?",
                    help="The output file")

args = parser.parse_args()

translator = Translator(args.cipher_file[0], args.type[0], args.input_file[0], args.output_file)
if args.output_file:
    translator.print_to_file()
else:
    print(translator.get_output_text())
pprint(translator.get_cipher())