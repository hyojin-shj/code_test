#첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다

remain = set()

for _ in range(10):
    num = int(input())
    remain.add(num % 42)

print(len(remain))

        
