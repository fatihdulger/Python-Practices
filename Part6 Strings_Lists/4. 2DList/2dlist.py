
twoDlist = [

#i 0         1      2       3

["Anna", "Lucian", "Em", "Jane"], #0

[1,2,3,10], #1

["SDLC", "HTML","CSS","JS"]#2

]

# access values by index

print(twoDlist[0][0], twoDlist[1][0], twoDlist[2][0]) # 2D list how to reach what we want

print(twoDlist[0][1], twoDlist[1][1], twoDlist[2][1])  # 2 D list

for i in twoDlist:
    
    # print(i[:3])
    for b in i:
        #numCheck = int(input("Enter a number"))
        if b == 3: # numCheck
           print(b)


print("Enumerate............")  ## this is to go deeper into the list and you can study this.

for c , a in enumerate(twoDlist): # c, a are variable you can put anything you like.

    print(f"This is List {c} and items {a} ")
    for d, f in enumerate(a):
        print(f"this is index position {d} and the item is {f} ")


for x in twoDlist:


# Gyula's 
    for y in x:

        listIndex = x.index(y)

        if y == 'Anna':

            index = y.index('Anna')

            print(f'found Anna in [{listIndex}] [{index}]')

       