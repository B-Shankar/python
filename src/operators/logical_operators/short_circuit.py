# Short Circuit Evaluation

high_income = False
good_credit = True
student = True

if high_income and good_credit and student:  # if high_income is False, then, it won't check rest of it. directly go to else part
    print("Eligible")
else:
    print("Not Eligible")

if high_income or good_credit or student:  # if high_income is False, then it will check rest of it, until it find one that is True or else part
    print("Eligible")
else:
    print("Not Eligible")
