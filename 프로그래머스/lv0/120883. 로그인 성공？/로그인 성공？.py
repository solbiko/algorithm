def solution(id_pw, db):
    for x in db:
        if x[0]==id_pw[0]:
            if x[1]==id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"    
