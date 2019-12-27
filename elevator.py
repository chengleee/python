if __name__ == '__main__':
    t = 0
    stop = []
    stop = list(map(int, input().split(' ')))
    if stop[0] == 0:
        print(0)
    if stop[0] == 1:
        print(stop[1] * 6 + 5)
    if stop[0] > 1:
        t = (stop[1] - 0) * 6 + 5
        for i in range(2, len(stop)):
            if stop[i] - stop[i - 1] > 0:
                t += 6 * (stop[i] - stop[i - 1]) + 5
            elif stop[i] - stop[i-1] < 0:
                t += 4 * (stop[i - 1] - stop[i]) + 5
            else:
                t += 5
        print(t)
