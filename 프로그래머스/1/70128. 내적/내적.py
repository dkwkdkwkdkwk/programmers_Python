def solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        mul = a[i]*b[i]
        answer += mul
    return answer