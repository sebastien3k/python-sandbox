print("Hello World")

while True:
  user_input = input('> ')
  if user_input.lower() == '':
    pass
  elif user_input.lower() in ['q', 'quit']:
    break
  else:
    print("You've inputted: " + (user_input))
  # print(f"That's dope {user_input}, anything else?")