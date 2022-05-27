


import random


def main():
   randlist = []

   for i in range(0, 15):
       n = random.randint(1, 200)
       randlist.append(n) 

   print(f"Unsortierte Liste: {randlist}")

   u_input = input("Aufsteigend oder absteigend sortieren? asc/desc ")

   if u_input.lower() == 'desc':
     desc_sort(randlist)

   if u_input.lower() == 'asc':
     asc_sort(randlist)



def desc_sort(randlist):
    mv = randlist[0]

    randlist_length = len(randlist)


    i = 0
    l = i + 1

    for i in range (randlist_length):
        for l in range (randlist_length):
            if randlist[i] > randlist[l]:
                mv = randlist[l]
                randlist[l] = randlist[i]
                randlist[i] = mv

    print(f"Sortierte Liste: {randlist}")


def asc_sort(randlist):
    mv = randlist[0]

    randlist_length = len(randlist)


    i = 0
    l = i + 1

    for i in range (randlist_length):
        for l in range (randlist_length):
            if randlist[i] < randlist[l]:
                mv = randlist[l]
                randlist[l] = randlist[i]
                randlist[i] = mv

    print(f"Sortierte Liste: {randlist}")
    


if __name__ == '__main__':
    main()