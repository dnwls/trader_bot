
daum = 89000
naver = 751000

res = daum * 100 + naver * 20

print("2-1. res ==> ", res)
print("2-2. res ==>  daum -5% : ", daum*0.05, "| naver -10% : ", naver*0.10, " | loss : ", daum*0.05 + naver*0.10)

fTem = 50
print("2-3. res ==> C = (F-32)/1.8 = ", (fTem-32)/1.8 )

p = "pizza"
print("2-4. res ==> ", p * 10)

mNaver = 1000000
print("2-5. res ==> ", mNaver * 0.7 * 0.7 * 0.7)

b1 = "정우진"
b2 = "19960212"
b3 = "960212-1******"
print("2-6. res ==> 이름:", b1, " 생년월일:", b2, " 주민등록번호:", b3)

s = "Daum KaKao"
s1 = s.split(' ')[0]
s2 = s.split(' ')[1]
print("2-7. res ==> ", s2 , s1)

a = "hello world"
a1 = a.split(' ')[0]
a1 = "hi"
a2 = a.split(' ')[1]
a = a1 + " " + a2
print("2-8. res ==> ", a)

x = "abcdef"
print("2-9. res ==> ", x[1:] + x[0:1])