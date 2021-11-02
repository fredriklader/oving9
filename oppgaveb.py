

class Flervalgsspørsmål:
    #Konstruktør
    def __init__(self, question, answer, correct):
        self.question = question
        self.answer = answer
        self.correct = correct

    def __str__(self):
        print(f"Spørsmålet er: \n{self.question}")
        antall = 0
        print("Svaralternativene er:")
        for i in self.answer:
            antall += 1
            print(f"{antall}: {i}")

    def check_answer(self, Useranswer):
        if Useranswer == self.correct:
            print("Du hadde riktig!")
        else:
            print("Du hadde feil!")



question = "Hvor mange meter over havet er Preikestolen?"
answer = ["705 meter", "420 meter", "690 meter", "604 meter"]
correct = "4"

the_question = Flervalgsspørsmål(question, answer, correct)
the_question.__str__()
Useranswer = input("Skriv inn tallet som representerer svaret: ")
the_question.check_answer(Useranswer)
