# Start with a dictionary
d = {"name": "Alice", "age": 25}

# 1. get()
print("GET:", d.get("name"))         # Alice
print("GET (missing):", d.get("city", "Not Found"))  # Not Found

# 2. keys()
print("KEYS:", d.keys())             # dict_keys(['name', 'age'])

# 3. values()
print("VALUES:", d.values())         # dict_values(['Alice', 25])

# 4. items()
print("ITEMS:", d.items())           # dict_items([('name', 'Alice'), ('age', 25)])

# 5. update()
d.update({"city": "Bhopal"})
print("AFTER UPDATE:", d)           # {'name': 'Alice', 'age': 25, 'city': 'Bhopal'}

# 6. pop()
d.pop("age")
print("AFTER POP 'age':", d)        # {'name': 'Alice', 'city': 'Bhopal'}

# 7. popitem()
last_item = d.popitem()
print("POPITEM:", last_item)        # ('city', 'Bhopal')
print("AFTER POPITEM:", d)          # {'name': 'Alice'}

# 8. clear()
d.clear()
print("AFTER CLEAR:", d)            # {}

# 9. copy()
d = {"x": 1, "y": 2}
copy_d = d.copy()
print("COPY:", copy_d)              # {'x': 1, 'y': 2}

# 10. setdefault()
copy_d.setdefault("z", 0)
print("AFTER SETDEFAULT:", copy_d)  # {'x': 1, 'y': 2, 'z': 0}