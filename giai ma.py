def decrypt(ciphertext, private_key):
    """
    Giải mã văn bản sử dụng khóa bí mật.
    Args:
        ciphertext (List[int]): Danh sách các giá trị số nguyên đại diện cho văn bản đã mã hóa
        private_key (Tuple[int, int]): Khóa bí mật (d, n)
    Returns:
        str: Văn bản đã được giải mã
    """
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])

    return plaintext

private_key = []
with open('x_privkey.txt','r+') as f:
    tmp = f.readline().split(' ')
    private_key = list(map(int,tmp))
    print(private_key)
# Giải mã văn bản
ciphertext =[]
with open("Data_cipher.txt" , "r") as f:
    tmp = f.readline()
    ciphertext = eval(tmp)
decrypted_text = decrypt( ciphertext, private_key)
x= decrypted_text.split('/')
for i  in x:
    print(i)