import string
alphabet = list(string.ascii_uppercase)
# Hi Joseph, congratuations on making it this far! Now you need to use this code to decode your present.

def encode(text):
    result = ''
    for i in list(text.upper()):    
        if i in alphabet:      
            result += alphabet[-alphabet.index(i)+25] 
        else:  
            result += i
    return result

text = input("Your message: ")    
#print(text)    


print("Encoded message is: ", encode(text))
#print("Decoded message: ", encode(encode(text)))


# Bonus code IEU8C-WATRK-53OEW
# Bonus code 24WU6-D6XGZ-PVO48