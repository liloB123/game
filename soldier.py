def soldier_start_loc():
    soldier_matrix = []
    for i in range(4):
        for j in range(2):
            soldier_index = []
            soldier_index.append(i)
            soldier_index.append(j)
            soldier_matrix.extend([soldier_index])
    return soldier_matrix


