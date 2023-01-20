from company import *

my_org = Org("my org", "software")

finance_team = Team("finance team 1", Team.TeamType.FINANCE,
    None, my_org)
dev_team = Team("crm team", Team.TeamType.DEV,
    "CRM", my_org)

finance_guy = NormalEmployee("Jack", 100, finance_team)
dev_manager = ManagerEmployee("Joe", 200, dev_team)
dev1 = NormalEmployee("Jim", 100, dev_team)

# finance_guy.get_salary()
# dev_manager.get_salary()
# dev1.get_salary()

# my_org.pay_all_employee_salary()

def pay_team(org, team_type):
    for team in org.teams:
        if team.type == team_type:
            for employee in team.members:
                employee.get_salary()

# pay_team(my_org, Team.TeamType.DEV)
my_org.pay_team(Team.TeamType.DEV)
