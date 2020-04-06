from collections import deque
def solution(road, n):
    answer = 0
    q = deque()
    q.append([0,0])
    check = [[-1]*(n+1) for i in range(len(road))]
    check[0][0] = 1
    longest = 0
    while q:
        x, cnt = q.popleft()
        if x == len(road)-1:
            break
        if road[x+1] == '0' and cnt < n:
            check[x+1][cnt+1] = check[x][cnt]+1
            longest = max(longest, check[x+1][cnt+1])
            q.append([x+1, cnt+1])
            check[x+1][cnt] = 0
            q.append([x+1, 0])
        elif road[x+1] == '1':
            check[x+1][cnt] = check[x][cnt]+1
            longest = max(longest, check[x+1][cnt])
            q.append([x+1, cnt])
    print(longest)
    print(check)
    return 

# road = "111011110011111011111100011111"	
# road = "001100"
road = "101010110001111"
# n = 3
# n = 5
n = 2
solution(road, n)
