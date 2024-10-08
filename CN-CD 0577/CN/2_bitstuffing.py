DELIM_BIT_PATTERN = "01111110"
SNDR_INPUT = 0
SNDR_OUTPUT = 1
REC_INPUT = 2
REC_OUTPUT = 3

data = [""] * 4

def valid_data():
    if not data[SNDR_INPUT]:
        print("\n***Enter Some Data***\n")
        return False
    for char in data[SNDR_INPUT]:
        if char not in '01':
            print("** This is not binary data. Please enter 0's and 1's\n")
            return False
    return True

def sender_bit_stuff():
    count = 0
    data[SNDR_OUTPUT] = DELIM_BIT_PATTERN
    for bit in data[SNDR_INPUT]:
        if count == 5:
            data[SNDR_OUTPUT] += '0'
            count = 0
        if bit == '1':
            count += 1
        else:
            count = 0
        data[SNDR_OUTPUT] += bit
    if count == 5:
        data[SNDR_OUTPUT] += '0'
    data[SNDR_OUTPUT] += DELIM_BIT_PATTERN

def receiver_process_data():
    count = 0
    src = data[REC_INPUT][len(DELIM_BIT_PATTERN):-len(DELIM_BIT_PATTERN)]
    data[REC_OUTPUT] = ""
    for bit in src:
        if count == 5:
            count = 0
            continue
        if bit == '1':
            count += 1
        else:
            count = 0
        data[REC_OUTPUT] += bit

ans = 1
while ans != 0:
    data[SNDR_INPUT] = input("\nEnter Data from Network Layer in Binary Form: ")
    if not valid_data():
        continue
    sender_bit_stuff()
    print("\nSender's Physical Layer Data: {}\n".format(data[SNDR_OUTPUT]))
    data[REC_INPUT] = data[SNDR_OUTPUT]
    receiver_process_data()
    print("\nReceiver's Network Layer Data: {}\n".format(data[REC_OUTPUT]))
    ans = int(input("Do you want to continue? (y: 1/n: 0): "))

