import json

class JsonImporter():

    def get_cipher_from_file(file):
        load = json.load(open(file, "r"))
        return sorted(load,key= lambda x:len(x["phrase"]),reverse=True)

