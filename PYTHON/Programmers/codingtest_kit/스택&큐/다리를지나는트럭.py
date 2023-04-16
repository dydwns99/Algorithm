# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지

def solution(bridge_length, weight, truck_weights):
    # 다리에 있는 트럭의 무개가 weight 보다 작아야 됨
    # 일초당 다리 길이 단위로 +1을 감
    answer =0
    bridge = [0 for _ in range(bridge_length)]

    while bridge:
        answer+=1
        bridge.pop(0)

        if truck_weights:
            if sum(bridge)+truck_weights[0]<=weight:
                t=truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)

