import time
T = int(input("상황(T): "))

t_list = [dict() for _ in range(T)]
i = 0
while i < T:
    t_list[i]['H'], t_list[i]['W'], t_list[i]['N'] = map(int, input(f"{i+1}번째 상황(H, W, N): ").split())
    if t_list[i]['H'] < 1 or t_list[i]['W'] > 99 or (1 <= t_list[i]['N'] <= t_list[i]['H']*t_list[i]['W']) == False:
        print("잘못된 값 입력.")
    else:
        i += 1
for n in range(T):
    rn = 0
    if t_list[n]['N']%t_list[n]['H'] != 0:
        rn = t_list[n]['N']//t_list[n]['H'] + 1
        rn += t_list[n]['N']%t_list[n]['H'] * 100
    else:
        rn = t_list[n]['N']//t_list[n]['H']
        rn += t_list[n]['H'] * 100
    print(int(rn))
