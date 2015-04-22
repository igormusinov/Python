#http://www.spoj.com/problems/TOANDFRO/
#!/usr/bin/env python
dialog = []
message = ""
raw = input()
while raw:
  text = raw_input()
  for i in range(raw):
      message = message + text[i::raw]
  dialog.append(message)
  raw = input()
for i in range(0, len(dialog)):
  print dialog[i]
