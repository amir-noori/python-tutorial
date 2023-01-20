from enum import Enum
from i18n.i18n import I18N
from i18n.i18n import Lang

i18n = I18N(Lang.EN)

class Org:

    def __init__(self, org_name, org_industry):
        self.name = org_name
        self.industry = org_industry
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def pay_all_employee_salary(self):
        for team in self.teams:
            for employee in team.members:
                # the follwing pring is boilerplate code
                # print(f"paying employee {employee.name} ${employee.salary}" +
                #     f" in team '{team.name}'")
                self.pay_employee(employee)

    def pay_employee(self, employee):
        print(i18n.message("payment", employee.name, employee.salary,
            employee.team.name))
        # print(f"paying employee {employee.name} ${employee.salary}" +
        #     f" in team '{employee.team.name}'")
        
    def pay_team(self, team_type):
        for team in self.teams:
            if team.type == team_type:
                for employee in team.members:
                    self.pay_employee(employee)

class Team:

    class TeamType(Enum):
        FINANCE = 1
        DEV = 2

    def __init__(self, team_name, team_type, team_project, team_org):
        self.name = team_name
        self.type = team_type
        self.project = team_project
        self.org = team_org
        self.members = []
        self.org.add_team(self)

    def add_member(self, member):
        self.members.append(member)

class Employee:

    def __init__(self, employee_name, employee_salary, employee_team):
        self.name = employee_name
        self.salary = employee_salary
        self.team = employee_team
        self.team.add_member(self)

    def get_salary(self):
        self.team.org.pay_employee(self)


class ManagerEmployee(Employee):
    pass

class NormalEmployee(Employee):
    pass




