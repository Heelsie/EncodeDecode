import string
alphabet = list(string.ascii_uppercase)


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


print("Your encoded message is: ", encode(text))
print("Your decoded message is: ", encode(encode(text)))