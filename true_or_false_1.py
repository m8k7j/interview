"""
input = "dffdkfklsfjjfsfjfssjjfd"
result = d1f2d1k1f1k1l1s1f1j2s1f1j1f1s2j2f1d1
result_1 = d3f8k1l1s4j5
"""
input_raw = "aabbbccdde"

init_pos = 0
cur_pos = 0
length = len(input_raw)
result = []
count = 1

while cur_pos < length-1:

    if input_raw[cur_pos] == input_raw[cur_pos+1]:
        if cur_pos+1 == length-1:
            print input_raw[cur_pos]
            result.append((input_raw[cur_pos], count+1))
        cur_pos += 1
        count += 1
    else:
        if cur_pos+1 == length-1:
            result.append((input_raw[cur_pos+1], 1))
        result.append((input_raw[cur_pos], count))
        cur_pos += 1
        count = 1

print result
