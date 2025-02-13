text = input("Enter a sentence: ")
start = input("Starts with: ")
end = input("Ends with: ")
print(text.startswith(start) and text.endswith(end))