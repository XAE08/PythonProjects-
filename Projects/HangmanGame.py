import random
class Solution:
    def __init__(self) -> None:
        self.words=['apple','banana','mango','pears','pineapple','grapes','plum','orange','avocado','coconut','strawberry','cantaloupe','blueberry','lychee','cherry']
        self.min_guess=0
        self.word=''
        self.placeholder=[]

    def initialSetup(self)->None:
        self.word=random.choice(self.words)
        self.placeholder=['_ ' for _ in range(len(self.word))]
        self.min_guess=len(self.word)+2
        print(''.join(self.placeholder))
    
    def guessWork(self)->None:
        while self.min_guess>0:
            s=input("Guess the alphabet.HINT:It's a fruit name\n")
            indices=self.findLetter(s)
            if indices:
                for i in indices:
                    self.placeholder[i]=s
                print(''.join(self.placeholder))    
                if (''.join(self.placeholder))==self.word:
                    print("You Won")
                    break
            else:
                print("Wrong Guess.Try Again!")
            self.min_guess-=1
        if (''.join(self.placeholder).replace("_","")!=self.word):
            print(f"Wrong Guess!Better Luck next time.The fruit was {self.word}") 



    def findLetter(self,letter)->list:
        indices=[]
        for i in range(len(self.word)):
            if self.word[i]==letter:
                indices.append(i)
        return indices

if __name__=="__main__":
    s=Solution()
    s.initialSetup()
    s.guessWork()





























