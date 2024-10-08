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

def decodeData(data, key):
    remainder = mod2div(data, key)
    return remainder

# Server code
s = socket.socket()
print("Socket successfully created")

port = 1240
s.bind(("", port))
print("Socket binded to %s" % port)

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    data = c.recv(1024).decode()
    if not data:
        break

    # Split data by comma, error handling added
    try:
        data, key = data.split(",")
    except ValueError:
        print("Error: Invalid data format received.")
        c.send("Error in data format".encode())
        c.close()
        continue

    print("Received encoded data in binary format:", data)
    print("Received Key:", key)

    ans = decodeData(data, key)
    print("Remainder after decoding is -> " + ans)

    temp = "0" * (len(key) - 1)
    if ans == temp:
        msg = data[:-(len(key) - 1)]
        decoded_message = ""
        for i in range(0, len(msg), 7):
            decoded_message += chr(int(msg[i:i + 7], 2))
        print("Decoded message:", decoded_message)
        c.send(("Thank you, Data -> " + data + " Received, No error found").encode())
    else:
        c.send("Error in data".encode())

    c.close()
