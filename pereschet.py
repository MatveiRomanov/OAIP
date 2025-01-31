def pereschet(s):

    if not s:
        return 0

    vowels = 'йуеыаоэяиюЙУЕЫАОЭЯИЮ'


    if s[0] in vowels:
        return 1 + pereschet(s[1:])

    else:
        return pereschet(s[1:])

