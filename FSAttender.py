import time
import mysql.connector as sq
fh=open("FS-M.txt","r")
username=fh.readline()
print("""***FRIENDSHIP QUIZ***
Hii Dude!!!
Here is a wonderfullll quiz to test the depth of FRIENDSHIP between you and""",username)
print("Please fill the below details...")
pname=input("Name:\n")
pqua=input("Student(s)/Working(w):\n")
print("So.....",pname,"Let's Get Started")
print("You already have 100 points")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GO...")
time.sleep(1)
fh.close()

fh=open("FS-M.txt","r")
r=fh.readlines()
print("Question No. 1")
print("""A thing where your friend is good at?
1.Singing
2.Talking
3.Dancing
4.Studying
5.Nothing""")
a1=int(input("Your Answer: "))

print("Question No. 2")
print("""How would you describe your friend?
1.Studious
2.Chatter-box
3.Caring
4.Childish
5.Short-tempered""")
a2=int(input("Your Answer: "))

print("Question No. 3")
print("""What is your friend's favourite SUBJECT?
1.Mathematics
2.Chemistry
3.English
4.Physics""")
a3=int(input("Your Answer: "))

print("Question No. 4")
print("""What is your friend's past-time hobby?
1.Seeing mobile phone
2.Sleeping
3.Drawing/Painting
4.Talking""")
a4=int(input("Your Answer: "))

print("Question No. 5")
print("""Is your friend a BTS fan?
1.Yes
2.No""")
a5=int(input("Your Answer: "))

print("Question No. 6")
print("""What would your friend wish to do after XII Board Exams?"))
1.Sleep
2.Enjoy life with you
3.Prepare for any other competative exam
4.Enter into a job""")
a6=int(input("Your Answer: "))

print("Question No. 7")
print("""Your friend likes School life or College life?
1.School Life
2.College Life
3.Both
4.None""")
a7=int(input("Your Answer: "))

print("Question No. 8")
print("""If your friend get an oppotunity for an adventurous journey, who would he/she prefer?
1.Family
2.Friends
3.Soulmate
4.Alone""")
a8=int(input("Your Answer: "))

print("Question No. 9")
print("""What does your friend use most?
1.Tik-Tok
2.WhatsApp
3.Instagram
4.FaceBook
5.Nothing""")
a9=int(input("Your Answer: "))

print("Question No. 10")
print("""A thing your friend is bad at?
1.Driving
2.Dancing
3.Singing
4.Cooking""")
a10=int(input("Your Answer: "))

print("Question No. 11")
print("""What is important in your friend life?
1.Health
2.Money
3.Family
4.Friends""")
a11=int(input("Your Answer: "))

print("Question No. 12")
print("""What is your friend's morning routine?
1.Yoga/Exercise/Jogging
2.Going out
3.Sleeping
4.Studying""")
a12=int(input("Your Answer: "))

print("Question No. 13")
print("""What would your friend like to achieve in the next 5 years?
1.Build a home
2.Move abroad
3.Start a business
4.Write a book""")
a13=int(input("Your Answer: "))

print("Question No. 14")
print("""Given a chance to travel to a dream destination, which one will your friend pick?
1.Paris
2.New Zealand
3.Maldives
4.Dubai""")
a14=int(input("Your Answer: "))

num_cor = 100
if r[1]==(str(a1)+"\n"):
    num_cor += 50
if r[2]==(str(a2)+"\n"):
    num_cor += 50
if r[3]==(str(a3)+"\n"):
    num_cor += 50
if r[4]==(str(a4)+"\n"):
    num_cor += 50
if r[5]==(str(a5)+"\n"):
    num_cor += 50
if r[6]==(str(a6)+"\n"):
    num_cor += 50
if r[7]==(str(a7)+"\n"):
    num_cor += 50
if r[8]==(str(a8)+"\n"):
    num_cor += 50
if r[9]==(str(a9)+"\n"):
    num_cor += 50
if r[10]==(str(a10)+"\n"):
    num_cor += 50
if r[11]==(str(a11)+"\n"):
    num_cor += 50
if r[12]==(str(a12)+"\n"):
    num_cor += 50
if r[13]==(str(a13)+"\n"):
    num_cor += 50
if r[14]==(str(a14)+"\n"):
    num_cor += 50
else:
    pass
fh.close()

print("Counting your score....")
time.sleep(3)
print("Your score:",num_cor)
if num_cor>400:
    print("Amazing...\nYou both have such a great bonding <3")
elif num_cor==400:
    print(":) Well done...")
elif num_cor<400:
    print("Don't worry...\nKnowing one's feelings is more important than knowing one's likes and dislikes")

mycon=sq.connect(host="",user="",passwd="diya1234")
if mycon.is_connected()==True:
    cur=mycon.cursor()
    cur.execute("create database FSquiz")
    cur.execute("use FSquiz")
    cur.execute("create table SCOREBOARD(Name varchar(30),Status varchar(1),Score int)")
    cur.execute("insert into SCOREBOARD values('{}','{}',{})".format(pname,pqua,num_cor))
    mycon.commit()
mycon.close()


