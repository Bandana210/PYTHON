print("he said \" he wants to eat apple \" ")
print('''he said "hi" ''')

name= "bandana jain"
print(name[5])

## string is like an array of characters -- not exactly array

for i in name:
    print(i)


## STRING SLICING

print(name[2:9])                        ## include 2 but not 9
print(name[2:])
print("length is" ,len(name))                ##len(str)
print(name)
print(name[0:-3])
print(name[-1:len(name)-3])
print(name[-6:-1])

nm="harry"
print(nm[-4:-2])

## STRING METHODS

# strings are immutale -- i can make a copy and then make changes in that copy

## upper / lower
a="Harry"
print(a.upper())
print(a)
print(a.lower())

## rstrip/lstrip/strip

b="!!!!bandana!!!"
print(b.rstrip("!"))
print(b.strip('!'))

## replace ---  replace all  occurence in the string
c= "my name is Bandana jain. bandana is a CSE undergrad. bandana is learning python "
print(c.replace("bandana", 'she'))

## split  --- makes list --- elemnts after each space are list elemnet  --- space required 
d="bandana jain how are you"
print(type(d))
print(d.split())
print(type(d.split()))
print(type(d))

## capitalise
e="bandana jain. she is 20."
print(e.capitalize())

## center
print(e.center(50))
print(len(e))
print(len(e.center(50)))

f="welcome to python. welcome to vscode ide"
print(f.count('to'))
print(f.endswith("ide"))
print(f.endswith('to',4,10))
print(f.find('to'))               ##  1st occurence ka index
print(f.find('bandana'))


# islower()
# isspace()
# istitle()
# startswith()
# swapcase()
# title()s
# isalpha()

g="bandana jain \n age 20"
print(g.isprintable())                      # \n is not printable character -- hence false 
h="welcome 20"
j="welcome"

print(b.isalnum())
print(h.isalnum())
print(j.isalnum())

