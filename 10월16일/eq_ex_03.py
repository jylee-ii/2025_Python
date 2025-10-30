class User:
    def __init__(self, username, email):
        self.__username=username
        self.__email=email

    def __eq__(self, other):
        return self.__email==other.__email
    
u1=User("jane","jane@korea.korea")
u2=User("jennie","jane@korea.korea")

if u1==u2:
    print("중복된 이메일 입니다.")
