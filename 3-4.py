n, k = map(int, input().split())

result = 0

# 내가 짠 코드
# while True:
#     if n == 1:
#         break
#     elif n % k != 0:
#         n -= 1
#         result += 1
#     elif n % k == 0:
#         n //= k
#         result +=1

# 시간 복잡도 측면에서 더 좋은 코드
while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k
result += (n - 1)

print(result)