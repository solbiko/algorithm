"""
1517
N개의 수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에 대해서 버블 소트를 수행할 때, Swap이 총 몇 번 발생하는지 알아내는 프로그램을 작성하시오.
첫째 줄에 N(1 ≤ N ≤ 500,000)이 주어진다.
다음 줄에는 N개의 정수로 A[1], A[2], …, A[N]이 주어진다.
3
3 2 1
"""
import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
tmp=[0]*n  # 정렬용 임시 리스트

cnt=0

def mergeSort(s,e):
    global cnt
    if e-s<1:return
    m=int(s+(e-s)/2)  # 중간점
    # 재귀함수 형태로 표현
    mergeSort(s,m)
    mergeSort(m+1,e)

    for i in range(s,e+1):
        tmp[i]=a[i]

    # 정렬할 a리스트 인덱스
    k=s
    # 투 포인터
    idx1=s
    idx2=m+1
    # 두 그룹을 병합
    while idx1<=m and idx2<=e:
        if tmp[idx1]>tmp[idx2]:
            a[k] = tmp[idx2]
            cnt=cnt+idx2-k  # swap 카운트
            k+=1
            idx2+=1
        else:
            a[k]=tmp[idx1]
            k+=1
            idx1+=1
    # 한쪽 그룹이 모두 선택된 후 남아있는 값 정리
    while idx1<=m:
        a[k]=tmp[idx1]
        k+=1
        idx1+=1
    while idx2<=m:
        a[k]=tmp[idx2]
        k+=1
        idx2+=1

mergeSort(0,n-1)
print(cnt)