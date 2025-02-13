text = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for char in text if char in vowels)
consonant_count = len([char for char in text if char.isalpha() and char not in vowels])
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")