#შექმენით სია სადაც, შეიტანთ მინიმუმ 10 რიცხვს, გადაუარეთ for 
# ციკლის დახმარებით და დაბეჭდეთ თითოეული რიცხვი კენტია თუ ლუწი.
numbers = [1,2,3,4,5,6,7,8,9,10]


for number in numbers:
    if number % 2 == 0:
        print("ლუწი")
        
    else:
        print("არის კენტი")



#შექმენით სახელების სია სადაც გექნებათ მინიმუმ 10 სახელი, დაბეჭდეთ ამ 
#სიიდან მხოლოდ ის სახელები რომლების ინდექსებიც არის ლუწი

names = ["saba","sandro","givi","ana","ikuna","aleqsandre","rezi","aleko","nika","oto"]

for index in range(len(names)):
    if index % 2 == 0:
       print ([index] + (names))
       
