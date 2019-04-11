#include <stdio.h>
#include <stdlib.h>

int n,h,m,matrix[30][10],ret=4;

int check()
{
		int i,j,k;
		for(i = 0;i<n;i++)
		{
				k = i;
				for(j=0;j<h;j++)
				{
						if(matrix[j][k] == 1)
								k += 1;
						else if(matrix[j][k-1] == 1)
								k -= 1;
				}
				if(i != k)
						return 0;
		}
		return 1;
}


void DFS(int cnt,int x,int y)
{
		if(cnt > ret)
				return;
		else if(check() == 1)
		{
				ret = cnt;
				return;
		}
		if(cnt == 3)
				return;
		int i,j;
		for(i = y;i<h;i++)
		{
				for(j=x;j<n-1;j++)
				{
						if(matrix[i][j] != 0)
						{
								j++;
								continue;
						}
						matrix[i][j] = 1;
						DFS(cnt+1,j+2,i);
						matrix[i][j] = 0;
				}
				x = 0;
		}
}	

int main()
{
		scanf("%d %d %d",&n,&m,&h);
		int i,a,b;
		for(i=0;i<m;i++)
		{
				scanf("%d %d",&a,&b);
				matrix[a-1][b-1] = 1;
		}

		DFS(0,0,0);
		if(ret > 3)
				printf("-1\n");
		else
				printf("%d\n",ret);

		return 0;
}
