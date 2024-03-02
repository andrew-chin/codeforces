# Source: https://usaco.guide/general/io
import sys 
from sys import stdout
 
a = input()
a = int(a)
 
for t in range(a):
  i, j = map(int, input().split())
 
  qa, qb, qc, qd = -1, -1, -1, -1
 
  print("? 1 1")
  stdout.flush()
  qa = input()
  qa = int(qa)
  
  blx, bly = qa + 1, 1
  if i < qa + 1:
    blx, bly = i, qa + 2 - i
  
  tlx, tly = 1, (qa + 1)
  if j < qa + 1:
    tlx, tly = qa + 2 - j, j
    
  print("? " + str(tlx) + " " + str(tly))
  stdout.flush()
 
  qb = input()
  qb = int(qb)
 
  print("? " + str(blx) + " " + str(bly))
  stdout.flush()
 
  qc = input()
  qc = int(qc)
  
  if qb % 2 == 0 and qc % 2 == 1:
    #b is correct
    print("! " + str(tlx + (qb // 2)) + " " + str(tly - (qb // 2)))
    stdout.flush()
 
  elif qb % 2 == 1 and qc % 2 == 0:
    print("! " + str(blx - (qc // 2)) + " " + str(bly + (qc // 2)))
    stdout.flush()
 
  else:
    print("? " + str(tlx + (qb // 2)) + " " + str(tly - (qb // 2)))
    fin = input()
    stdout.flush()
 
    if fin == '0':
      print("! " + str(tlx + (qb // 2)) + " " + str(tly - (qb // 2)))
      stdout.flush()
    else:
      print("! " + str(blx - (qc // 2)) + " " + str(bly + (qc // 2)))
      stdout.flush()
 
 