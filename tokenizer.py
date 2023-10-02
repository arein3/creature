import re

tokens = {
  b"NUMBER": r"\d+(\.\d*)?",
  b"PLUS": r"\+",
  b"MINUS": r"-",
  b"MULTIPLY": r"\*",
  b"DIVIDE": r"/",
  b"LPAREN": r"\(",
  b"RPAREN": r"\)",
  b"LBRACKET": r"\[",
  b"RBRACKET": r"\]",
  b"LBRACE": r"\{",
  b"RBRACE": r"\}",
  b"NEQ": r"\!\=",
  b"NOT": r"\!",
  b"LE": r"\<\=",
  b"GE": r"\>\=",
  b"LT": r"\<",
  b"GT": r"\>",
  b"EQ": r"\=\=",
  b"ASSIGN": r"\=",
  









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
    raise Exception(f"token not found?")
    
      
def test_individual_tokens:
#fix how
  b"NUMBER": r"\d+(\.\d*)?",
  b"PLUS": r"\+",
  b"MINUS": r"-",
  b"MULTIPLY": r"\*",
  b"DIVIDE": r"/",
  b"LPAREN": r"\(",
  b"RPAREN": r"\)",
  b"LBRACKET": r"\[",
  b"RBRACKET": r"\]",
  b"LBRACE": r"\{",
  b"RBRACE": r"\}",
  b"NEQ": r"\!\=",
  b"NOT": r"\!",
  b"LE": r"\<\=",
  b"GE": r"\>\=",
  b"LT": r"\<",
  b"GT": r"\>",
  b"EQ": r"\=\=",
  b"ASSIGN": r"\=",


if __name__ == "__main__":
  test_individual_tokens()
  test_whitespace()
  test_multiple_tokens()
