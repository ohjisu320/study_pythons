# https://www.acmicpc.net/problem/14681

# 입력
# # 첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)

# 출력
# # 점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.

def Quadrant_n(x, y) :
    if x > 0 and y > 0 :
        print(1)
    elif x > 0 and y < 0 :
        print(4)
    elif x < 0 and y < 0 :
        print(3)
    elif x < 0 and y > 0 :
        print(2)

x = int(input())
y = int(input())
Quadrant_n(x, y)