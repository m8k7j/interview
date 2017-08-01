#coding:utf-8

def sub_string(*string):
    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            break
        
    return count


if __name__ == '__main__':
    
    string = 'aaffffccddeeeee'
    index = 0
    length = 0
    result = [index, length]
    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            if count > length:         #最大子串
                length = count
                index = i - count + 1  #找到最大子串位置,如果最大子串不在末尾，i+1已经到了下一个子串
                count = 1
            else:  #count 置1，返回初始长度
                count = 1
    #如果最大子串发生在末尾，则i是在倒数第二个，因此需要+2
    else:
        if count > length:
            length = count
            index = i - count + 2
            
    print (index, length)
            