import sys
input = sys.stdin.readline
# 한개의 정수를 입력받을 때
# int 로 형변환 하는 이유
# (1) 한줄 단위로 입력받기 때문에 개행문자(\n)이 같이 입력받아짐. 따라서 개행문자를 제거해야함
# (2) 변수 타입이 문자열(str)이기 때문에 정수로 형변환
a = int(input())
print(a)


# 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할때
b = list(map(int, input().split())) # a = [1,2,3,4,5]
print(b)

# 정해진 개수의 정수를 한줄에 입력받을 때
c,d = map(int,input().split())
print(c)
print(d)

# 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
data = []
n = int(input())
for i in range(n):
    data.append(list(map(int,input().split())))

print(data)
# 문자열 N줄을 입력받아 리스트에 저장할 때
N = int(input())
data = [input().strip() for i in range(n)]
print(data)

# strip : 맨 앞과 맨 끝의 공백문자를 제거
# rstrip : 맨 앞 공백문자 제거
# lstrip : 맨 뒤 공백문자 제거