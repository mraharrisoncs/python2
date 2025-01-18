def convertor(val, target):
  if target == "kg":
    result = val / 2.2
  elif target == "lb":
    result = val * 2.2
  else:
    print("invalid target")
    result = -999
  return result 

print(convertor(75,"e"))