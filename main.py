print("1.Food story    2.Your stroy")
print()
user = int(input("Enter your choice : "))
print()

if user == 1:
  food = input("Enter a type of food : ")
  print()
  jamie = input("Enter a girl's name : ")
  print()
  adj1 = input("Enter an adjective : ")
  print()
  bird = input("Enter a noun : ")
  print()
  verb1 = input("Enter a verb in the past tense : ")
  print()
  verb2 = input("Enter another verb in the past tense : ")
  print()
  verb3 = input("Enter a third verb in the past tense : ")
  print()
  noun1 = input("Enter a noun : ")
  print()

  print("Here is the story : ")
  print()

  story = "It was " + food + " day at school, and " + jamie + " was super " + adj1 + " for lunch. But when she went outside to eat, a " + bird + " stole her " + food + "! " + jamie + " chased the " + bird + " all over school. She " + verb1 + ", " + verb2 + ", and " + verb3 + " through the playground. Then she tripped on her " + noun1 + " and the " + bird + " escaped! Luckily, " + jamie + "'s friends were willing to share their " + food + " with her."

  print()
  print()
  print()
  print(story)
  print()

elif user == 2:
  name = input("Enter your name : ")
  print()
  gender = input("Himself or herself : ")
  print()
  aim = input("Enter your aim : ")
  print()
  ability = input("Enter your ability : ")
  print()
  school_name = input("Enter your school name : ")
  print()
  year = input("Enter a future year : ")
  print()

  print("Here is the story : ")
  print()

  story = "The user " + name + " is a well-known " + aim + " and extraordinary genius personality known by almost all of us all over the world due to his/her dedication towards " + ability + " . He/She quoted that success is a failure in progress and someone who has never failed cannot truly be a successful person. During childhood " + name + " suffered from continuous failures. " +  name + " got admision in " + school_name + " But, leading to the ways of success consistently, " + name + " proved " +     gender + " as a renowned gem in the ocean of " + ability + " and finally won the Nobel Prize for " + ability + " in " +    year + " . "
  print()
  print()
  print()
  print(story)
  print()

else:
  print("Invalid option selected")
  print()
