def print_star(row):
    asterix = "*"
    actual_row_count = row * 2
    for i in range(0, actual_row_count):
        if i % 2 == 0:  # hide the even lines where spaces are not sync
            continue
        half_width = (actual_row_count - i) // 2
        print(r" " * half_width, end="")
        print(asterix * i)


print_star(21)
