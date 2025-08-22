def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_s, map_t = {}, {}
    for cs, ct in zip(s, t):
        if (cs in map_s and map_s[cs] != ct) or (ct in map_t and map_t[ct] != cs):
            return False
        map_s[cs] = ct
        map_t[ct] = cs
    return True

# Input
s = input().strip()
t = input().strip()

# Output
print("True" if isIsomorphic(s, t) else "False")
