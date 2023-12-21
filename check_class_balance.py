import os
from collections import defaultdict

# Path to your dataset labels
label_path = './'  # Update this path

# Counters for each class
class_counts = defaultdict(int)
print("Class counts:", class_counts)

# Loop through label files and count class instances
for label_file in os.listdir(label_path):
    if label_file.endswith('.txt'):
        with open(os.path.join(label_path, label_file), 'r') as file:
            for line in file:
                class_id = int(line.split()[0])
                class_counts[class_id] += 1

print("Class counts:", class_counts)
