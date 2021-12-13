import re

f = open("input6.txt",'r')
lines = f.readlines()

fish = {i:0 for i in range (0,9)}
for line in lines:
    for num in re.split(r'\D+', line):
        fish[int(num)] += 1

print("Intial State: ",fish)

def simulate_day(fish, day):
    births = fish[0] 
    for i in range(0,8):
        fish[i] = fish[i + 1]
    fish[6] += births
    fish[8] = births

    print("Fish after day ", day, ": ", sum(fish.values()))

for day in range(0,256):
    simulate_day(fish, day)


