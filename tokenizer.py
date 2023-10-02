import re

tokens = {
  b"NUMBER": r"\d+(\.\d)"




def tokenize(characters):
  result = []
  
  t= None
  for token, regex in tokens.items():
    pattern =re.compile(regex)
    match = pattern.match(characters, pos)
    if match:
      t=(token, match.group(0))
      pos = match.end()
      break

  if t:
    result.append(t)
  else:
    raise Exception
      



