import os
databaseName = input("Enter database name > ")
mySqlUsername = input("Enter mysql  username > ")
path = input("Enter path where you want to store backup database > ")
query = f"mysqldump -u {mySqlUsername} -p {databaseName} --single-transaction > {path}\\{databaseName}_backup.sql"

os.system(f'cmd /k cd C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin ^& {query}')



# C:\Users\acer\Desktop\sem3_mini_project\CFL_mini_project