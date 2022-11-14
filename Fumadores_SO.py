import threading
import random
import time
 
def generateRandomItems():
    item1 = random.randint(1,100)
    item2 = random.randint(1,100)
    item1 %= 3
    item2 %= 3
    if (item1 == item2):
        item2 += 1
        item2 %= 3
    itemList = [item1, item2]
    return itemList
 
class cigaretteSmoker:
    def __init__(self):
        self.condMutex = threading.Condition()
        self.vendorSleep = threading.Semaphore(0)
        self.ingredients = ['TOBACO', 'PAPEL', 'CERILLA']
        # No item is available on table.
        self.availableItems = [False, False, False]
        self.smokerThreads = []
        # Create three smokers threads.
        self.smokerThreads.append(threading.Thread(target=self.smokerRoutine, \
                                  name='Mr.Tabaco', args=(1, 2)))
        self.smokerThreads.append(threading.Thread(target=self.smokerRoutine, \
                                  name='Mr.Papel', args=(0, 2)))
        self.smokerThreads.append(threading.Thread(target=self.smokerRoutine, \
                                  name='Mr.Cerilla', args=(0, 1)))
        for smokers in self.smokerThreads:
            smokers.start()
        # Create vendor thread.
        self.vendorThread = threading.Thread(target=self.vendorRoutine)
        self.vendorThread.start()
 
    def vendorRoutine(self):
        while True:
            # Generate two random items.
            randomItems = generateRandomItems()
            self.condMutex.acquire()
            print('Vendor produced: {0} and {1}'.\
                  format(self.ingredients[randomItems[0]], \
                         self.ingredients[randomItems[1]]))
            # Make items available on table.
            self.availableItems[randomItems[0]] = True
            self.availableItems[randomItems[1]] = True
            # Announce to all smokers that items are made available on table.
            self.condMutex.notify_all()
            self.condMutex.release()
            # Go to sleep till the selected smoker is done with smoking.
            self.vendorSleep.acquire()

    #Indicamos lo items iniciales de cada fimador
    mrTabacoIt,mrPapelIt,mrCerillaIt=5,5,5 #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def smokerRoutine(self, neededItem1, neededItem2, mrTabacoItems=mrTabacoIt, mrPapelItems=mrPapelIt, mrCerillaItems=mrCerillaIt):
        myName = threading.current_thread().name
        initialItems=1
        while (True):

            self.condMutex.acquire()
            # Block till the needed items are on table.
            while (False == self.availableItems[neededItem1] or
                   False == self.availableItems[neededItem2]):
                self.condMutex.wait()
                #Advertencia de sin items restantes
            if initialItems<=0:
                print(f'ADVERTENCIA: ¡{myName} ya no puede fumar! \n ¡Se ha producido un BLOQUEO!')
                raise SystemExit(0)
            self.condMutex.release()
            # Pickup the items from the table.
            self.availableItems[neededItem1] = False
            self.availableItems[neededItem2] = False
            # All ingredients are with you start smoking.
            print('{0} started smoking.'.format(myName))
            print('{0} ended smoking.'.format(myName))

            #Se espera para ver mejor los resultadores en colsola
            # time.sleep(2)

            #Se resta 1 a los items iniciales del fumador que haya fumado
            if myName=='Mr.Tabaco':
                mrTabacoItems-=1
            elif myName=='Mr.Papel':
                mrPapelItems-=1
            elif myName=='Mr.Cerilla':
                mrCerillaItems-=1
            
            if myName=='Mr.Tabaco':
                initialItems=mrTabacoItems
            elif myName=='Mr.Papel':
                initialItems=mrPapelItems
            elif myName=='Mr.Cerilla':
                initialItems=mrCerillaItems

            print(f'name: {myName} ------ items restantes:{initialItems}\n\n')


            # Smoking is done, wakeup the sleeping vendor.
            self.vendorSleep.release()
 

if __name__== "__main__":
    obj = cigaretteSmoker()