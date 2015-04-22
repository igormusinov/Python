#http://www.spoj.com/problems/ACPC10A/
#!/usr/bin/env python
list = []
raw = raw_input()

(a, b, c) = raw.split(" ")
while (a, b, c) != ("0", "0", "0"):
  a = int(a)
  b = int(b)
  c = int(c)
  if c - b == b - a:
    list.append("AP " + str(c + c - b))
  if c / b == b / a:
    list.append("GP " + str(c * c / b))
  raw = raw_input()
  (a, b, c) = raw.split(" ")
for i in range(0, len(list)):
  print list[i]
