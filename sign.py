if __name__ == '__main__':
    # 赋值
    M = int(input())
    L = []
    for i in range(M):
        L.append(list(input().split()))

    # 得出结果
    Min = L[0]
    Max = L[0]
    for m in L:
        if Min[1] > m[1]:
            Min = m
        if Max[2] < m[2]:
            Max = m
    print(Min[0],Max[0])
