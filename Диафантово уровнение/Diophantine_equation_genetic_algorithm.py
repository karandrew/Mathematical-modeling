from random import randint
 
class Genetic:
    def __init__(self,gen=None,id=None):
        '''
       Инициализация отдельной особи.
       self.gen - генотип особи
       self.id - уникальный идентификатор для кроссовера
       '''
        if gen != None:
            self.gen = gen
        else:
            self.gen = [randint(1,30) for i in range(1,5)]
           
        if id != None:
            self.id = gen
        else:
            self.id = randint(0,2)
           
    def fitness(self):
        '''
       Функция приспособленности.
       '''
        a,b,c,d = self.gen
        return (a+2*b+3*c+4*d)-30
   
    def crossover(self,f):
        '''
       Кроссовер.
       Перемешивание генотипов.        
       '''
       
        # гены исходной особи
        a,b,c,d = self.gen
        mid = self.id
       
        # гены некоторой другой особи
        aa,bb,cc,dd = f.genotype()
        fid = f.show()
       
        if mid == 0:
            if mid == fid:
                return Genetic([a,bb,cc,dd])
            else:
                return Genetic([aa,b,c,d])
        elif mid == 1:
            if mid == fid:
                return Genetic([a,b,cc,dd])
            else:
                return Genetic([aa,bb,c,d])
        else:
            if mid == fid:
                return Genetic([a,b,c,dd])
            else:
                return Genetic([aa,bb,cc,d])
                   
    def genotype(self):
        '''
       Генотип особи.
       '''
        return self.gen
 
    def show(self):
        '''
       Идентификатор кроссовера.
       '''
        return self.id
       
       
class Population:
    def __init__(self,num=10):
        '''
       Создаем популяцию из num экземпляров.
       По умолчанию - 10 особей.
       '''
        self.p = [Genetic() for i in range(1,num+1)]
       
    def cross(self):
        '''
       Кроссовер внутри популяции.
       '''
        from random import sample
        l = len(self.p)
        # создаем две перемешанных копии популяции
        # для выполнения кроссовера
        f = sample(self.p,l)
        m = sample(self.p,l)
        z = []
        # сам кроссовер
        for i in range(0,len(f)):
            z.append(f[i].crossover(m[i]))
           
        # промежуточная функция для выполнения
        # "естественного отбора"
        def check(a,b):
            if a.fitness() < b.fitness():
                return a
            else:
                return b
        # популяция после отбора
        self.p = list(map(check,self.p,z))
       
    def mutate(self):
        '''
       Генератор мутаций внутри популяции.
       '''
        l = len(list(self.p))
        num = int(l*0.4213)+1 # количество мутаций
       
        for i in range(1,num):
            v = randint(0,l-1) # элемент популяции нужный для мутации
            p = self.p.pop(v) # запоминаем этот элемент и удаляем его из популяции
            ex = p.genotype() # выясняем его генотип
            ind = randint(0,3) # выбираем элемент генотипа для мутации
            ex.pop(ind)   # удаляем его
            ex.insert(ind,randint(1,30)) # вставляем мутацию
            self.p.append(Genetic(ex)) # вставляем мутированную особь
       
    @property
    def view(self):
        '''
       Все особи популяции.
       '''
        return self.p
 
# популяция из 50 особей                
x = Population(150)
 
# запускаем развитие в течение 15 поколений.
for i in range(1,15):
    x.cross()
    x.mutate()
   
# отсеиваем особей с генотипами, соответствующими решениям
# диофантова уравнения    
k = [i for i in x.view if i.fitness() == 0]
 
if len(k) == 0:
    print('Решений не обнаружено! Попробуйте еще раз')
else:
    for i in k:
        print (i.genotype())
