import datetime as dt

class Member:
    free_days = 365

    def __init__(self, username, fullname):
        self.date_joined = dt.date.today()

        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)
        


    @classmethod
    def setfreedays(cls, days):
        cls.free_days = days

    

w = Member("wblomger","Wblomger Blomegren")

print(w.date_joined)
print(w.free_expires)

w.setfreedays(30)

print(w.free_expires_m)


