# https://www.acmicpc.net/problem/8393

# 문제
# # n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력
# # 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력
# # 1부터 n까지 합을 출력한다.
def sum_print(n) :
    list_n=[n]
    for x in range(n) :
        n = n-1
        list_n.append(n)
    print(sum(list_n))

n=int(input())
sum_print(n)