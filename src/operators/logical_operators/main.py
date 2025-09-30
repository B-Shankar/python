# Three Logical Operator: and(&), or(|), not

high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
