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
        #salary = job['salary']
        if job['salary'] > max_salary:
            max_salary = job['salary']
            best_occupation.append({'occupation': job['occupation'], 'salary': job['salary']})
           # print({'occupation': job['occupation'], 'salary': job['salary']})
            #print(*best_occupation)
            

#vip_user = []


#for user in users:
  #  total = 0
   # friends = user.get('friends', [])
   # for friend in friends:
    #    total += friend['job']['salary']
     #   print(total)
      #  if vip_user == total:
       #     print(total)



max_friends_total_salary = 0

for user in users:
    friends_total_salary = 0
    friends = user.get('friends', [])
    for friend in friends:
        friends_total_salary += friend['job']['salary']
    
    if friends_total_salary > max_friends_total_salary:
        max_friends_total_salary = friends_total_salary
        vip_user = user['name']
        print(vip_user)
        print(max_friends_total_salary)
            










