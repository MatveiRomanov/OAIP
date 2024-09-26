def main():

    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = int(input())

    if i + 3 > len(alf):
        alf = alf * 2
        print(alf[i - 1:i + 3])
    else:
        print(alf[i - 1:i + 3])

main()