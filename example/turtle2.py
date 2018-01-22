from turtle import *

degree = 1              #角度の初期値
distance = 50           #距離の初期値

for iLoop in range(40): #40回ループ
    forward(distance)   #前進して線を引く
    right(degree)       #右側へ角度移動
    degree += 2         #角度を2足す
    distance -= 1       #距離を1引く

input()                 #入力受付にして動作を停止