size, k = map(int, input().split())
parcel = list(map(int, input().split()))

# Initial calculation of effort
min_val = min(parcel)
max_val = max(parcel)
k_val = parcel[k-1]
effort = min_val * k_val + min_val * max_val

# Swap elements: min_val with parcel[k-1], and max_val with min_val's original position
t1 = min_val
t2 = max_val
t3 = k_val

l1 = parcel.index(t1)  # index of min_val
l2 = parcel.index(t2)  # index of max_val

# Perform swaps
parcel[k-1], parcel[l1], parcel[l2] = t2, t3, t1

# Remove the max parcel (max_val)
parcel.remove(max(parcel))

# Sort a copy of parcel
lst1 = sorted(parcel)

# Remove elements from parcel where parcel[i] == lst1[i]
# Use a while loop carefully because of removing items during iteration
i = 0
while i < len(parcel):
    if parcel[i] == lst1[i]:
        parcel.pop(i)
        lst1.pop(i)
    else:
        i += 1

# Continue processing until parcel is empty
while parcel:
    i = len(parcel) - 1
    current_max = max(parcel)
    if parcel[i] == current_max:
        # do nothing (pass)
        pass
    else:
        if parcel[i] != min(parcel):
            # Add effort according to given formula
            effort += min(parcel) * parcel[i] + min(parcel) * max(parcel)
           
            # Swap current element with min and max positions
            t1 = min(parcel)
            t2 = max(parcel)
            t3 = parcel[i]

            l1 = parcel.index(t1)
            l2 = parcel.index(t2)

            parcel[i], parcel[l1], parcel[l2] = t2, t3, t1
        else:
            effort += min(parcel) * max(parcel)
            parcel.remove(max(parcel))

    # If parcel[i] was max, remove it here?
    if parcel and parcel[-1] == max(parcel):
        parcel.pop()

print(effort)
 
