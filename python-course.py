# email = input("Enter your email address: ")

# if "@" in email and "." in email:
#     print("Valid email address.")
# else:
#     print("Invalid email address. Please try again.")

# username = email[:email.index("@")]
# print(f"Your username is: {username}")


# Formatting a float to one decimal place
# price = 3.15488777
# print(f"The price is: ${price:.1f} dollars")

import time

my_time = int(input("Enter the time in seconds: "))

for i in range(my_time, 0, -1):
    print(f"00:00:{i:02d}", end="\r")
    time.sleep(1)
