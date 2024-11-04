# setting up the high score and ranking
score = 30
file = open('score.txt', 'r')
tempstr = ''
for ans in file:
    tempstr = tempstr+ans
words = tempstr.split('-')
h = []
for each in words:
    h.append(int(each))
if (h[0] < score):
    h[0] = score
    print("hey you got 1st rank")
elif (h[1] < score):
    h[1] = score
    print("hey you got 2nd rank")
elif (h[2] < score):
    h[2] = score
    print("hey you got 3rd rank")
file.close()
file = open('score.txt', 'w')
file.write(str(h[0]))
file.write("-")
file.write(str(h[1]))
file.write("-")
file.write(str(h[2]))

file.close()
file = open('score.txt', 'r')
print("score ranking is:")
Rcount = 1
tempstr = ''
for ans in file:
    tempstr = tempstr+ans
words = tempstr.split('-')
for each in words:
    print("rank", Rcount, "score is", each)
    Rcount += 1
