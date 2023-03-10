L, S = [int(x) for x in input().split()]

#O(LS)
def solve(L, S):
  dptable = [[0]*(S+1) for i in range(L+1)] #dptable을 0으로 초기화
  #dptable 초기값 설정
  for i in range(1, L+1):
    dptable[i][1] = 1 #몇의 자리수든지 1을 만들 수 있는 경우는 제일 큰 자리수에 1이 오는 경우 하나 뿐
    for j in range(1, S+1):
      if j >= 10: #1의 자리수로 만들 수 있는 값을 테이블의 초기값으로 주기위해
        break
      dptable[1][j] = 1 #1의 자리수로 만들 수 있는 값은 1개뿐임.(j가 10 이전에)
  
  #dptable 동작
  for i in range(2, L+1):
    for j in range(2, S+1):
      if j > (i*9): # 자리수가 i개 일때 만들수 있는 자리수의 합은 최대 i*9이므로 그 이후의 값은 0으로 설정. 예를들어 자리수가 3인 값으로 만들수 있는 값은 27이 최대임.
        dptable[i][j] = 0
      elif j > 10: # j가 십의자리를 넘어갈 경우 
        dptable[i][j] = dptable[i][j-1] + dptable[i-1][j] - dptable[i-1][j-10]
      else:
        dptable[i][j] = dptable[i][j-1] + dptable[i-1][j]
  
  # for i in range(L+1): #dptable에 들어있는 값 확인코드
  #   print(dptable[i])

  return dptable[L][S]

# solve(L, S)
print(solve(L, S)%2147483647)

'''
위 코드는 dp를 활용하여 L개의 자리 값의 합이 S가 되는 자연수의 개수를 구현한 것이다.
우선은 dptable의 초기값으로 L이 1일 때와 S가 1일 때는 1개의 경우뿐만 존재하므로 dptable[1][S], dptable[L][1]에 1을 넣어주었다.
예를들어 L이 4, S가 1인 경우는 1000인 경우 1개,
L이 1 S가 6인 경우는 6인 경우 1개이다.
하지만 L이 1, S가 10 이상일 경우는 불가능 하므로 0인 상태인 코드를 작성하여 dptable을 생성하였다.

dptable을 그림으로 확인해보면 (L이 4, S가 36일때)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 54, 61, 66, 69, 70, 69, 66, 61, 54, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 4, 10, 20, 35, 56, 84, 120, 165, 219, 279, 342, 405, 465, 519, 564, 597, 615, 615, 597, 564, 519, 465, 405, 342, 279, 219, 165, 120, 84, 56, 35, 20, 10, 4, 1]
이다.
j가 10을 넘지 않는 경우는 dptable[i][j]의 값은 dptable[i][j-1]과 dptable[i-1][j]의 합인 것을 볼 수 있다.
j가 10을 넘어갈 경우 dptable[i][j]의 값은 dptable[i][j-1]과 dptable[i-1][j]의 합에서 어떠한 숫자를 빼는 것을 볼 수 있다.
예를들어 i가 2일때 dptable[2][11]은 dptable[2][10] + dptable[1][11]의 값에서 -1을 하였고
i가 3일때 dptable[3][12]는 dptable[3][11] + dptable[2][12]에서 -2한 것을 볼 수 있고, dptable[3][13]는 dptable[3][12] + dptable[2][13]에서 -3 한 것을 볼 수 있다.
여기서 -2와 -3은 dptable[2][2]와 dptable[2][3]에서 각각 볼 수 있다. 따라서 점화식을 작성해보면 dptable[i][j] = dptable[i][j-1] + dptable[i-1][j] - dptable[i-1][j-10]이 된다.
위의 점화식을 i가 4일때도 성립한다. 한가지 예시로 dptable[4][30]의 값은 84인데 이 값은 dptable[4][29] + dptable[3][30] - dptable[3][20]으로 120 + 0 - 36 = 84 인 것을 확인할 수 있다.

위의 알고리즘의 수행시간은 dptable은 입력받는 두 값 L, S의 크기에 의해 결정되고 이중 for문을 돌아가며 수행하므로 O(LS)이다.
'''