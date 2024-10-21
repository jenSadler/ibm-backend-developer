from randomuser import RandomUser
import pandas as pd

def getUsers():
    users =[]

    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})

    return pd.DataFrame(users) 

df1 = pd.DataFrame(getUsers())

print(df1)