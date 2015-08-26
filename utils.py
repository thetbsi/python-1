''' My Utilities. They are here.'''

import colors as c

def ask(question,color=c.green):
    print(color + question + c.reset)
    answer = input('--> ' + c.base3).lower().strip()
    print(c.reset)
    return answer
