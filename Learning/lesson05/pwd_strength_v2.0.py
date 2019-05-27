'''作者：Egbert
    功能：判断密码强度
    版本：2.0
    2.0新增功能：循环的终止
    日期：2019-5-19
'''

def check_num_exist(password_str):
    '''
        判断字符串中是有数字
    '''
    has_num = False

    for c in password_str:
        if c.isnumeric():
            has_num = True
            break
    return has_num

def check_letter_exist(password_str):
    '''
        判断字符串中是有字母
    '''
    has_letter = False

    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter

def main():

    try_times = 3
    while try_times > 0:
        password = input('请输入密码：')

        #密码强度
        strength_level = 0

        #规则1：密码长度大于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度要求至少8位！')

        #规则2：包含数字
        if check_num_exist(password):
            strength_level += 1
        else:
            print('密码要求包含数字！')

        #规则3：包含字母
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母！')

        if strength_level == 3:
            print('恭喜！密码强度合格！')
            break
        else:

            print('密码强度不合格！')
            try_times -= 1
            print('\n')

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')

if __name__ == '__main__':
    main()