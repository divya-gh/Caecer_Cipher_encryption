print("Caeser Cipher! ")
import string as str

#List of alphabets lowercase
alphabets = list(str.ascii_lowercase)+list(str.ascii_lowercase)
print(alphabets)
#Ask user to input data
go = True
while go == True:
    direction= input("Type 'encode' to encrypt and type 'decode' to decrypt : ")

    text = input("Type your message without space: " ).lower()

    shift = int(input("Type the shift number (<20): "))

    'Conver tthe inputed text to a list'
    text_list = []
    def encrypt(text , shift):
        # split the string charecters into a list 
        '''for char in text:
            text_list.append(char)'''

        text_list = list(text)
        #print(text_list)

        #Find the index of the letters in the text message in alphabet list
        new_text_list =[]
        for letter in text_list:
            # Find the index of the letter and then the new index of shifted letter and its corresponding letter
            first_index = alphabets.index(letter)
            new_index = first_index + shift
            new_letter = alphabets[new_index]
            # append it into a new list
            new_text_list.append(new_letter)
        #join the list items (encided message) into a single string
        encoded_msg = "".join(new_text_list)
        #Print encoded message
        #print(new_text_list)
        #print(f"Your encoded message is : {encoded_msg}")
        return encoded_msg


    #Decrypt the message

    def decrypt(encoded_text , shift):
        decoded_msg = ""
        for letter in encoded_text:
            first_index = alphabets.index(letter)
            second_index = alphabets.index(letter,first_index +1)
            new_index = second_index - shift
            new_letter = alphabets[new_index]
            decoded_msg+=new_letter
        #print(f"Your Decoded Message is : {decoded_msg}")
        return decoded_msg


    encoded_msg = encrypt(text,shift)
    decoded_msg = decrypt(encoded_msg, shift)
    if direction == "encode" :
        print(f"Your encoded message is : {encoded_msg}")
        value = input("Would you like to decode your message ?Y/N : ").upper()
        if value == "Y":
            print(f"Your decoded message is: {decoded_msg}")
        else:
            pass
    elif direction == "decode":
        print(f"Your decoded message is: {decrypt(text, shift)}")
    proceed = input("Would you like to continue? Y/N: ").upper()
    if proceed == "Y":
        go = True
    else:
        break
    


        
    
            


