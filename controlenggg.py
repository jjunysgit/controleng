import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control
import sympy
# 전달함수 G1과 G2 정의
K = 1 # 전달함수 미지수 선정
G1 = control.TransferFunction([K],[1])
G2 = control.TransferFunction([1],[1,1])

# 전달함수 G = G1 * G2 전향경로 / 직렬결합 
G = G1 * G2

#전달함수 출력
print(G)

#feedback
#G1에서 G2를 feedback 시킨 전달함수 G
G4 = control.feedback(G1 * G2)
print(G4)

s, K = sympy.symbols('s K') #미지수로 대입해서 표현 하지않은 전체 전달함수 출력
G = K / (s + 1 + K)
print(G)


#전체 전달함수 및 극점 찾기 완료---------------------------------------------------------------

# 전달 함수 정의
K = 1 # 전달함수 미지수 선정
num = [K]
den = [1,K+1]

system = signal.TransferFunction(num,den)



#극점과 영점 찾기
zeros, poles, _ = signal.tf2zpk(num, den)


#그래프 그리기 : 극점과 영점
plt.figure()
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='red', label='Poles')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='blue', label='Zeros')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.title('Poles and Zeros of H(s) = K / (s + 1 + K)')
plt.legend()
plt.grid()