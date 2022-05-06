def part_one():
    result = 0
    for row in data:
        for outputs in row[1]:
            if len(outputs) in [2, 3, 4, 7]: result += 1
    return result    
    
def part_two():
    result, numbers = 0, {"abcefg" : "0", "cf" : "1", "acdeg" : "2", "acdfg" : "3", "bcdf" : "4", "abdfg" : "5", "abdefg" : "6", "acf" : "7", "abcdefg" : "8", "abcdfg" : "9"}

    for row in data:
        decrypt = get_segments(row[0])
        number = ""
        for num in row[1]:
            decrypted = ""
            for element in num: decrypted += decrypt[element]
            number += numbers["".join(sorted(decrypted))]
        result += int(number)
    return result

def get_segments(row):
    segments, all = {}, ""
    for e in row:
        if len(e) == 4:
            all += 3 * e
        all += e
    for letter in ["a", "b", "c", "d", "e", "f", "g"]:
        match all.count(letter):
            case 8: segments[letter] = "a"
            case 9: segments[letter] = "b"
            case 11: segments[letter] = "c"
            case 10: segments[letter] = "d"
            case 4: segments[letter] = "e"
            case 12: segments[letter] = "f"
            case 7: segments[letter] = "g"
    return segments

data = [[elems.split(" ") for elems in line.split(" | ")] for line in open("data.txt", "r").read().split("\n")]
print ("Answer to part one: " + str(part_one()))
print ("Answer to part two: " + str(part_two()))