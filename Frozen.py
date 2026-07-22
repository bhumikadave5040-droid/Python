roles=frozenset(["admin","faculty","receptionist"])

for i in roles:
    if i=="admin":
        print(i)

roles.add("hacker")