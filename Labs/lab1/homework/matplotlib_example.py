from matplotlib import pyplot

#data cua Matplotlib dung type List

# 1. Prepare data
machine_counts = [18, 4, 2]

# 2. Prepare labels
machine_names = ["PC", "Mac", "Linux"]

# 3. Draw pie
pyplot.pie(machine_counts, labels = machine_names, autopct = "%.2f%%", shadow = True, explode = [0, 0.2, -1])
pyplot.title("PC vs MAC vs Linux usage")
pyplot.axis("equal")

# 4. Show
pyplot.show()