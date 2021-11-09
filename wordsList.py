
with open('words.txt') as f:
  clean = lambda x: x.replace('\n', '').upper()
  words = [clean(x) for x in f.readlines()]