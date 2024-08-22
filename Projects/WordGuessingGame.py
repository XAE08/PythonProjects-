import random


class WordGame:
    def __init__(self):
        self.words=['python','java','go','rust','ruby','javascript','c','R','scala','typescript','dart','perl','lua']
        self.min_turn=12
        self.placeholder=''
        self.word=''
        self.failed=0

    def initialStep(self)->None:
        self.word=random.choice(self.words)
        name=input("Enter your name!\n")
        print(f"Hi {name}! Let's get started")
        self.placeholder=['_ ' for _ in range(len(self.word))]
        print("Your turn to guess")
        print(f'Hint:{"".join(self.placeholder)}')

    def guessWork(self)->int:
        while self.min_turn>0:
            print("Ready!!Guess the letter...")
            s=input()
            indices= self.findletter(s,self.word)
            if indices:
                for i in indices:
                    self.placeholder[i]=s
                print(''.join(self.placeholder))
                if (''.join(self.placeholder)).replace("_",'')==self.word:
                    print("You won!Well done!")
                    break
            else:
                self.failed+=1
                print("Wrong Guess.Try Again!")
            
                
            self.min_turn-=1
        if ("".join(self.placeholder)).replace("_","")!=self.word and self.min_turn==0 and self.failed!=0:
            print(f"Better Luck next time! The word was {self.word}")

    
    

    def findletter(self,letter:str,word:str)->list:
        indices=[]
        for i in range(len(word)):
            if letter==word[i]:
                indices.append(i)
        return indices
    
if __name__=="__main__":
    c=WordGame()
    c.initialStep()
    c.guessWork()
