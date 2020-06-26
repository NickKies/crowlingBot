print("\n*************************************ex1*************************************")
# 함수란 ??
# def는 define의 앞글자를 따서 만든거다.
# 함수명은 자유롭게 기능에 맞춰 지어내면 된다.
# 함수 내에서는 tab 키로 한 칸 띄우고 입력해야한다.
# 함수 이름은 중복되면 안된다.

def print_test():
 print("test!!!!")




# 함수를 호출할 때는 함수 이름과 "()" 를 붙여서 사용하면 된다.
# 함수는 호출되기 전까지는 구동 하지 않는다.
print("함수 호출 전")
print_test()
print("함수 호출 후")





print("\n*************************************ex2*************************************")
# 매개변수(parameter)
def print_test2(x):
 print(x)

print_test2("test!!!")
print_test2("test2!!")






print("\n*************************************ex3*************************************")
# 함수를 사용하는 이유? 코드가 중복되는 것을 방지하기 위해서
# ex) 1과 2를 더한 결과, 3과 4를 더한 결과, 5와 6을 더한 결과를 출력하는 프로그램을 만드시오.
x=1
y=2
z=x+y
print(z)

x=3
y=4
z=x+y
print(z)

x=5
y=6
z=x+y
print(z)





print("\n*************************************ex4*************************************")
# 위 코드를 함수로 간소화시키면???
def print_test3(x,y):
 z=x+y
 print(z)

print_test3(1,2)
print_test3(3,4)
print_test3(5,6)


print("\n*************************************ex5*************************************")
# return ??
def print_test4(x,y):
 return x+y

z=print_test4(1,3)


print(z)



print("\n*************************************ex6*************************************")
# 지역변수 vs 전역 변수
# 함수 내에서 선언된 변수를 지역변수, 함수 밖에서 선언된 변수는 전역변수
# 지역 변수는 함수가 호출되었을 때에만 저장되어 있다. 즉, 함수를 빠져나오는 순간 저장된 값은 사라진다.

def ex6():
 ex6_x=2
 print("지역변수 : ", ex6_x)

ex6_x=1
ex6()
print("전역변수 :", ex6_x)


print("\n*************************************ex6_1*************************************")

def ex7():
 z=1
 print(z)
z=3
ex7()
print(z)