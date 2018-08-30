from random import shuffle

names = ["Steve", "Andrea", "Kirsty", "Cynthia", "Suman", "Sean", "Peter", "Ben ", "Jay "]

names_baking = names[:]
names_paper = names[:]

shuffle(names_paper)
shuffle(names_baking)

ready = False

while not ready:
	hit = False
	for i in range(len(names)):
		if names_paper[i] == names_baking[i]:
			hit = True
	if hit:
		shuffle(names_paper)
	else:
		ready = True

		
	
for i in range(len(names)):
	paper = names_paper[i]
	baker = names_baking[i]

	print("Session #{}: Baker: {} \tPaper: {}".format(i+1, baker, paper))
