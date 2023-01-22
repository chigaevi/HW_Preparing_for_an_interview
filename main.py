class Stack_list():
    def __init__(self, list_=[]):
        self.list_ = list_

    def is_empty(self):
        if len(self.list_) == 0:
            return True
        else:
            return False

    def push(self, new_el):
        # self.list_ += new_el
        self.list_.append(new_el)

    def pop(self):
        return self.list_.pop()

    def peek(self):
        return self.list_[-1]

    def size(self):
        return len(self.list_)

class Stack_str():
    def __init__(self, str_=''):
        self.str_ = str_

    def is_empty(self):
        if len(self.str_) == 0:
            return True
        else:
            return False

    def push(self, new_el):
        self.str_ += new_el

    def pop(self):
        last_el = self.str_[-1]
        self.str_ = self.str_[0:-1]
        return last_el

    def peek(self):
        return self.str_[-1]

    def size(self):
        return len(self.str_)

def equilib(raw_str):
    closed_bracket = [')','}',']']
    if len(raw_str)%2 != 0 or raw_str[0] in closed_bracket:
        return print('Несбалансированно')
    end_ind = int(len(raw_str)/2)
    for i_ in range(end_ind):
        i = 0
        for ind, el in enumerate(raw_str):
            if i == int(len(raw_str)/2):
                break
            if el == '(' and raw_str[ind+1] == ')':
                raw_str = raw_str[:ind] + raw_str[ind+2:]
                break
            elif el == '[' and raw_str[ind+1] == ']':
                raw_str = raw_str[:ind] + raw_str[ind+2:]
                break
            elif el == '{' and raw_str[ind+1] == '}':
                raw_str = raw_str[:ind] + raw_str[ind+2:]
                break
            i += 1
    if int(len(raw_str)) > 0:
        return print('Несбалансированно')
    else:
        return print('Cбалансированно')

if __name__ == '__main__':
    my_stack = Stack_str('[[{()}]][][][]{}{}')
    equilib(my_stack.str_)

