def solution(id_pw, db):
    for i,p in db:
        if id_pw[0] == i:
            if id_pw[1] == p:
                return "login"
            else:
                return "wrong pw"
                        
    return "fail"