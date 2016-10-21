import element_dict as ed

def main():

    ciphertext_file = open('ciphertext.txt','r')
    plaintext_file = open('plaintext.txt','w')

    element_dict = ed.element_dict_generate()

    for n in ciphertext_file.read().split():
        # n is each group of characters in ciphertext separated 
        # by spaces.

        # If n is a character:
        if n.isalpha():
            # Simply write it to the file as-is (uppercase)
            s = n.upper()

        
        else: # n is an atomic number: 
            # Match the atomic number with the atomic symbol
            s = element_dict[int(n)].upper()

        plaintext_file.write('{}'.format(s))

    plaintext_file.close()
    ciphertext_file.close()

if __name__ == '__main__':
    main()


