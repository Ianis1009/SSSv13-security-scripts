
import os
files = ['a', 'f', 'g', 'l']
def get_permutations(vec):
    if len(vec) == 1:
        return [vec]
    perms = []
    for i in range(len(vec)):
        elem = vec[i]
        rest = vec[:i] + vec[i+1:]
        for p in get_permutations(rest):
            perms.append([elem] + p)
    return perms
perms = get_permutations(files)
for perm in perms:
    os.system('cat ' + ' '.join(perm) + ' > ' + ''.join(perm))