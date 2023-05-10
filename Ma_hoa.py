
def encrypt(plaintext, public_key):
    """
    Mã hóa văn bản sử dụng khóa công khai.
    Args:
        plaintext (str): Văn bản cần mã hóa
        public_key (Tuple[int, int]): Khóa công khai (e, n)
    Returns:
        List[int]: Danh sách các giá trị số nguyên đại diện cho văn bản đã mã hóa
    """
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext
public_key, private_key = [],[]
# with open('x_privkey.txt','r+') as f:
#     tmp = f.readline().split(' ')
#     print(tmp)
#     private_key = list(map(int,tmp))
#     print(private_key)
with open('x_pubkey.txt','r+') as f:
    tmp1 = f.readline().split(' ')
    public_key = list(map(int,tmp1))
    print(public_key)
# Mã hóa văn bản
data = ""
with open("Data.txt","r+") as f:
    data = f.read()
    data = data.replace('\n', '/')
plaintext = data
ciphertext = encrypt(plaintext, public_key)
print("Ciphertext:", ciphertext)
with open("Data_cipher.txt","w+") as f:
    f.write(str(ciphertext))
