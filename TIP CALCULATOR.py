print("welcome to the tip calculator")
total_amount=(input("Enter your total amount? $"))
total_tip=(input("Enter your total tip? 5,10,15,20 or any other amount? $"))
total_members=(input("Enter your total members?"))
total_bill=int(total_amount)+int(total_tip)
split_bill=int(total_bill)/int(total_members)
split_bill=round(split_bill)
print(f"each person to pay amount is ${split_bill}")

