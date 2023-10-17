a = int(input("How many times?"))

if isinstance(a, int):
    while a > 0:
        print("Hey Tmux!")
        a = a - 1
