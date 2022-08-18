n = input().split(" ")
first_person = n[0]
second_person = n[1]
if ((first_person == 'R' and second_person == 'S') or (first_person == 'S' and second_person == 'R')):
    print("R")
elif ((first_person == 'P' and second_person == 'S') or (first_person == 'S' and second_person == 'P')):
    print("S")
elif ((first_person == 'R' and second_person == 'P') or (first_person == 'P' and second_person == 'R')):
    print("P")
elif (first_person == 'P' and second_person == 'P'):
    print("D")
elif (first_person == 'R' and second_person == 'R'):
    print("D")
elif (first_person == 'S' and second_person == 'S'):
    print("D")

