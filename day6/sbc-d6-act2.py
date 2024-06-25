def create_box(border_length, border_width):
    border = "=" * border_length
    print(border)

    middle_row = "=" + " " * (border_length - 2) + "="
    for _ in range(border_width - 2):
        print(middle_row)

    print(border)
while True:
    try:
        border_length = int(input("Enter the border length(must be atleast 3) : "))
        if border_length < 3:
            print("Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive number.")

while True:
    try:
        border_width = int(input("Enter the border width (must be at least 3): "))
        if border_width < 3:
            print("Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive number.")

create_box(border_length, border_width)