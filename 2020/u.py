def split_at_char(s, n):
    l = s[0:n]
    r = s[n:]
    return (l, r)


def get_pos(arr, i, j, di, dj):
    if not (0 <= i + di < len(arr)):
        return '.'

    if not (0 <= j + dj < len(arr[i])):
        return '.'

    else:
        return arr[i+di][j+dj]

def get_visible(arr, i, j, di, dj):
    while (0 <= i + di < len(arr)) and (0 <= j + dj < len(arr[i])):
        i += di
        j += dj
        if arr[i][j] != '.':
            return arr[i][j]

    return '.'

# Assuming same size
def compare_2d_arrays(a1, a2):
    for i in range(0, len(a1)):
        for j in range(0, len(a1[0])):
            if a1[i][j] != a2[i][j]:
                return False

    return True
