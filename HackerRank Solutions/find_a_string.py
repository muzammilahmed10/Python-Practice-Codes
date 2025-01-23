def count_substring(string, sub_string):
    x = len(string)
    y = len(sub_string)
    count = 0
    for i in range(0, x):
        if sub_string == string[ i : i+y ]:
            count += 1
    return count
string = input()
sub_string = input()
count = count_substring(string,sub_string)
print(count)