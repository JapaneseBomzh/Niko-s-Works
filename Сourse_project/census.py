import openpyxl
from adress_list import Daddress,DOblast
#Ім'я
name = input('Ім\'я українською мовою. Будь ласка, вказуйте ТОЧНО так само, як вказано в документі, що посвідчує особу.\n')

#Призвище
surname = input('Прізвище українською мовою. Будь ласка, вказуйте ТОЧНО так само, як вказано в документі, що посвідчує особу.\n')
 
#По батькові
fathers_name_q = input("Чи є у Вас по батькові? (1 - так, 2 - ні): \n")
while fathers_name_q not in ('1', '2'):
    print("Введіть коректне значення ")
    fathers_name_q = input('Чи є у Вас по батькові? (1 - так, 2 - ні): \n')
if fathers_name_q == "1":
    fathers_name = input("По батькові українською мовою. Будь ласка, вказуйте ТОЧНО так само, як вказано в документі, що посвідчує особу.\n")
else:
    fathers_name ="-"

#Номер телефону
phone = input('Введіть номер телефону у форматі XХХХХХХХХХ. \n')
while len(phone) != 10 or not phone.isdigit():
    print("Номер телефону повинен містити 10 цифр\n")
    phone = input('Введіть номер телефону у форматі XХХХХХХХХХ. \n')

#Область,Район,Адреса
print('Введіть адресу місця постійного проживання: \n')
oblast = DOblast(1)
rayon ,home_adress=Daddress(oblast)

#2 - Стать
gender = input('Будь ласка, зазначте стать . Будь ласка, оберіть одну відповідь із запропонованих нижче. \n 1 - чоловіча\n2 - жіноча\n3 - Небінарна \n4 - Інша\n5 - Не хочу говорити \n')
while gender not in ('1', '2', '3', '4', '5'):
    print("Введіть коректне значення статі(Число)")
    gender = input('Будь ласка, зазначте стать . Будь ласка, оберіть одну відповідь із запропонованих нижче. \n 1 - чоловіча\n2 - жіноча\n3 - Небінарна \n4 - Інша\n5 - Не хочу говорити \n')

#4 - Дата Народження
birthdate = input('Введіть дату народження (дд/мм/рррр): \n')
while True:
    try:
        day, month, year = map(int, birthdate.split('/'))
        if len(birthdate) != 10 or birthdate[2] != '/' or birthdate[5] != '/' or not (1 <= month <= 12) or not (1 <= day <= 31):
            raise ValueError
        break
    except ValueError:
        print("Введіть коректний формат дати народження (дд/мм/рррр)\n")
        birthdate = input('Введіть дату народження (дд/мм/рррр): \n')

#4 - Скільки виповнилось років
age = int(input("Введіть Ваший повний вік: \n"))

#5 - Місце народження
print('Введіть місце народження: \n')
birthplace = DOblast(2)

#6 - Етнічне походження
ethnicity = input('Введіть етнічне походження (вкажіть національність або етнічну групу): \n')

#7 - Рідна мова
native_language = input('Введіть Вашу рідну мову: \n')
if native_language.lower() != 'українська': #7 - Володіння українською мовою
    ukrainian = input('Володієте українською мовою? (1 - так, 2 - ні): \n')
else:
    ukrainian = "1"
other_language = input('Введіть іншу мову, якою Ви вільно володієте: \n')#7 - Інша мова

#8 - Громадянство
сitizenship = input('Введіть Ваше громадянство \n1 - Україна \n2 - без громадянства \n3 - інша держава\n')
while сitizenship not in ('1', '2', '3'): 
    print("Введіть коректне значення ")
    сitizenship  = input('Введіть Ваше громадянство \n1 - Україна \n2 - без громадянства \n3 - інша держава\n')
if сitizenship == "3":
    сitizenship=input("Введіть Вашу країну , де Ви маєте громадянство:\n")

#9 - Сімейний стан
if age >= 15:    
    marital_statuses = ["1", "2", "3", "4", "5", "6"]
    marital_status = input("Ваш сімейний стан (для осіб віком 15 років і старших) - \n1 ніколи не перебував(ла) у шлюбі, \n2 перебуваю у зареєстрованому шлюбі, \n3 перебуваю у незареєстрованому шлюбі, \n4 удівець, удова, \n5 розлучений(на), \n6 розійшовся(лася): ")
    while marital_status not in marital_statuses:
        print("Введіть коректний сімейний стан")
        marital_status = input("Ваш сімейний стан (для осіб віком 15 років і старших) - \n1 ніколи не перебував(ла) у шлюбі, \n2 перебуваю у зареєстрованому шлюбі, \n3 перебуваю у незареєстрованому шлюбі, \n4 удівець, удова, \n5 розлучений(на), \n6 розійшовся(лася): ")
else:marital_status ="-"

#10 - Освіта
if age >= 6:
    education = input("Ваша освіта: \n1 повна вища (вища);\n2 базова вища ;\n3 початкова вища(середня спеціальна);\n4 незакінчена вища(для осіб, які закінчити навчання до 1996 року) ;\n5 повна загальна середня(середня загаьна);\n6 базова загальна середня(неповна середня) ;\n7 початкова загальна (початкова) ;\n8 не маю початкової загальної ;\n9 неписьменний(на) ")
    while education not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Некоректне значення. Будь ласка, введіть число від 1 до 9.")
        education = input("Ваша освіта: \n1 повна вища (вища);\n2 базова вища ;\n3 початкова вища(середня спеціальна);\n4 незакінчена вища(для осіб, які закінчити навчання до 1996 року) ;\n5 повна загальна середня(середня загаьна);\n6 базова загальна середня(неповна середня) ;\n7 початкова загальна (початкова) ;\n8 не маю початкової загальної ;\n9 неписьменний(на) ")
    while True:
        try:
            education_info = input("Введіть назву навчального закладу, кількість класів(курсів) та рік закінчення (в такому форматі: 'Назва закладу, кількість класів(курсів)(число), рік(число)')\nЯкщо  незакінчував ніякий навчальий заклад \"-\" \n")
            if education_info == "-":
                school = "-";classes = "-";eyear = "-"
                break
            else:
                school, classes, eyear = education_info.split(", ")
                break
        except ValueError:
            print("Ви ввели неправильний формат даних. Спробуйте ще раз.")
else: education = "-"; education_info = "-"
#11 - Чи закінчили п-т навч. заклад? 
if age >= 15:    
    vocational_school = input("Ви закінчили професійно-технічний навчальний заклад (введіть 1 для так або 2 для ні): ")
    while vocational_school not in ["1", "2"]:
        print("Некоректне значення. Будь ласка, введіть 1 для так або 2 для ні.")
        vocational_school = input("Ви закінчили професійно-технічний навчальний заклад (введіть 1 для так або 2 для ні): ")    
else: vocational_school ="-"

#12 - Тип навчального закладу
if age >= 6: #???
    education_type = input("Тип навчального закладу, в якому Ви навчаєтесь (для осіб віком 6 років і старших):\n1 - вищий\n2 - професійно-технічний\n3 - загальноосвітній\n4 - інший навчальний заклад (курси)\n5 - не навчаюсь\nДля осіб віком до 7 років, які не відвідують школу вказати, чи відвідують дошкільний заклад:\n6 - так\n7 - ні ")
    while education_type not in ["1", "2", "3", "4", "5", "6", "7"]:
         print("Некоректне значення. Будь ласка, введіть число від 1 до 7.")
         education_type = input("Тип навчального закладу, в якому Ви навчаєтесь (для осіб віком 6 років і старших):\n1 - вищий\n2 - професійно-технічний\n3 - загальноосвітній\n4 - інший навчальний заклад (курси)\n5 - не навчаюсь\n Для осіб віком до 7 років, які не відвідують школу вказати, чи відвідують дошкільний заклад:\n 6 	так \n7 ні ")
else: education_type ="-"

#13 - Джерела засобів існування
set_chosen_sources = set()
while True:
    chosen_source = input("Виберіть джерело засобів існування:\n1 - робота на підприємстві, в організації, установі, селянському (фермерському) господарстві\n2 - робота у окремих громадян\n3 - робота на власному підприємстві\n4 - робота на індивідуальній основі\n5 - робота у власному селянському (фермерському) господарстві\n6 - робота на сімейному підприємстві без оплати праці\n7 - робота в особистому підсобному господарстві\n8 - прибуток від власності\n9 - пенсія\n10 - стипендія\n11 - допомога (крім допомоги по безробіттю)\n12 - допомога по безробіттю\n13 - інший вид державного забезпечення\n14 - на утриманні інших осіб\n15 - інше джерело\n")
    if chosen_source.isdigit() and chosen_source in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'):
        set_chosen_sources.add(chosen_source)
    else:
        print("Некоректне значення. Будь ласка, введіть число від 1 до 15.")
    chose = input(f"Обрані джерела засобів існування: {set_chosen_sources}\nБажаєте додати ще? (1 - так, 2 - ні): ")
    while chose not in ('1', '2'):
        print("Некоректне значення.") 
        chose = input(f"Обрані джерела засобів існування: {set_chosen_sources}\nБажаєте додати ще? (1 - так, 2 - ні): ")
    if chose == '2':
        break

#13 - Номер основного джерела засобів існування
main_source = input("Вказати номер основного джерела засобів існування (1-15): ")
while main_source not in set_chosen_sources:
    print("Некоректне значення.") 
    main_source = input("Вказати номер основного джерела засобів існування (1-15): ")

#Збереження даних
wb = openpyxl.load_workbook('census.xlsx')
ws = wb.active

row = ws.max_row + 1
ws.cell(row=row, column=1, value=row-1)
ws.cell(row=row, column=2, value=name)
ws.cell(row=row, column=3, value=surname)
ws.cell(row=row, column=4, value=fathers_name)
ws.cell(row=row, column=5, value=phone)
ws.cell(row=row, column=6, value=oblast)
ws.cell(row=row, column=7, value=rayon)
ws.cell(row=row, column=8, value=home_adress)
ws.cell(row=row, column=9, value=gender)
ws.cell(row=row, column=10, value=birthdate)
ws.cell(row=row, column=11, value=birthplace)
ws.cell(row=row, column=12, value=ethnicity)
ws.cell(row=row, column=13, value=native_language)
ws.cell(row=row, column=14, value=ukrainian)
ws.cell(row=row, column=15, value=other_language)
ws.cell(row=row, column=16, value=сitizenship)
ws.cell(row=row, column=17, value=marital_status)
ws.cell(row=row, column=18, value=education)
ws.cell(row=row, column=19, value=education_info)
ws.cell(row=row, column=20, value=vocational_school)
ws.cell(row=row, column=21, value=education_type)
ws.cell(row=row, column=22, value=', '.join(set_chosen_sources))
ws.cell(row=row, column=23, value=main_source)
wb.save('census.xlsx')