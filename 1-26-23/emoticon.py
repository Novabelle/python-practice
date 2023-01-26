import random

eyes_00 = "O O"
eyes_01 = "o O"

nose_00 = " |"
nose_01 = "-"

mouth_00 = " ~"
mouth_01 = "~~~"


eyes = [eyes_00, eyes_01]
noses = [nose_00, nose_01]
mouths = [mouth_00, mouth_01]

eyes_choice = random.choice(eyes)
nose_choice = random.choice(noses)
mouth_choice = random.choice(mouths)

print(eyes_choice)
print(nose_choice)
print(mouth_choice)

