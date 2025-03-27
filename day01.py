
# print
print('hello world!')
print("hello_world!")
print('''Hello World!''')
print("""Hello_World!""")

# sep 옵션 사용법
print('a', 'b', 'c')
print('a', 'b', 'c', sep=" ")
print('010', '1234', '5678', sep="-")
print('python', 'google.com', sep='@')

# end 옵션 사용법
print('hello', end=" ")
print('world', end=" ")
print()

# file 옵션 사용법
import sys
print('Study Python', file=sys.stdout)

# with open('test.txt', 'w') as test_file:
#     test_file.write("안녕하세요 \n")
#     test_file.write("반갑습니다 \n")
#     print('파이썬', file=test_file)

# format 사용법
# s: string(문자열) ,d: decimal(10진수 정수), f: float(10진수 실수)
print('%s %s' % ('one', 'two'))
# print('%d %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{} {}'.format(1, 'two'))
print('{1} {0}'.format(1, 'two'))
print('{1} {0}'.format(1, 'two'))

# 인터프리터 언어(python, javascript, php) vs 컴파일 언어(java, c) compile


#정렬 < : 왼쪽정렬, > : 오른쪽 정렬, ^ : 가운데 정렬
print('------')
print('%10s' % ('python'))
print('%-10s' % ('python'))
print('------')
print('{0:10}'.format('python'))
print('{0:>10}'.format('python'))
print('{0:<10}'.format('python'))
print('------')
print('{0:$>10}'.format('python'))
print('{0:^10}'.format('python'))
print('{0:$^10}'.format('python'))

#슬라이싱
print('%.5s' % ('python'))
print('{0:10.5}'.format('python'))
print('{0:10.5}'.format('python'))
