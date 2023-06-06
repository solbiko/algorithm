"""
11004
수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램
첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.
둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)
5 2
4 1 2 3 5
"""
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))
tmp=[0]*n  # 정렬용 임시 리스트

# 병합정렬
def mergeSort(s,e):
    if e-s<1:return
    m=int(s+(e-s)/2)  # 중간점
    # 재귀함수 형태로 표현
    mergeSort(s,m)
    mergeSort(m+1,e)

    for i in range(s,e+1):
        tmp[i]=a[i]

    # 정렬할 a리스트 인덱스
    j=s
    # 투 포인터
    idx1=s
    idx2=m+1
    # 두 그룹을 병합
    while idx1<=m and idx2<=e:
        if tmp[idx1]>tmp[idx2]:
            a[j]=tmp[idx2]
            j+=1
            idx2+=1
        else:
            a[j]=tmp[idx1]
            j+=1
            idx1+=1
    # 한쪽 그룹이 모두 선택된 후 남아있는 값 정리
    while idx1<=m:
        a[j]=tmp[idx1]
        j+=1
        idx1+=1
    while idx2 <= m:
        a[j] = tmp[idx2]
        j+=1
        idx2+=1

mergeSort(0,n-1)

print(a[k-1])