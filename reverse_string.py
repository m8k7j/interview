"""
string_s = 'dfsasfb'
result_s = 'bfsasfd'

"""
raw_str = 'dfsasfb'

def reverse_string(raw_str):

    """
    reverse string by li.pop()
    then ''+ str(li[i]) change to str
    """
    result = []
    result_str = ''
    list_str = list(raw_str)
    count = len(list_str)
    for i in range(count):
        result.append(list_str.pop())

    for i in result:
        result_str += str(i)
    return result_str


print reverse_string(raw_str)



