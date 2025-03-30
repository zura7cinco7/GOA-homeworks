even_sum = 0
odd_sum = 0

for i in range(1, 21):
    if i % 2 == 0:
        even_sum += i 
    else:
        odd_sum += i 

even_sum_5th_power = even_sum ** 5
odd_sum_5th_power = odd_sum ** 5

if even_sum_5th_power > odd_sum_5th_power:
    print(f"ლუწი რიცხვების ჯამი (5-ე ხარისხში): {even_sum_5th_power}")
else:
    print(f"კენტის რიცხვების ჯამი (5-ე ხარისხში): {odd_sum_5th_power}")
