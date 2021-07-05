#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.



words = [1000]

words = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
decades = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

for d in decades:
    words.append(d)
    for i in range(0,9):
        words.append(str(d + words[i]))

for j in range(0,9):
    words.append(str(words[j] +'hundred'))
    for k in range(0,99):
        words.append(str(words[i]+'hundredand'+words[k]))

words.append('onethousand')

c = 0
for w in words:
    c = c + len(w)

print(c)