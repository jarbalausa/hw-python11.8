#1 ,2
face_part=['eye','nose','lips','hair','face']
# 3
print(len(face_part))
# 4
print(face_part[0])
print(face_part[2])
print(face_part[4])
#5
mixed_data_types=('Balaussa', '18', '160cm','single', 'Dosmukhambet srt. "160a')
print(mixed_data_types)

#6 ,7 ,8,9 book, Google, Microsoft, Apple, IBM, Oracle и Amazon.
it_companies=('Face-book','Microsoft','Apple', 'IBM','Oracle' , 'Amazon')                                                                      
print(len(it_companies ))
print(f"First company's {it_companies[0]} ,mid company's {it_companies[3]}  and last company's {it_companies[-1]}")
#10,11,12
it_companies[-2]= 'Capgemini'
print(it_companies)
it_companies.append('Infosys')
print(it_companies)
it_companies.insert(5,'TCS')
print(it_companies)
# 13
a= it_companies[6].uppper()
print(a)

# 14
print(" # " .join(it_companies))

# 15
print('Prada' in it_companies)

# 16 ,17
print(sorted(it_companies ,reverse=True))
# 18,19,20
print(it_companies[0:3])
print(it_companies[-1:-4])
print(it_companies[5])

# 21,22,23,24,25
print(it_companies.pop[0])
print(it_companies.pop[5])
print(it_companies.pop[-1])
print(it_companies.clear())
del it_companies

# 26,27

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack= front_end + back_end
full_stack.append('Python','SQL','Redux')
print(fullstack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(sorted(ages))
min_age= ages[0]
max_age=ages[-1]
middle_age =max_age- min_age
aver_age = sum(ages) / len(ages)
mid_age=ages[5]
midpoint = int(mid_age) //2
min_average=abs(middle_age-min_age)
max_average=abs(middle_age-max_age)
print(f"Min age's {min_age} in average {min_average} . Max age's {max_age} in average {max_average}.Middle age's {middle_age}.Midpoint in the ages {midpoint}. Average in the summary {aver_age} ")
country=['Китай', 'Россия', 'США', 'Финляндия', 'Швеция', 'Норвегия', 'Дания']
print(country[3])
country_even=('Китай','США','Швеция','Дания')
country2=('Россия' ,'Финляндия', 'Норвегия')
print(country_even)
coutry1 ,country2 , country3 , *scandinavian_country=country
print(scandinavian_country)










