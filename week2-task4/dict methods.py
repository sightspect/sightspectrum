
#-----------DICTIONARIES METHODS--------------------

#-----FROMKEYS---------
##n={"jdks","urfh","jheb","erj"}
##c={34,46}
##print(dict.fromkeys(n,c))

##n={"jdks","urfh","jheb","erj"}
##c=34
##print(dict.fromkeys(n,c))

##n={("jdks"),("urfh","jheb"),"erj"}
##c=34
##print(dict.fromkeys(n,c))

##n={["jdks"],["urfh"],["jheb"],["erj"]}
##c={[5]}
##print(dict.fromkeys(n,c))

##n=["jdks","urfh","jheb","erj"]
##c={5}
##print(dict.fromkeys(c,n))


##n={["jdks","urfh","jheb","erj"]}
##c={[34]}
##print(dict.fromkeys(n,c))

#-----------GET------------
##s={"sz":5,"kthlr":56,"ghf":76}
##print(s.get("sz"))

##s={"hello":34,"divya":35,"hi":56}
##a=s.get("hello")
##print(a)

##w={"jock":12,"hello":875,"get":98}
##a=w.get("jock")
##print(a)

##s={"jsd":76,"jjjj":676}
##a=s.get("jsd")
##print(a)

##x={"model":"tata","brand":34}
##s=dict.values()
##print(s)

##var = {"name":{"divya":{"surname":["s","m","n"]}}}
##var["name"]["divya"]["surname"][2]="a"
##print(var)


##var = {"name":{1:{"surname":["s","m","n"]}}},"jega",{1:{"surname":["s","m","n"]}}
##var["name"][1]["surname"]["jega"]["surname"][2]="l"
##print(var)

##var = {"name":{1:{"surname":["s","m","n"]}},"jega":{1:{"surname":["s","m","n"]}}}
##print(var)               

##import json
##var = '{"country":"india"}'
##print(type(var))
##output = json.dumps(var)
##print(type(output))

#-----------KEYS--------------
##b={"hello":23,"divya":89,"age":12}
##print(b.keys())
##
##s={"name":{"divya":{"age":12,"home":(9.464,7648,7747)}}}
##print(s.keys())


#---------POP--------------
##d={"hsj":43,"jkewh":7874,"uher":"ygef"}
##print(d.pop("hsj"))
##
##a={("jjk"):{"hdbh":(2,4,5,6)}}
##print(a.pop("jjk"))
##


#----------SETDEFAULT--------
##a={"name":"divya","age":23,"hello":123}
##print(a.setdefault("color"))
##
##
##a={"name":"divya","age":23,"hello":123}
##print(a.setdefault("color","white"))
##
##q={"hello":{"divya":{"age":34,"hi":23}}}
##print(q.setdefault("divya","food"))


















































































































