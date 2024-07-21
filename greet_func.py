def greet(name = input("Your Name : ")):
    if len(name) < 3 :
        print("Name should be greater than 3 words.")
        while len(name) < 3 :
            name = input("Your Name : ")
    if len(name) > 16 :
        print('Name should be smaller than 16 words.')
        while len(name) > 16:
            name = input("Your Name : ")  
    print("Welcome,",name.title())
greet()
