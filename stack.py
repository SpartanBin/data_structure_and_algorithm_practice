def determine_bracket_validity(input_str):
    stack = []
    legal_dict = {'[': ']', '(': ')', '{': '}'}
    illegal_list = [']', ')', '}']
    for item in input_str:
        if stack:
            if item in illegal_list and item != legal_dict[stack.pop()]:
                return False
            elif item in legal_dict.keys():
                stack.append(item)
        else:
            if item in illegal_list:
                return False
            elif item in legal_dict.keys():
                stack.append(item)
        print(stack)
    if stack:
        return False
    return True


if __name__ == '__main__':

    print(determine_bracket_validity('()()'))