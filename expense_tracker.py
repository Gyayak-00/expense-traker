first_person = int(input("How much money did the first person spend? "))
second_person = int(input("How much money did the second person spend? "))
third_person = int(input("How much money did the third person spend? "))

total = first_person + second_person + third_person
print(f"\nTotal trip expense: ${total}")

choice = input("\nIf you want to divide the amount equally among 3, press D: ").lower()

if choice == 'd':
    equal_share = total / 3
    print(f"\nEach person should pay: ${equal_share:.2f}")
    
    diff1 = round(equal_share - first_person, 2)
    diff2 = round(equal_share - second_person, 2)
    diff3 = round(equal_share - third_person, 2)

    print("\n--- Settlement ---")
    if diff1 > 0:
        print(f"First person should give: ${diff1}")
    elif diff1 < 0:
        print(f"First person will get back: ${-diff1}")
    else:
        print("First person is settled.")

    if diff2 > 0:
        print(f"Second person should give: ${diff2}")
    elif diff2 < 0:
        print(f"Second person will get back: ${-diff2}")
    else:
        print("Second person is settled.")

    if diff3 > 0:
        print(f"Third person should give: ${diff3}")
    elif diff3 < 0:
        print(f"Third person will get back: ${-diff3}")
    else:
        print("Third person is settled.")

else:
    print("\nThank you for using the expense tracker!")
