'''
N개의 파이프가 필요
공사하고 남은 M개의 파이프가 있다
1 <= M <= 50
각각의길이 100,000을 넘지 않는 정수.
1 <= N <= 1023
128이하의 자연수

M개의 파이프를 잘라서 N개의 파이프 만들기
'''

def find(m_pipe,n_pipe,visited,m_index,n_index):
    while True:
        if n_pipe[n_index] > m_pipe[m_index]:
            return
        m_pipe[m_index] -= n_pipe[n_index]
        visited[n_index] = 1z
        print(m_index,m_pipe)
        print(n_index,n_pipe)
        print(visited)
        if m_pipe[m_index] >= n_pipe[n_index+1]:
            find(m_pipe,n_pipe,visited,m_index,n_index+1)
        else:
            find(m_pipe,n_pipe,visited,m_index+1,0)
        m_pipe[m_index] += n_pipe[n_index]
        visited[n_index] = 0
        n_index += 1
        



m = int(input())
mpipe = list(map(int,input().split()))
mpipe.sort()
n = int(input())
npipe = list(map(int,input().split()))
n_visited = [0]*n
npipe.sort()
print(mpipe)
print(npipe)

find(mpipe,npipe,n_visited,0,0)
