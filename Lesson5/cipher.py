def cipher(text, diff):
    L = [ord(i) + diff for i in text]
    
    result_text = [chr(i) for i in L]
    
    return ''.join(result_text)
    

def decipher(text, diff):
    L = [ord(i) - diff for i in text]
    
    result_text = [chr(i) for i in L]
    
    return ''.join(result_text)


ciphered = cipher("Hello, world!", 5)
print(ciphered)

deciphered = decipher(ciphered, 5)
print(deciphered)
