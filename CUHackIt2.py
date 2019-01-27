class CUHackIt2(object):
    pass

import random
import re

Q = ["What is 2+2?","Who was the first President of the United States?", "Who was the Roman Emperor from 275-276?", "Which bird is the national bird of Angola?"]
A = ["4", "George Washington", "Tacitus", "Red-crested turaco"]

while True:
  index = random.randint(0, len(Q)-1)
  print(Q[index])
  speech = input()
  if re.match(speech, "end practice", re.IGNORECASE): break
  while True:
    if re.match(speech, A[index], re.IGNORECASE): break
    elif re.match(speech, "repeat question", re.IGNORECASE): 
      print(Q[index])
      speech = input()
    else: 
      print(A[index])
      break
  while True:
    speech = input()
    if re.match(speech, "repeat answer", re.IGNORECASE): 
      print(A[index])
    else: 
      break




