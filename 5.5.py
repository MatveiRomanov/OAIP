def main():

    num_colors = int(input())

    colors = []
    for _ in range(num_colors):
        color = input()
        colors.append(color)

    num_flags = int(input())

    garland = (colors * (num_flags // num_colors + 1))[:num_flags]

    print(' '.join(garland))

main()