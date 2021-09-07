from Application import salary
from Application.db import people
import datetime

if __name__ == '__main__':
    dt_now = datetime.datetime.today()
    print(dt_now)
    salary.calculate_salary()
    people.get_employees()