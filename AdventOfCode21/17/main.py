def main():
    data = [[e.split("..") for e in data] for data in [open("data.txt", "r").read().replace("target area: x=", "").replace(" y=", "").split(",")]][0]
    xmin, xmax, ymin, ymax, result, x, sum = int(data[0][0]), int(data[0][1]), int(data[1][0]), int(data[1][1]), [0, 0], 0, 0

    y = abs(ymin + 1)
    for v in range(y + 1): result[0] += v

    while not xmin < sum < xmax:
        x += 1
        sum += x

    for i in range(x, xmax + 1):
        for j in range(ymin, y + 1):
            sum, counter = [0, 0], [i, j]
            while sum[0] <= xmax and sum[1] >= ymin:
                sum[0] += counter[0]
                sum[1] += counter[1]
                if counter[0] > 0: counter[0] -= 1
                counter[1] -= 1
                if xmin <= sum[0] <= xmax and ymin <= sum[1] <= ymax: 
                    result[1] += 1
                    break

    print("Answer to part one: " + str(result[0]))
    print("Answer to part two: " + str(result[1]))

main()