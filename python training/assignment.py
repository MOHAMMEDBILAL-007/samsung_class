emp_name = input("enter your name :")
emp_id = input("enter your employ id :")
basic_salary = float(input("enter you r monthly salary"))
special_allowance = float(input("enter your special allowance per month"))
bonus_perc = float(input("how many percent of bonus do you get :%"))
gross_m_salary = basic_salary + special_allowance
gross_a_salary = gross_m_salary*12
gross_a_b_salary = gross_a_salary + (gross_a_salary*(bonus_perc/100))

print(f"employee name:{emp_name} \nemployee id:{emp_id} \ngross monthly salary:{gross_m_salary} \ngross annual salary:{gross_a_b_salary}")