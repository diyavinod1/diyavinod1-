print("""What do you want to do???
1. Create a Quiz
2. Attend the existing Quiz""")
ch=int(input("Your Choice:"))
if ch==1:
    import FSMaker
elif ch==2:
    import FSAttender
else:
    print("Invalid Entry")
