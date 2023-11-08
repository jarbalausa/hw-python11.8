#level1
#1
empty_tuple=()
#2
sisters=("Amanda","Camelia","Largina")
brothers=("Asherl","Camelius","Talgin")
#3
sis_and_bro= sisters + brothers
#4
print(len(sis_and_bro))
#5
family_members=sis_and_bro + ("Granabel" ,"Hanquerk")
print(family_members)

#lvl2
#1
family_members=list(family_members)
parents=family_members[-2:]
sublings=family_members[0:6]
print(parents )


*sis_and_bro, par7 ,par8 =family_members
print(sis_and_bro)
print(f"{par7} ,{par8}")



#2
fruits=("ananas","banana","pean","peach")
vegatables=("eegplant","cucumber","tomato","garlic")
animal_products=("milk","cheese","egg","meat")
food_stuff_tp= fruits + vegatables +animal_products
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)

#3
food_stuff_tp=tuple(food_stuff_tp)
middle_item=food_stuff_tp[5:7]
print(middle_item)
#4
first_items=food_stuff_tp[0:3]
last_items=food_stuff_tp[-4:-1]
#5
del food_stuff_tp
#6
print(first_items in food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries) 
print( "Iceland" in nordic_countries)
 






