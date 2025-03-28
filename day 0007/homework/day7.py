# 2) ცვლადები და მონაცემთა ტიპების შემოწმება
int_var = 10  # integer
float_var = 3.14  # float
str_var = "Hello, world!"  # string
bool_var = True  # boolean
list_var = [1, 2, 3, 4]  # list

# მონაცემთა ტიპების შემოწმება
print("int_var ტიპი:", type(int_var))  # <class 'int'>
print("float_var ტიპი:", type(float_var))  # <class 'float'>
print("str_var ტიპი:", type(str_var))  # <class 'str'>
print("bool_var ტიპი:", type(bool_var))  # <class 'bool'>
print("list_var ტიპი:", type(list_var))  # <class 'list'>

# 3) მომხმარებლისგან რიცხვის მიღება და მონაცემთა ტიპის შემოწმება
user_input = input("შეიყვანეთ რიცხვი: ")

# შემოწმება და ტიპის გარდაქმნა
user_input_int = int(user_input)
print("შემოტანილი რიცხვის ტიპი:", type(user_input_int))  # <class 'int'>

# 4) შედარების ოპერატორები
print("\n1. ტოლი == ოპერატორი")
print(10 == 10)  # True
print(10 == 5)  # False

print("\n2. არ არის ტოლი != ოპერატორი")
print(10 != 5)  # True
print(10 != 10)  # False

print("\n3. დიდი > ოპერატორი")
print(10 > 5)  # True
print(5 > 10)  # False

print("\n4. ნაკლები < ოპერატორი")
print(5 < 10)  # True
print(10 < 5)  # False

print("\n5. დიდი ან ტოლი >= ოპერატორი")
print(10 >= 10)  # True
print(5 >= 10)  # False

# 5) `and` და `or` ოპერატორები
print("\n`and` ოპერატორი")
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

print("\n`or` ოპერატორი")
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# 6) ასაკის ტიპის გარდაქმნა
age_str = input("\nშეიყვანეთ თქვენი ასაკი: ")
print("ასაკის ტიპი (სტრინგი):", type(age_str))  # ყოველთვის str

# სტრინგის გარდაქმნა integer-ად
age_int = int(age_str)
print("ასაკის ტიპი (integer):", type(age_int))

# integer-ის გარდაქმნა float-ად
age_float = float(age_int)
print("ასაკის ტიპი (float):", type(age_float))

# 7) საყვარელი რიცხვის შემოწმება, არის თუ არა ლუწი
favorite_number = int(input("\nშეიყვანეთ თქვენი საყვარელი რიცხვი: "))

if favorite_number % 2 == 0:
    print(f"{favorite_number} არის ლუწი რიცხვი.")
else:
    print(f"{favorite_number} არ არის ლუწი რიცხვი.")

# 8) ასაკის და სახელის შემოწმება
name = input("\nშეიყვანეთ თქვენი სახელი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if age >= 18:
    print("თქვენი ასაკი არის სრულწლოვანი.")
else:
    print("თქვენი ასაკი არაა სრულწლოვანი.")

if name.lower() == "თქვენი სახელი".lower():
    print("თქვენი სახელი ემთხვევა ჩემს სახელს!")
else:
    print("თქვენი სახელი არ ემთხვევა ჩემს სახელს.")
