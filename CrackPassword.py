import random,string,operator

def fitness(password,word):
    password_size = len(password)
    if password_size != len(word):
        print("Wrong Size!!")
        return
    score = 0
    for i in range(password_size):
        if password[i] == word[i]:
            score+=1
    return score*100/password_size

def gen_start_pop_(password_size,size_pop):
    pop =[]
    for i in range(size_pop):
        specimen= ''
        for j in range(password_size):
            # lettes and numbers
            # 1-16 num, 17-100 letter
            if random.randint(0,100) < 17:
                specimen+=random.choice(string.digits)
            else:
                specimen+=random.choice(string.ascii_letters)
        pop.append(specimen)
    return pop

def pop_fitness(pop,password):
    pop_score={}
    for specimen in range(len(pop)):
        pop_score[specimen]=fitness(password,pop[specimen])
    return sorted(pop_score.items(),key=operator.itemgetter(1),reverse = True)

def chosen_pop(pop,pop_ord,best,randoms):
    next_gen=[]
    for i in range(best):
        next_gen.append(pop[pop_ord[i][0]])
    for i in range(randoms):
        next_gen.append(pop[random.choice(pop_ord)[0]])
    random.shuffle(next_gen)
    return next_gen

def gen_child(ind1,ind2):
    child =''
    for i in range(len(ind1)):
        if (int(100 * random.random()) < 50):
            child+= ind1[i]
        else:
            child+= ind2[i]
    return child

def gen_children(pop,number_child):
    next_pop =[]
    for i in range(len(pop)//2):
        for j in range(number_child):
            next_pop.append(gen_child(pop[i],pop[len(pop)-1-i]))
    return next_pop


def mutation(pop, taxa):
	for i in range(len(pop)):
		if random.random()*100 < taxa:
			pop[i] = mutacao_individuo(pop[i])
	return pop

def mutacao_individuo(individuo):
	indice = int(random.random() * len(individuo))
	letra = random.choice(string.ascii_lowercase)
	if indice == 0:
		individuo = letra + individuo[1:]
	else:
		individuo = individuo[:indice] + letra + individuo[indice+1:]
	return individuo

password='PassWord'
size_password = len(password)
size_pop = 1000 #tip: 10 to 1000
best = int(0.6 * size_pop)
randoms = int(0.4 * size_pop)
number_child=2
mutation_tax = 5
max_iter= 10000 # tip: 100 to ∞
find = 0

pop = gen_start_pop_(size_password,size_pop)
for i in range(max_iter):
    pop_ord = pop_fitness(pop,password)
    pop = chosen_pop(pop,pop_ord,best,randoms)
    pop =gen_children(pop,number_child)
    pop =mutation(pop,mutation_tax)
    index_best, score_best =pop_fitness(pop,password)[0]
    if(score_best == 100):
        print("find password in %d gen" % (i))
        print("Your password '%s' " % (pop[index_best]))
        find = 1
        break
    else:
        print("gen ",i)
        print(pop)
        find = i
if( find != 1):
    print('cant find your password in %d gen' % (find+1))