#!/usr/bin/env python
# coding=utf-8


"""
给一个字符串，如何写出它可能组成的所有ip
str to ip

1122334455
112.233.44.55

"""
init_str = "1122112211"
length = len(init_str)
init = list(init_str)
ip_a = 0
ip_b = 0
ip_c = 0
ip_d = 0
for i in range(1,4):
    if i == 1:
        ip_a = int(init[0])
    elif i == 2:
        ip_a = int(init[0])*10+int(init[1])
    elif i == 3:
        ip = int(init[0])*100+int(init[1])*10+int(init[2])
        if ip > 256:
            break
    for j in range(1,4):
        if j == 1:
            ip_b = int(init[i])
        elif j == 2:
            ip_b = int(init[i])*10+int(init[i+1])
        elif j == 3:
            ip_b = int(init[i])*100+int(init[i+1])*10+int(init[i+2])
            if ip_b > 256:
                break
        for k in range(1,4):
            if k == 1:
                ip_c = int(init[i+j])
            elif k == 2:
                ip_c = int(init[i+j])*10+int(init[i+j+1])
            elif k == 3:
                ip_c = int(init[i+j])*100+int(init[i+j+1])*10+int(init[i+j+2])
                if ip_c > 256:
                    break
            l = length-i-j-k
            if l == 1:
                ip_d = int(init[i+j+k])
                print (ip_a, ip_b, ip_c, ip_d)
            elif l == 2:
                ip_d = int(init[i+j+k])*10+int(init[i+j+k+1])
                print (ip_a, ip_b, ip_c, ip_d)
            elif l == 3:
                ip_d = int(init[i+j+k])*100+int(init[i+j+k+1])*10+int(init[i+j+k+2])
                if ip_c > 256:
                    break
                else:
                    ip_d = int(init[i+j+k])*10+int(init[i+j+k+1])
            else:
                break





