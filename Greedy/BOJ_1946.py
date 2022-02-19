T = int(input()) # test case 입력
ans = [] #정답 리스트

for i in range(T):
    case = [] # 성적을 담을 리스트
    N = int(input())
    for j in range(N):
        x, y = map(int, input().split()) # case를 2차원리스트로 만들어서 성적을 저장
        case.append([x,y])
    score = sorted(case, key = lambda x : x[0])  # 서류심사 성적을 기준으로 오르차순 정렬
    best = score[0][1] #비교 기준이 될 사람
    cnt = 1 # 고용할 수 있는 사람 수. 첫번째 사람(best)는 서류심사 성적이 1등이기 때문에 일단 고용.
    for j in range(1,N):
        if score[j][1] < best: #for문을 돌면서 해당 순번의 면접시험 순위가 best보다 높으면 best가 된다.
            best = score[j][1]
            cnt += 1 # 서류성적이 본인보다 낮은 사람들에 비해 면접순위가 높기 때문에 선발.
    ans.append(cnt)

print(*ans,sep="\n")


