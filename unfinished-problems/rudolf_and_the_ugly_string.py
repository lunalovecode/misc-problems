t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    map_count = string.count("map")
    pie_count = string.count("pie")
    print(map_count + pie_count)