# 1. Coordinates → Tuples are used when position shouldn't change
location = (19.0760, 72.8777)  # Latitude & Longitude of Mumbai
print("Location (Lat, Long):", location)

# 2. Tuples as dictionary keys (lists can't be keys)
person_scores = {
    ("Tushar", "AI"): 95,
    ("Neha", "DS"): 90
}
print("Tushar's AI Score:", person_scores[("Tushar", "AI")])

# 3. List vs Tuple: Performance & Safety
cities_list = ["Pune", "Mumbai", "Delhi"]
cities_tuple = ("Pune", "Mumbai", "Delhi")

# Memory size
import sys
print("\nMemory used by list:", sys.getsizeof(cities_list))
print("Memory used by tuple:", sys.getsizeof(cities_tuple))

# Safety: tuple is immutable
try:
    cities_tuple[0] = "Nashik"  #  Will raise error
except TypeError as e:
    print("Error (as expected):", e)



# output:
# Location (Lat, Long): (19.076, 72.8777)
# Tushar's AI Score: 95

# Memory used by list: <number may vary>
# Memory used by tuple: <number may vary>
# Error (as expected): 'tuple' object does not support item assignment
