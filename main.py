# 1
roy = ["hi", "hello"]
print(list(map(lambda x: len(x) + 1, roy)))

# 2
roy = [12, 24, 36]
print(list(map(lambda x: x / 12, roy)))

# 3
roy = ["A", "B", "C"]
print(list(map(lambda x: x.lower(), roy)))

# 4
roy = [3, 5, 7]
print(list(map(lambda x: str(x * 10), roy)))

# 5
roy = ["1", "2", "3"]
print(list(map(lambda x: int(x) + 100, roy)))
