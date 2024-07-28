def getageinput(person):
    while True:
        try:
            age = int(input(f"შეიყვანეთ {person}-ის ასაკი: "))
            if age < 0:
                raise ValueError("ასაკი უარყოფითი არ უნდა იყოს.")
            return age
        except ValueError as e:
            print(f"არასწორი მნიშვნელობა. სცადეთ თავიდან. {e}")

def compareages(age1, age2):
    if age1 > age2:
        print("პირველი პირი უფროსია.")
    elif age1 < age2:
        print("მეორე პირი უფროსია.")
    else:
        print("ორივე პირი თანაბარი ასაკის არიან.")

def main():
    age1 = getage_input("პირველი პირი")
    age2 = get_age_input("მეორე პირი")
    compare_ages(age1, age2)

if __name == "__main":
    main()
    