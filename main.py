import random

# user input for address_num and frame_size
# using validation (both inputs should be numbers)
address_num = frame_size = 0
f = open("output.txt", "w")
f.close()

while True:
    input_line = input("Enter the number of possible addresses: \n")
    try:
        address_num = int(input_line)
        if address_num <= 1:
            print("The number should be larger than 1!")
            continue
        break
    except ValueError:
        print("[Error] You must enter a number!")
        continue

while True:
    input_line = input("Enter the number of frames: \n")
    try:
        frame_size = int(input_line)
        if frame_size < 1:
            print("The number should be equal or larger than 1!")
            continue
        break
    except ValueError:
        print("[Error] You must enter a number!")
        continue

# creating addresses
addresses = []
while True:
    choice = input("Do you want to use random addresses"
                   " or enter then yourself? (Random->\"R\"/Manual->\"M\")\n")
    if choice == "R":
        for i in range(address_num):
            addresses.append(random.randrange(1, address_num, 1))
        break
    elif choice == "M":
        print("Enter addresses one by one: ")
        for i in range(address_num):
            while True:
                input_line = input()
                try:
                    num = int(input_line)
                    addresses.append(num)
                    break
                except ValueError:
                    print("[Error] You must enter a number!")
                    continue
        break
    else:
        print("[Error] Invalid input!")

print("Addresses: " + addresses.__str__())


def print_line(address: int, arr):
    f = open("output.txt", "a")
    global frame_size
    print("| Address " + address.__str__().center(3) + " |", end=" ")
    f.write("| Address " + address.__str__().center(3) + " | ")
    for i in range(len(arr)):
        print(arr[i].__str__().center(5) + " |", end=" ")
        f.write(arr[i].__str__().center(5) + " | ")
    counter = len(arr)
    while counter < frame_size:
        print("".center(5) + " |", end=" ")
        f.write("".center(5) + " | ")
        counter += 1
    f.close()


def print_divider():
    f = open("output.txt", "a")
    global frame_size
    print("|" + 13*"-" + "|", end="")
    f.write("|" + 13*"-" + "|")
    for i in range(frame_size):
        print(7*"-" + "|", end="")
        f.write(7*"-" + "|")
    print("---|")
    f.write("---|\n")
    f.close()


def fifo(arr, n: int):
    frames = []
    hit_count = 0
    print_divider()
    for address in arr:
        if frames.__contains__(address):
            hit = True
            hit_count += 1
        else:
            hit = False
            if len(frames) < n:
                frames.append(address)
            else:
                frames.pop(0)
                frames.append(address)
        if hit:
            print_line(address, frames)
            print("* |")
            f = open("output.txt", "a")
            f.write("* |\n")
            f.close()
            print_divider()
        else:
            print_line(address, frames)
            print("  |")
            f = open("output.txt", "a")
            f.write("  |\n")
            f.close()
            print_divider()
    print("\nHits: " + hit_count.__str__())
    print("Hit ratio: " + (hit_count/len(arr)).__str__())


def lru(arr, n: int):
    frames = []
    hit_count = 0
    print_divider()
    for address in arr:
        if frames.__contains__(address):
            hit = True
            hit_count += 1
            frames.remove(address)
            frames.append(address)
        else:
            hit = False
            if len(frames) < n:
                frames.append(address)
            else:
                frames.pop(0)
                frames.append(address)
        if hit:
            print_line(address, frames)
            print("* |")
            f = open("output.txt", "a")
            f.write("* |\n")
            f.close()
            print_divider()
        else:
            print_line(address, frames)
            print("  |")
            f = open("output.txt", "a")
            f.write("  |\n")
            f.close()
            print_divider()
    print("\nHits: " + hit_count.__str__())
    print("Hit ratio: " +
          (hit_count/len(arr)).__str__())


# deciding which replacement policy to use
while True:
    choice = input("Which cache replacement algorithm you would like to use? (\"FIFO\"/\"LRU\")\n")
    if choice == "FIFO":
        fifo(addresses, frame_size)
        break
    elif choice == "LRU":
        lru(addresses, frame_size)
        break
    else:
        print("[Error] Invalid input!")


