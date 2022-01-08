lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
not_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+']
do_again = True

def caesar (text, shift, method):
    data = ''
    
    for idx in range(len(text)):
        if method == "encode":
            position = lower_case.index(text[idx]) + shift
            data += lower_case[position]
        elif method == "decode":
            position = lower_case.index(text[idx]) - shift
            data += lower_case[position]

    print(f"The {method}d text is {data}")

while do_again:
    method = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift %= 26
    caesar (text, shift, method)

    result = input("Do you want to do again? (yes/no): ").lower()
    if result == "no":
        do_again = False