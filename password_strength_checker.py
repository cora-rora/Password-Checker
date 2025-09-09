'''Ja'Cora Lagrant
This is a personal project a password strength checker'''

password = input('Please enter a password: ')

score = 0

if len(password) >=8:
    score +=1
if any (c.isupper() for c in password):
    score +=1
if any (c.islower() for c in password):
    score +=1
if any (c.isdigit() for c in password):
    score +=1
if any (c in "#@!%&*[]><?" for c in password):
    score +=1

if score <=2:
    strength = 'Weak'
elif score <=4:
    strength = 'Moderate'
else:
    strength = "Strong"

print(f"Password Strength: {strength}")
