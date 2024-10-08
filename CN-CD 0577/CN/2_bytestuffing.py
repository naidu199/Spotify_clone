def get_input():
    inputs = []
    while True:
        word = input("Enter the Word: ")
        inputs.append(word)
        answer = int(input("Do you want to continue? (y: 1/n: 0): "))
        if answer == 0:
            break
    return inputs

def make_frames(words):
    print("\nThe Transmitted Data is:")
    for word in words:
        print(f"{len(word)}{word}\n", end='')

words = get_input()
make_frames(words)

