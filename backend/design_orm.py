""" print(hash("123"))
print(hash("123"))
print(hash("1234"))
print(hash("1234")) """
# python自带的hash每次计算结果都不一样，所以一定用hashlib
import hashlib
""" sha256 = hashlib.sha256()
sha256.update("123".encode("utf-8"))
print(sha256.digest())
print(sha256.hexdigest())
print(hashlib.sha256("123".encode()).hexdigest())
print(hashlib.shake_256("123".encode("utf-8")).hexdigest(20)) """

class User:
    def __init__(self, id, nickname, pwd) -> None:
        self.id = id
        self.nickname = nickname
        self.hashed_pwd = hashlib.sha256(pwd.encode()).hexdigest()
        self.cur_month_fee = 440

u1 = User("1", "aaa", "123")
# print(u1.hashed_pwd + "\n" + str(u1.cur_month_fee))
u_dict = {}
u_dict["1"] = u1

class Service:
    def __init__(self, id, name, month_fee):
        self.id = id
        self.name = name
        self.month_fee = month_fee

s1 = Service("1", "追加服务1", 100)
s2 = Service("2", "追加服务2", 70)
# print(s2.name, s2.month_fee)
s_dict = {}
s_dict["1"] = s1; s_dict["2"] = s2

from datetime import datetime, date
# 学院派作法的关联表的主键应该是相关联的表的外键拼在一起做主键，但实际还是另搞一个id做主键的
class Subscribe:
    def __init__(self, id, user_id, service_id) -> None:
        self.id = id
        self.user_id = user_id
        self.service_id = service_id
        self.start_date = datetime.now()

us_dict = {}
us_dict["1"] = Subscribe("1", "1", "1")
us_dict["2"] = Subscribe("2", "1", "2")

def set_user_month_fee(user: User):
    for sub in us_dict.values():
        if sub.user_id == user.id:
            user.cur_month_fee += s_dict[sub.service_id].month_fee

set_user_month_fee(u1)
print(u1.cur_month_fee)
