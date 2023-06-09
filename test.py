import streamlit as st
###
st.title(" 메카트로닉스공학과 제어공학 시험")
st.header(" LEE YONG JUN ")

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 전달 함수 정의
num = [20]
den = [1,16,68,80]

system = signal.TransferFunction(num,den)

#단위 계단 응답
t,y=signal.step(system)

#그래프 그리기: 단위 계단 응답
fig1 = plt.figure()
plt.plot(t,y)
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Step Response of H(s) = 20 / (s^3 + 16s^2 + 68s + 80)')
plt.grid()

st.pyplot(fig1)
#극점과 영점 찾기
zeros, poles, _ = signal.tf2zpk(num, den)

#그래프 그리기 : 극점과 영점
fig2 = plt.figure()
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='red', label='Poles')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='blue', label='Zeros')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.title('Poles and Zeros of H(s) = 20 / (s^3 + 16s^2 + 68s + 80)')
plt.legend()
plt.grid()

st.pyplot(fig2)

# 전달 함수 정의
num = [1,4]
den = [1,16,68,80]

system = signal.TransferFunction(num,den)

#단위 계단 응답
t,y=signal.step(system)

#그래프 그리기: 단위 계단 응답
fig3 = plt.figure()
plt.plot(t,y)
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Step Response of H(s) = (s + 4) * 20 / (s^3 + 16s^2 + 68s + 80)')
plt.grid()

st.pyplot(fig3)
#극점과 영점 찾기
zeros, poles, _ = signal.tf2zpk(num, den)

#그래프 그리기 : 극점과 영점
fig4 = plt.figure()
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='red', label='Poles')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='blue', label='Zeros')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.title('Poles and Zeros of H(s) = (s + 4) * 20 / (s^3 + 16s^2 + 68s + 80)')
plt.legend()
plt.grid()

st.pyplot(fig4)

# 전달 함수 정의
num = [1,5]
den = [1,16,68,80]

system = signal.TransferFunction(num,den)

#단위 계단 응답
t,y=signal.step(system)

#그래프 그리기: 단위 계단 응답
fig5 = plt.figure()
plt.plot(t,y)
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Step Response of H(s) = (s + 5) * 20 / (s^3 + 16s^2 + 68s + 80)')
plt.grid()

st.pyplot(fig5)
#극점과 영점 찾기
zeros, poles, _ = signal.tf2zpk(num, den)


#그래프 그리기 : 극점과 영점
fig6 = plt.figure()
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='red', label='Poles')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='blue', label='Zeros')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.title('Poles and Zeros of H(s) = (s + 5) * 20 / (s^3 + 16s^2 + 68s + 80)')
plt.legend()
plt.grid()

st.pyplot(fig6)
# 전달 함수 정의
num = [1,4.1]
den = [1,16,68,80]

system = signal.TransferFunction(num,den)

#단위 계단 응답
t,y=signal.step(system)

#그래프 그리기: 단위 계단 응답
fig7 = plt.figure()
plt.plot(t,y)
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Step Response of H(s) = (s + 4.1) * 20 / (s^3 + 16s^2 + 68s + 80)')
plt.grid()

st.pyplot(fig7)
#극점과 영점 찾기
zeros, poles, _ = signal.tf2zpk(num, den)

#그래프 그리기 : 극점과 영점
fig8 = plt.figure()
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='red', label='Poles')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='blue', label='Zeros')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.title('Poles and Zeros of H(s) = (s + 4.1) * 20 / (s^3 + 16s^2 + 68s + 80)')
plt.legend()
plt.grid()

st.pyplot(fig8)