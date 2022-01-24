from dataset import users, countries
from pprint import pprint



user_wrong_password = []

for user in users:
    if user['password'].isdigit():
        user_wrong_password.append({'name': user['name'], 'mail': user['mail']})
       


girls_drivers = []

for friends in user.get('friends'):
    if friends['sex'] == 'F' and friends.get('cars'):
        girls_drivers.append({friends['name']})
       

best_occupation = []
max_salary = 0

for user in users:
    friends = user.get('friends', [])
    for friend in friends:
        job = friend['job']
        salary = job['salary']
        if salary > max_salary:
            max_salary = job['salary']
            best_occupation.append({'occupation': job['occupation'], 'salary': job['salary']})
            print(best_occupation)
