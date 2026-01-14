def solution(num_list):
    odd = ""
    even = ""
    
    for n in num_list:
        if n % 2 == 1:
            odd += str(n)
        else:
            even += str(n)
    answer = int(odd) + int(even)
    
    return answer