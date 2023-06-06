#----------------------------------SET---------------------------------------

# SET ARE USED TO STORE MULTIPLE ITEMS IN A SINGLE VARIABLE. SET HAS A FLOWER BRACKET

#SET
##var={1,2,34,5,55,667,99}
##print(var)
##print(type(var))

#-------------------------BUILT IN FUNCTIONS----------------------------------------------

#----------ADD-----------
##var={"hello","divya",45,67,89}
##var.add("world")
##print(var)


##m={23,45,6,78,5,7,6}
##m.add(45)
##print(m)

##m={"bb","mxzm","jhedjd"}
##print(m.add(34))
##print(m)

#----------CLEAR--------
##var={"sddf","dgdfh","gfdfhg"}
##var.clear()
##print(var)

# IT DOES NOT ALLOW TO CLEAR A SPECIFIED ELEMENT
##m={"fgdg","gdfg","hdfh"}
##print(m.clear())


#--------COPY----------
##m={32,454,768,84,5,66}
##m.copy()
##print(m)

#--------------DIFFERENCE------------
##m={"happy","sad","enjoy"}
##n={"divya","gayatri","sad"}
##m.difference_update(n)
##print(m)


##flower={"rose","jasmine","flower"}
##fruits={"apple","jack","mango","flower"}
##print(fruits.difference(flower))

#----------------DISCARD----------
##m={"hi","am","divya"}
##m.discard("hi")
##print(m)

#REMOVE AND DISCARD IS TOTALLY DIFFERENCE BECAUSE REMOVE GIVES ERROR IF THE SPECIFIED ELEMENT IS NOT THEIR BUT DISCARD DOES NOT
##m={"hi","am","divya"}
##m.remove("hi")
##print(m)



#-----------INTERSECTION-----------
##m={"hi","am","divya"}
##n={"am","here","to","do work"}
##m.intersection_update(n)
##print(m)


#-----------DISJOINT--------------
##m={"sad","happy","devil"}
##n={"divya","enjoy"}
##print(m.isdisjoint(n))

#------------SUPERSET-------------
##var={11,23,34,"hi"}
##var1={23,56,67,"am"}
##print(var.issuperset(var1))


#-----------UNION-----------
##m={"happy","sad","enjoy"}
##n={"divya","gayatri","sad"}
##print(m.union(n))




































































































