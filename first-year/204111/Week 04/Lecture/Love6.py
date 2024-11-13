def main():
  love6(6,6)
  love6(0,6)
  love6(1,0)
def love6(a:int,b:int) -> bool:
  if a == 6 or b == 6:
    return True
  elif a+b == 6:
    return True
  elif abs(a-b)==6:
    return True
  else:
    return False