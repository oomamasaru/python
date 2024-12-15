names = ["A", "B", "C"]

rename = list(
    map(
        lambda x: x+"さん",
        names
    )
)

print(rename)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(
    filter(
        lambda x: x % 2 == 0,
        number
    )
)

print(even)
