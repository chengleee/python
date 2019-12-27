if __name__ == '__main__':
    tree = {}
    allgen = 0
    gen = 0
    lid = 0
    lst = list(map(int,input().split()))
    N = lst[0]
    M = lst[1]
    if N == 0 or N == 1:
        print(N)
    elif M == 0:
        print(N)
    else:
        for i in range(0, M):
            lst = list(map(int,input().split()))
            ID = lst[0]
            K = lst[1]
            if i == 0:
                tree[ID] = [K, 1]
            elif K == 0 or ID not in tree:
                continue
            else:
                tree[ID][0] = K
            gen = tree[ID][1] + 1
            for j in range(2, len(lst)):
                cid = lst[j]
                lid = cid
                tree[cid] = [0, gen]

        out = []
        if not lid:
            out.append(1)
        else:
            for j in range(1, tree[lid][1] + 1):
                count = 0
                for i in tree:
                    if tree[i][1] == j and tree[i][0] == 0:
                        count += 1
                out.append(count)

        if len(out) > 1:
            for i in out[0:len(out) - 1]:
                print(i,end = ' ')
            print(out[len(out) - 1])
        else:
            print(out[0])
