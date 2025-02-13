text = input("Enter a string: ")
print("Contains digits" if any(char.isdigit() for char in text) else "No digits found")
