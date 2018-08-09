
hund = 7
thou = 8
and_word = 3

one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4

twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6

under_20 = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

one_to_9 = one + two + three + four + five + six + seven + eight + nine

tens = (twenty + thirty + forty + fifty + sixty + seventy + eighty + ninety) * 10

twenty_to_99 = (one_to_9 * 8) + tens

one_to_19 = 0
for i in under_20:
    one_to_19 += i

one_to_99 = one_to_19 + twenty_to_99

ands = (and_word * 99) * 9

hundreds = (one+hund + two+hund + three+hund + four+hund + five+hund + six+hund + seven+hund + eight+hund + nine+hund) * 100

thousand = one + thou

total_letters = (one_to_99*10) + ands + hundreds + thousand

print("The total number of letters used to write out 1 to 1000 in words:", total_letters)

k = input('\nAny key to exit')
