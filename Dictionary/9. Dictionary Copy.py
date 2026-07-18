import copy

d1 = {
    "a": [1, 2],
    "b": {
        "x": 10
    }
}

d2 = d1.copy()
d3 = copy.deepcopy(d1)

d2["a"].append(3)
d2["b"]["x"] = 20

d3["a"].append(4)
d3["b"]["x"] = 30

print("d1 =", d1)
print("d2 =", d2)
print("d3 =", d3)