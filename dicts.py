emp = {"San": 50, "Dan": 45, "Tom": 35}
print("San's salary is", emp["San"])
emp["Will"] = 55
print("Will's salary is", emp["Will"])
emp["San"] = emp["San"] + 10
print("San's new salary is", emp["San"])
emp = {
    "San": {"Age": 30, "Exp": 10}, 
    "Dan": {"Age": 18, "Exp": 1}, 
    "Tom": {"Age": 25, "Exp": 5}
    }
print(emp.items())
print(emp.keys())
print(emp.values())