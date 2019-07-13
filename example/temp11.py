try :
    userData = int(input())
    result = int(10 / userData)
    print('result : {0}'.format(result))
except ZeroDivisionError as e:
    print('ZeroDivisionError 예외발생 {0}'.format(e))

except Exception as e :
    print('Exception 예외발생 : {0}'.format(e))
    
else :
    print('예외 발생X')

finally :
    print('무조건 실행')
