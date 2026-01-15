import random
from game import data

def datas(acc):
    acc_name = acc["name"]
    acc_desc = acc["description"]
    acc_country = acc["country"]
    return f"{acc_name},a {acc_desc},from {acc_country}."
def check(user_guess,a_followers,b_followers):
    if a_followers>b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"

score=0
should_continue=True
acc_b=random.choice(data)
while should_continue:
    acc_a=acc_b
    acc_b=random.choice(data)
    if acc_a==acc_b:
        acc_b = random.choice(data)

    print(datas(acc_a))
    print(datas(acc_b))

    guess=input("who as more followers 'A' or 'b' ").lower()
    print("\n"*20)
    a_follower_count=acc_a['follower_count']
    b_follower_count=acc_b['follower_count']

    is_correct= check(guess,a_follower_count,b_follower_count)


    if is_correct:
        score+=1
        print(f"you are right and your score is {score}.")
        acc_a=acc_b
    else:
        print(f"sorry you are wrong, your final score is{score}.")
        should_continue=False