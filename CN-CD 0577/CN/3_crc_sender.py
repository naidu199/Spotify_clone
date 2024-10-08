import socket

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return "".join(result)

def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0:pick]

    while pick < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]
        else:
            tmp = xor('0'*pick, tmp) + divident[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    checkword = tmp
    return checkword

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

def crcfind():
    ans = encodeData(data, key)
    print("Encoded data to be sent to server in binary format:", ans)
    ans = ans + "," + key  # Corrected to add a comma between data and key
    s.sendto(ans.encode(), ('127.0.0.1', port))
    print("Received feedback from server:", s.recv(1024).decode())

# Client code
s = socket.socket()
port = 1240
s.connect(('127.0.0.1', port))

input_string = input("Enter data you want to send -> ")
data = ("".join(format(ord(x), 'b').zfill(7) for x in input_string))  # Added .zfill(7)
print("Entered data in binary format:", data)

while True:
    print("Choose which CRC Technique you want to use: ")
    print("1. CRC-12")
    print("2. CRC-16")
    print("3. Exit")

    n = int(input())

    if n == 1:
        key = input("Enter key for CRC-12 (The key should start and end with 1 and contains 13 digits): ")
        crcfind()
    elif n == 2:
        key = input("Enter key for CRC-16 (The key should start and end with 1 and contains 17 digits): ")
        crcfind()
    else:
        break
s.close()

