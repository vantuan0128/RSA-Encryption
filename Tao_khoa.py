import os
import random
import math

def is_prime(num):
    """
    Kiểm tra xem một số có phải là số nguyên tố hay không.
    Args:
        num (int): Số cần kiểm tra
    Returns:
        bool: True nếu là số nguyên tố, False nếu không phải
    """
    if num < 2: return False
    for i in range(2, int(math.sqrt(num)) + 1, 1):
        if num % i == 0: return False
    return True

def gcd(a, b):
    """
    Tính ước chung lớn nhất của hai số.
    Args:
        a (int): Số thứ nhất
        b (int): Số thứ hai
    Returns:
        int: Ước chung lớn nhất của hai số
    """
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, n):
    """
    Tính nghịch đảo của a trong modulo n.
    Args:
        a (int): Số nguyên a
        n (int): Số nguyên modulo n
    Returns:
        int: Nghịch đảo của a trong modulo n, hoặc -1 nếu không tồn tại
    """
    m0 = n
    y, x = 0, 1

    if n == 1:
        return 0

    while a > 1:
        # Phép chia lấy dư
        q = a // n
        a, n = n, a % n
        x, y = y, x - q * y

    if x < 0:
        x = x + m0

    return x if a == 1 else -1

def generate_prime():
    """
    Tạo ra một số nguyên tố ngẫu nhiên.
    Returns:
        int: Số nguyên tố ngẫu nhiên
    """
    while True:
        num = random.randint(100, 1000)  # Tạo số nguyên tố trong khoảng từ 100 đến 1000
        if is_prime(num):
            return num

def generate_keys():
    """
    Tạo ra cặp khóa công khai và khóa bí mật.
    Returns:
        Tuple[Tuple[int, int], Tuple[int, int]]: Cặp khóa công khai và khóa bí mật
    """
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 0
    d = 0

    while True:
        e = random.randint(2, phi_n - 1)
        if math.gcd(e, phi_n) == 1:
            d = mod_inverse(e, phi_n)
            d %= phi_n
            break

    public_key = (e, n)
    private_key = (d, n)

    fb = open("x_pubkey.txt","w+")
    fr = open("x_privkey.txt","w+")
    # print(str(public_key))
    # print(str(private_key))
    tmp = str(public_key[0]) +" " + str(public_key[1])
    fb.write(tmp )
    tmp =""
    tmp = str(private_key[0]) +" "+str(private_key[1])
    fr.write(tmp)
    fr.close()
    fb.close()

    with open('x_privkey.txt','r+') as f:
        newkey2 = f.read()
        print(newkey2)

generate_keys()