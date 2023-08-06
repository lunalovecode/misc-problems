if __name__ == '__main__':
    s = input()
    alpha_num, alpha, num, lowercase, uppercase = False, False, False, False, False
    for c in s:
        if c.isalnum():
            alpha_num = True
            if c.isalpha():
                alpha = True
                if c.islower():
                    lowercase = True
                else:
                    uppercase = True
            else:
                num = True
    print(alpha_num)
    print(alpha)
    print(num)
    print(lowercase)
    print(uppercase)