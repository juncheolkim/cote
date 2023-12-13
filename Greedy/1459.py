X,Y,W,S = map(int, input().split())
if 2*W < S: # 대각선으로 가지 않는다.
    print((X+Y)*W)
else: # 대각선을 가능한 간다.
    if W > S: # 축으로 가는 것보다 대각선으로 가는게 더 빠를 때
        if (X + Y) % 2 :
            print((max(X,Y)-1)*S + W)
        else:
            print(max(X,Y)*S)
    else:
        print(min(X,Y)*S + abs(X-Y)*W)