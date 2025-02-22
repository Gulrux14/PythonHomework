def insert_underscore(txt):
    vowels = "aeiouAEIOU"
    result = []
    count = 0

    for i, char in enumerate(txt):
        result.append(char)
        count += 1
        
        if count == 3:
            if i + 1 < len(txt) and (txt[i] in vowels or txt[i+1] == '_'):
                if i + 2 < len(txt):
                    result.append(txt[i+1])
                    result.append('_')
                    count = 0
                continue
            else:
                result.append('_')
                count = 0
    
    return ''.join(result)

if name == "main":
    txt = input("Enter text: ")
    print("Result:", insert_underscore(txt))