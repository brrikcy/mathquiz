import random
def generate_options(res):
    options = []
    options.append(res)
    for i in range(3):
        options.append(random.randint(res-40,res+40))
    random.shuffle(options)
    for j in options:
        print(j)
    answer = int(input("choose an answer: "))
    if answer == res:
        print("correct")
    else:
        print("wrong")
def qsum():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    result=num1+num2
    print(f"{num1} + {num2} ")
    generate_options(result)
def qdif():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    result=num1-num2
    print(f"{num1} - {num2} is ")
    generate_options(result)
def qpro():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 100)
    result=num1*num2
    print(f"{num1} * {num2} is ")
    generate_options(result)
def qdiv():
    num1 = random.randint(50, 1000)
    num2 = random.randint(2, 50)
    while(num1%num2!=0):
        num2 = random.randint(2, 50)
    quest_display = f"{num1} / {num2} is"
    print(quest_display)
    result = int(num1 / num2)
    generate_options(result)
def qmod():
    num1 = random.randint(1, 300)
    num2 = random.randint(1, 300)
    result=num1%num2
    print(f"{num1} % {num2} is ")
    generate_options(result)
operations=[qsum,qdif,qpro,qdiv,qmod]
question=random.choice(operations)
question()
