'''
    作者：Egbert
    功能：BMR计算器
    版本：4.0
    日期：2019-4-24
    新增功能：用户可以用空格分割一次性输入性别、体重、身高、年龄
    4.0新增功能：异常情况处理（try-except）
'''

#
def main():
    #主函数
    print('请输入以下信息，用空格分割')
    input_str = input('性别 体重（kg) 身高（cm） 年龄：')
    #找空格位置：input_str.find(' '),
    #以,分割：input_str.split(',')
    str_list = input_str.split(' ')

    try:
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])

        if gender == '男':
            # 男性BMR
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            # 女性BMR
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('您的性别：{0}，体重：{1}kg，身高：{2}cm，年龄：{3}岁'.format(gender, weight, height, age))
            print('您的基础代谢率:{}大卡'.format(bmr))
        else:
            print('暂不支持该性别BMR计算！')

    except ValueError:
        print('请输入正确的信息！')
        except:  # 包含所有的错误，但暂时无法找到原因
        print('程序异常！')



    print('**************************************************')  #我是分隔符
    y_or_n = input('是否退出程序（y/n）？')

if __name__ == '__main__':
    main()