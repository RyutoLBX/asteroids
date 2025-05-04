from constants import PRETTY_PRINT_COL_COUNT

def pretty_print(text="", char = '='):
  if text == "":
    print(f"{char * PRETTY_PRINT_COL_COUNT}")
    return
  
  equals_count = PRETTY_PRINT_COL_COUNT // 2 - 1
  if len(text) % 2 == 0:
    equals_count -= len(text) // 2
    formatted_text = f"{char * equals_count} {text} {char * (equals_count+1)}"
  else:
    equals_count -= len(text) // 2
    formatted_text = f"{char * equals_count} {text} {char * equals_count}"
  print(formatted_text)

def print_end_score(score):
  pretty_print("", " ")
  pretty_print(f"Score: {score}", " ") 
  pretty_print("", " ")
  pretty_print()