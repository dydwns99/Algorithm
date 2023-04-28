# 장르별 가장 많이 들은 노래 2개를 골라 수록

def solution(genres, plays):
    # 장르 별로 리스트에 담고(고유번호와 함께)
    album={}
    name = set(genres)
    for n in name:
        album[n]=[]
    for idx, gr in enumerate(genres):
        album[gr].append([idx,plays[idx]])

    for gr in genres:
        album[gr].sort(key=lambda x : x[1], reverse=True)

    # print(album)
    # 장르 가장 많이 듣는 순서 부터
    total=[]
    for n in name:
        sum=0
        for i in album[n]:
            # (1,600) (4,2500)
            sum+=i[1]
        total.append([n,sum])
    # 노래 2개씩 수록함
    total.sort(key = lambda x : x[1], reverse=True)
    # print("total ",total)
    res=[]
    for t in total:
        if len(album[t[0]])>=2:
            res.append(album[t[0]][0][0])
            res.append(album[t[0]][1][0])
        elif len(album[t[0]])==1:
            res.append(album[t[0]][0][0])
    # print("res ",res)

    return res
print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 500, 800, 2500]))