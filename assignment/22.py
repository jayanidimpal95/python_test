to_exclude = {0, 2,4,6}
vector= [12,24,35,70,88,120,155]
vector2 = [element for i, element in enumerate(vector) if i not in to_exclude]
print vector2
