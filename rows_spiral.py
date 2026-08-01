s = "TSEA(yh)wopeeie*akesr*nnnbanaocrypti"
N = 6

m = [list(s[i*N:(i+1)*N]) for i in range(N)]

def spiral_read(mat):
    res = []
    top, left = 0, 0
    bottom, right = len(mat)-1, len(mat[0])-1

    while top <= bottom and left <= right:
        for j in range(left, right+1):
            res.append(mat[top][j])
        top += 1

        for i in range(top, bottom+1):
            res.append(mat[i][right])
        right -= 1

        if top <= bottom:
            for j in range(right, left-1, -1):
                res.append(mat[bottom][j])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top-1, -1):
                res.append(mat[i][left])
            left += 1

    return "".join(res)

print("rows -> spiral:")
print(spiral_read(m))

def spiral_fill(text, n):
    mat = [[""]*n for _ in range(n)]
    top, left = 0, 0
    bottom, right = n-1, n-1
    idx = 0

    while top <= bottom and left <= right:
        for j in range(left, right+1):
            mat[top][j] = text[idx]; idx += 1
        top += 1

        for i in range(top, bottom+1):
            mat[i][right] = text[idx]; idx += 1
        right -= 1

        if top <= bottom:
            for j in range(right, left-1, -1):
                mat[bottom][j] = text[idx]; idx += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top-1, -1):
                mat[i][left] = text[idx]; idx += 1
            left += 1

    return mat

m2 = spiral_fill(s, N)

print("\nspiral -> rows:")
for row in m2:
    print("".join(row))
print("".join("".join(r) for r in m2))