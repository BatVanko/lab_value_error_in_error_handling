class valueTooSmallException(Exception):
    pass


str_value = input()


class IncludingError(Exception):
    pass


for x in str_value:
    if x not in ['0', '1']:
        raise IncludingError("The input should contain only 0's and 1's ")
value = int(input())

if value < 10:
    raise valueTooSmallException(f'{value} is less than 10')
