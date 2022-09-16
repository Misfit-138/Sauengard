printable_quantum_book = {1: {1: "Quantum Missile",
                       2: "Sleep",
                       3: "Turn Undead"}
                   }

quantum_level = 1
new_dict = {}
key_lst = list(printable_quantum_book[q_level].keys())
value_list = list(printable_quantum_book[q_level].values())
res = {key_lst[i]: value_list[i] for i in range(len(key_lst))}
for key, value in res.items():
    print(f"{key}: {value}")
