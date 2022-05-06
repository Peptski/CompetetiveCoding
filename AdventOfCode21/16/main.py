import math

def main():
    data = open("data.txt", "r").read()
    data = bin(int(data, 16))[2:].zfill(len(data) * 4)

    _, num, ver = decode_packet(data, 0, 0)

    print("Answer to part one: " + str(ver))
    print("Answer to part two: " + str(num))

def decode_packet(data, v, size):
    v += int(data[size:size + 3], 2)
    t = int(data[size + 3:size + 6], 2)
    size += 6

    if t == 4:
        number = ""
        done = False 
        while not done:
            if data[size:size+1] == "0": done = True
            number += data[size+1:size+5]
            size += 5
        return size, int(number, 2), v
    else:
        mode = data[size:size+1]
        numbers = []
        if mode == "0":
            sub_bits = int(data[size+1:size+16], 2)
            size += 16
            end = size + sub_bits
            while size < end:
                size, num, v = decode_packet(data, v, size)
                numbers.append(num)
            return size, op(numbers, t), v
        else:
            sub_packs = int(data[size+1:size+12], 2)
            size += 12
            while sub_packs > 0:
                size, num, v = decode_packet(data, v, size)
                numbers.append(num)
                sub_packs -= 1
            return size, op(numbers, t), v

def op(numbers, type):
    match type:
        case 0: return sum(numbers)
        case 1: return math.prod(numbers)
        case 2: return min(numbers)
        case 3: return max(numbers)
        case 5: return 1 if numbers[0] > numbers[1] else 0
        case 6: return 1 if numbers[0] < numbers[1] else 0
        case 7: return 1 if numbers[0] == numbers[1] else 0

main()