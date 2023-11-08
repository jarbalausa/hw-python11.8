words=[ 'Thirty', 'Days', 'Of', 'Python' ]
results=' '.join(words)
print(results)

# 2
words2=[ 'Coding', 'For' , 'All' ]
results2=' '.join(words2)
print(results2)

# 3 
company=results2
company='Coding For All'
# 4
print(company)
# 5
print(len(company))
# 6
print(company.upper())
# 7
print(company.lower())

# 8 capitalize(), title(), swapcase() 
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(company[0:6])

# 10
first_word=('Coding')
print(company.find('Coding'))
print(company.index(first_word))
print(company.rfind('Coding'))
print(company.rindex(first_word))
print(company.startswith('Coding'))
print(company.endswith(first_word))

# 11
print(company.replace('Coding','Python'))

# 12
sentence=('Python for Everyone' )
print(sentence.replace('Everyone','All'))

# 13
print(company.split())

# 14
words3=("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon")
print(words3.split())

# 15
print(company[0])

# 16
print(company[-1])

# 17
print(company[10])
# 18
pyfal=('Python for all')
# 19
codfal=('Coding for all')
print(pyfal , codfal)

# 20
print(company.index('C'))
# 21
print(company.index('F'))

# 22
company2=('Coding For All People.')
print(company2.rindex('l'))

# 23
sentence3=('You cannot end a sentence with because because because because is a conjunction.')
print(sentence3.find('because'))
# 24
sentence4=('You cannot end a sentence with because because because is a conjunction')
print(sentence4.rindex('because'))

# 25,27
slisent=slice(31,55)
print(sentence4[slisent])

#26
print(sentence4.find('because'))

# # 28
# sub_string='Coding'
# print(compony.index(sub_string)) #error

# # 29
# sub_string2='coding'
# print(company.rfind(sub_string))  #error

# 30
print(company.lstrip())
print(company.rstrip())


# 31
sentence5 = '30DaysOfPython'
print(sentence5.isidentifier()) 
sentence6 = 'thirty_days_of_python'
print(sentence6.isidentifier())

# 32
python_library= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print( '# '.join(python_library))

# 33
sentences=("I am enjoying this challenge. /n I just wonder what is next.")
print(sentences)

# 34
tabs=("Name/tAge/tCountry/tCity")
tabs2=("Asabeneh/t250/tFinland/tHelsink")

# 35
radius=10
pi=3.14
area=pi* radius ** 2
form_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)

# 36 
a=8
b=6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a}*{b} = {a*b}')
print(f'{a}/{b} = {a/b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a}//{b} = {a//b}')
print(f'{a} ** {b} = {a**b}')