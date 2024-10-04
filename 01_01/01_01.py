while True:
  try:
    wert = int(input("Bitte geben Sie eine Zahl zwischen 0 und 9 ein: "))
    if wert > 0 and wert <= 9:
      print ("passt!!")
      break
    else:
      print("Das ist keine Zahl zwischen 0 und 9!!")
  except ValueError:
    print("Zu dumm eine Zahl einzugeben??")

  
