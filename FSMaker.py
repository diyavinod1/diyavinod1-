fh=open("FS-M.txt","a")
print("""Create your friendship dare quiz and
Improve your relations by finding your qualities, strength and zones of improvement""")
name=input("PLease fill your name:")
fh.write(name)
fh.write('\n')
print("So.....",name,"\nLet's Get Started")
print("""A thing you aregood at?
1.Singing
2.Talking
3.Dancing
4.Studying
5.Nothing""")
a1=int(input("Your Answer: "))
fh.write(str(a1))
fh.write('\n')
print("""How would you describe yourself?
1.Studious
2.Chatter-box
3.Caring
4.Childish
5.Short-tempered""")
a2=int(input("Your Answer: "))
fh.write(str(a2))
fh.write('\n')
print("""What is your favourite SUBJECT?
1.Mathematics
2.Chemistry
3.English
4.Physics""")
a3=int(input("Your Answer: "))
fh.write(str(a3))
fh.write('\n')
print("""What is your past-time hobby?
1.Seeing mobile phone
2.Sleeping
3.Drawing/Painting
4.Talking""")
a4=int(input("Your Answer: "))
fh.write(str(a4))
fh.write('\n')
print("""Are you a BTS fan?
1.Yes
2.No""")
a5=int(input("Your Answer: "))
fh.write(str(a5))
fh.write('\n')
print("""What do you wish to do after XII Board Exams?"))
1.Sleep
2.Enjoy life with you
3.Prepare for any other competative exam
4.Enter into a job""")
a6=int(input("Your Answer: "))
fh.write(str(a6))
fh.write('\n')
print("""You like School life or College life?
1.School Life
2.College Life
3.Both
4.None""")
a7=int(input("Your Answer: """))
fh.write(str(a7))
fh.write('\n')
print("""If you get an oppotunity for an adventurous journey, who would you prefer?
1.Family
2.Friends
3.Soulmate
4.Alone""")
a8=int(input("Your Answer: "))
fh.write(str(a8))
fh.write('\n')
print("""What do you use most?
1.Tik-Tok
2.WhatsApp
3.Instagram
4.FaceBook
5.Nothing""")
a9=int(input("Your Answer: "))
fh.write(str(a9))
fh.write('\n')
print("""A thing you are bad at?
1.Driving
2.Dancing
3.Singing
4.Cooking""")
a10=int(input("Your Answer: "))
fh.write(str(a10))
fh.write('\n')
print("""What is important in your life?
1.Health
2.Money
3.Family
4.Friends""")
a11=int(input("Your Answer: "))
fh.write(str(a11))
fh.write('\n')
print("""What is your morning routine?
1.Yoga/Exercise/Jogging
2.Going out
3.Sleeping
4.Studying""")
a12=int(input("Your Answer: "))
fh.write(str(a12))
fh.write('\n')
print("""What would you like to achieve in the next 5 years?
1.Build a home
2.Move abroad
3.Start a business
4.Write a book""")
a13=int(input("Your Answer: "))
fh.write(str(a13))
fh.write('\n')
print("""Given a chance to travel to a dream destination, which one will you pick?
1.Paris
2.New Zealand
3.Maldives
4.Dubai""")
a14=int(input("Your Answer: "))
fh.write(str(a14))
fh.write('\n')
fh.close()
print("Your answers are saved...\n\nNow your friends can attend your quiz")

