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
            




max_salary = 0

for user in users:
    total_salary = 0
    friends = user.get('friends', [])
    for friend in friends:
        total_salary += friend['job']['salary']
    
    if total_salary > max_salary:
        max_salary = total_salary
        vip_user = user['name']
        print(vip_user)
        print(max_salary)


total_flights = 0
friends_with_cars = 0

for user in users:
    friends = user.get('friends', [])
    for friend in friends:
        if friend.get('cars'):
            friends_with_cars += 1
            total_flights += len(friend.get('flights', []))
avg_flights = round(total_flights / friends_with_cars, 5)
print(avg_flights) 




clean_users = 0  
while clean_users < len(users):
    need_remove = False
    friends = users[clean_users].get('friends', [])
    for friend in friends:
        flights = friend.get('flights', [])
        for flight in flights:
            if flight['country'] in countries:
                need_remove = True
                break
        if need_remove:
            break
    
    if need_remove:
        del users[clean_users]
    else:
        clean_users += 1
        print(clean_users)

    
    
            










