#### Who wants to be a Millionaire

questions=[

["Which language is used in the script language in facebook", "python", "c++", "Javascript", "Php","None", 4],

["What is the national language in Bangladesh", "Bangla","Chatgaiya","English", "Dhakaiya","None",1],

["What is the national animal of BD", "Cow", "Tiger", "Lion", "Dear", "None",2],

["Whats your name?", "Urmi", "Piyal", "Ishfaq", "Mushfiq","None", 3],

["Whats your MOTHER'S name?", "Urmi", "Piyal", "Ishfaq", "Rubi","None", 4],

["Whats your FATHER'S name?", "Urmi", "Younus", "Ishfaq", "Rubi","None", 2],

["Whats your school?", "PSU", "ASU","CAL State","NYCU", "None",1],

["Whats the lowest wage in Oregon","11","12","13","15", "None",4],
]



levels=[1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 16000, 32000]

money=0

for i in range(0, len(questions)):
    question=questions[i]
    print(f"Questions for BDT. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}             b. {question[2]} ")
    print(f"c. {question[3]}             d. {question[4]} ")
    reply=int(input("What is the CORRECT ANSWER? (1-4)"))

    if (reply==question[-1]):
        print(f"Sahi Jawabbbbbbb! You have won BDT. {levels[i]} \n\n")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
    else:
        print("Wrong Answer \n")
        break

print(f"You have won BDT {money}")
