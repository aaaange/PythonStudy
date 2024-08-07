# 백준 문제풀이
## Git & Github 응용
1. 문제를 풀기 전에, Github에 Issue를 생성한다. 이슈명은 자유롭게 해도 전혀 상관없음.
2. 이슈를 생성했으니, 담당자(Assign를 자신으로 지정한다.)지정 후, Developement 탭을 통해, feature/이슈번호로 브랜치를 생성한다.
    - Git은 추적 중인 브랜치와 커밋에 현재 head를 나타내고 그 head를 내가 만든 브랜치로 옮기기 위해서 checkout을 해야하는데 내가 원격 저장소에서 브랜치를 만들었으니 로컬과 원격을 동기화해야 함(fetch). 그리고 이후에 checkout 하기.
    `git fetch origin`
    `git checkout feature/10`
3. 문제번호에 맞는 파일을 생성한다. ex) 1000.py
4. 문제를 등록한 시점에 맞는 커밋(수정사항을 반영하는것)을 한다.
5. 그 다음에 문제를 푼다.
6. 문제를 풀고나서, 커밋을 한다. -> 이 때는 맞든 틀리든 일단 커밋을 먼저 해서, 맨 처음 제출한 코드를 기록해놓는다.
7. 만약 제출을 했는데, 틀렸다 하면 수정을 한 뒤, 다시 커밋을 하고, 다시 제출한다.
8. 정답이 되었을 경우, Github Desktop에서 Push를 한다. -> 이 때, Push를 하면, Github 사이트에서도 커밋이 반영된다.
9. 그 다음, Github 사이트에서(혹은 Github Desktop에서 Pull Request Preview -> Create Pull Request) Pull Request를 한다. -> 이 때, Pull Request를 하면, Github 사이트에서 코드리뷰를 할 수 있다.
    - 이 때 중요한 것은, PR(Pull Request)을 할 때, 내용에 close #이슈번호 를 통해 이슈가 해결되었음을 알려줍니다.
10. 그 다음, PR을 Merge합니다.
11. feature/이슈번호 브랜치를 삭제한다.
12. 다음 문제를 풀기 전에, Github Desktop에서 Fetch origin을 통해, 최신화를 한다.