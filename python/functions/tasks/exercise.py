
import module as md

print("Task 1:")
names = ["Mayowa", "chizoba", "Chigozie"]
print(names[0].split(sep= ("a" or "o")))
print(md.task_one("Tade Gold Wealth") +"\n")

print("Task 2:")
task2 = ["first name", "last_name", "date of birth"]
print(md.task_two(task2))
print("\n")

print("Task 3:")
print(md.last_letter_check(names[1]))
print(md.task_three(names))
print("\n")

print("Task 4:")
entry = ["Wofai", "Na(me", "Zainab", "A4atullah", "Women42k", "Norm1al"]
print(md.task_four(entry))
print("\n")

print("Task 5:")
cust_names = [10, "mayowa", "zainab", 4, 5]
yielded = md.yield_bad_names(cust_names)
for i in yielded:
    print(i)