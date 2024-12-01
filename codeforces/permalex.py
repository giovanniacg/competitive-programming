# from itertools import permutations

# while True:
#     s = str(input()).strip()
#     if s == "#":
#         exit()
#     for index, perm in enumerate(sorted(set(permutations(s))), start=1):
#         perm_str = "".join(perm)
#         if perm_str == s:
#             print(f"{index:10}")
#             break


def perm(s):

    if len(s) == 1:
        return 1

    s_first = sorted(s)

    if DEBUG:
        print(f"target: {s}")

    occurrences = []
    last = s_first[-1]
    current_idx = -1
    count = 0
    while True:
        if s_first == s:
            return count + 1

        for i in range(len(s_first) + current_idx, -1, -1):
            if DEBUG:
                print(f"analysis: {s_first[i]} < {last}")
            if s_first[i] < last:
                tmp = []
                str_tmp = []
                str_tmp = s_first.copy()

                for _ in range(abs(current_idx)):
                    tmp.append(str_tmp.pop())

                for j in range(abs(current_idx)):
                    str_tmp.insert(i + j, tmp.pop())

                if DEBUG:
                    print(f"s_first: {s_first}")
                    print(f"str_tmp: {str_tmp}")

                if str_tmp not in occurrences:
                    occurrences.append(str_tmp)
                    count += 1
                    s_first = str_tmp
                    last = s_first[-1]
                    current_idx = -1
                else:
                    current_idx -= 1
                    if current_idx + len(s_first) == 0:
                        last = s_first[0]
                    else:
                        last = s_first[current_idx]

                break
        else:
            if DEBUG:
                print(f"current_idx: {current_idx}")
            current_idx -= 1
            last = s_first[current_idx]


DEBUG = False

while True:
    s = list(input().strip())
    if s == ["#"]:
        break
    print(perm(s))
