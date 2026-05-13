# Error Handling in Python
while True:
    try:
        age = int(input('What is your age? '))
        #print(age)
        10/age
        # raise ValueError('hey cut it out')
    except ValueError:
        print('please enter a number')
        # continue
    except ZeroDivisionError:
        print('please enter an age higher than zero')
        # break
    else:
        print('thank you!')
        break
    finally:
        print('ok, i am finally done')
    # print('can you hear me?')
    

# def sum(num1, num2):
#     try:
#         return num1/num2
#     except (TypeError, ZeroDivisionError) as err:
#         #print(f'please enter numbers {err}')
#         print(err)
#         print('oops')

# print(sum(1,0))

