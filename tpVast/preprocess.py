import random


rnd_numbs = random.sample(range(1010), 100)

f= open("./media/Participants_sample.csv","w+")

f.write("participantId")

for i in rnd_numbs:
    f.write(str(i) + "\n")

f.close()



