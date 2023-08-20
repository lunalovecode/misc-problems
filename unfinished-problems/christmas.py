def count_layers(n):
    layer_count, patty_count, bun_count = 1, 1, 0
    if n == 0:
        return layer_count
    else:
        a = count_layers(n - 1) + count_layers(n - 1)
        layer_count = a + 3
        patty_count = a + 1
        bun_count = layer_count - patty_count
        # 1 * 2^n + 3
        return layer_count
n, x = [int(x) for x in input().split()]
print(count_layers(n))