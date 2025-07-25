def solve():
    n, k = map(int, input().split())
    parcels = list(map(int, input().split()))

    # Adjust k to be 0-indexed
    k -= 1

    # Create the target sorted order
    sorted_parcels = sorted(parcels)
    heaviest_parcel = sorted_parcels[-1]

    target_arrangement = [0] * n
    target_arrangement[k] = heaviest_parcel

    remaining_sorted = sorted_parcels[:-1] # Exclude the heaviest parcel
    
    current_remaining_index = 0
    for i in range(n):
        if i == k:
            continue
        target_arrangement[i] = remaining_sorted[current_remaining_index]
        current_remaining_index += 1

    # Map current positions to their sorted target positions
    # and also map values to their original indices
    pos_map = {parcels[i]: i for i in range(n)}
    
    total_effort = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] or parcels[i] == target_arrangement[i]:
            continue

        # Start a new cycle
        cycle_size = 0
        current_cycle_min_weight = float('inf')
        current_cycle_sum_weights = 0
        
        j = i
        while not visited[j]:
            visited[j] = True
            current_cycle_min_weight = min(current_cycle_min_weight, parcels[j])
            current_cycle_sum_weights += parcels[j]
            
            # Find the target position for the parcel at parcels[j]
            # This is slightly tricky because target_arrangement is not a simple sort.
            # We need to find the index of the parcel[j] in the target_arrangement.
            
            # We need to find the *current* index of the element that should be at this position
            # This is where the mapping from the original positions to the sorted position is required.

            # We need to find where parcels[j] should go in the final sorted arrangement.
            # It's not as simple as target_arrangement.index(parcels[j]) because of the k exception
            
            # Let's rebuild the pos_map for the target arrangement for easier lookup
            target_pos_map = {target_arrangement[x]: x for x in range(n)}
            
            j = target_pos_map[parcels[j]] # Find the position where parcels[j] should be
            cycle_size += 1

        # Now, calculate the minimum effort for this cycle
        current_cycle_sum_weights -= current_cycle_min_weight

        # Option 1: Use the local minimum within the cycle
        cost1 = current_cycle_sum_weights + current_cycle_min_weight * (cycle_size - 1)

        # Option 2: Use the overall minimum parcel as an intermediary
        overall_min_weight = sorted_parcels[0]
        cost2 = overall_min_weight * (cycle_size + 1) + current_cycle_sum_weights + 2 * current_cycle_min_weight

        total_effort += min(cost1, cost2)

    print(total_effort)

# Example Usage:
# solve()
