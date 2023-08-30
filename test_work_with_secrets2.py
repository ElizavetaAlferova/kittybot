# test_work_with_secrets2.py

import os

auth_token = os.getenv('TOKEN')

# Значением переменной auth_token будет 123

account_sid = os.getenv('ACCOUNT_SID')
# А эту переменную мы не определили в пространстве переменных окружения
# Значением переменной account_sid будет None
tokens = [1, 2, None]
if all(tokens):
    print(True)
else:
    print(False)
print(type([1, 2, 3]))
