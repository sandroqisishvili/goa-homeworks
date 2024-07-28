def main():
    try:
        number = float(input("შეიყვანეთ რიცხვი: "))

        if 0 < number < 10:
            print(True)
        else:
            print(False)
    except ValueError:
        print("შეიყვანეთ სწორი რიცხვი")

if name == "main":
    main()