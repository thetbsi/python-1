"""A module of command-line helpers"""

import colors as c

def ask(question,color=c.yellow,lower=True,strip=True,end='\n> '):
    print(color + question + c.reset, end=end)
    answer = input(c.base3)
    if lower: answer = answer.lower()
    if strip: answer = answer.strip()
    print(c.reset, end="")
    return answer

if __name__ == '__name__':
    print(c.clear)
    answer = ask("What is your name?")
    print(answer)
    answer = ask("What is your name in color?",c.random_color())
    print(answer)
    answer = ask("What is your full name?",lower= False)
    print(answer)
    answer = ask("What is something with space around it:")
    print(answer)
    answer = ask("What is something with space around it again:",strip=False)
    print(answer)

