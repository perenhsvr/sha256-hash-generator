import hashlib

text = input("Metin giriniz: ")

hash_value = hashlib.sha256(text.encode()).hexdigest()

print("SHA256:", hash_value)
