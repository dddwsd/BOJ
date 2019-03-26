#include <iostream>
#include <cstring>
using namespace std;

char u[3][3], d[3][3], f[3][3], b[3][3], l[3][3], r[3][3];
char utmp[3][3], dtmp[3][3], ftmp[3][3], btmp[3][3], ltmp[3][3], rtmp[3][3];
void cpy_cube() {
   for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
         utmp[i][j] = u[i][j], dtmp[i][j] = d[i][j], ftmp[i][j] = f[i][j], btmp[i][j] = b[i][j], ltmp[i][j] = l[i][j], rtmp[i][j] = r[i][j];
      }
   }
}
void find_sol(char cmd[][2], int n) {
   for (int i = 0; i < n; i++) {
      cpy_cube();
      if (cmd[i][1] == '+') {
         if (cmd[i][0] == 'U') {
            f[0][0] = rtmp[0][0], f[0][1] = rtmp[0][1], f[0][2] = rtmp[0][2];
            l[0][0] = ftmp[0][0], l[0][1] = ftmp[0][1], l[0][2] = ftmp[0][2];
            b[0][0] = ltmp[0][0], b[0][1] = ltmp[0][1], b[0][2] = ltmp[0][2];
            r[0][0] = btmp[0][0], r[0][1] = btmp[0][1], r[0][2] = btmp[0][2];
            /* 자체 회전 */
            u[0][0] = utmp[2][0], u[0][1] = utmp[1][0], u[0][2] = utmp[0][0];
            u[1][0] = utmp[2][1], u[1][1] = utmp[1][1], u[1][2] = utmp[0][1];
            u[2][0] = utmp[2][2], u[2][1] = utmp[1][2], u[2][2] = utmp[0][2];
         
         }
         else if (cmd[i][0] == 'D') {
            r[2][0] = ftmp[2][0], r[2][1] = ftmp[2][1], r[2][2] = ftmp[2][2];
            b[2][0] = rtmp[2][0], b[2][1] = rtmp[2][1], b[2][2] = rtmp[2][2];
            l[2][0] = btmp[2][0], l[2][1] = btmp[2][1], l[2][2] = btmp[2][2];
            f[2][0] = ltmp[2][0], f[2][1] = ltmp[2][1], f[2][2] = ltmp[2][2];
            /* 자체 회전 */
            d[0][0] = dtmp[2][0], d[0][1] = dtmp[1][0], d[0][2] = dtmp[0][0];
            d[1][0] = dtmp[2][1], d[1][1] = dtmp[1][1], d[1][2] = dtmp[0][1];
            d[2][0] = dtmp[2][2], d[2][1] = dtmp[1][2], d[2][2] = dtmp[0][2];
         }
         else if (cmd[i][0] == 'F') {
            r[0][0] = utmp[2][0], r[1][0] = utmp[2][1], r[2][0] = utmp[2][2];
            d[0][0] = rtmp[2][0], d[0][1] = rtmp[1][0], d[0][2] = rtmp[0][0];
            l[0][2] = dtmp[0][0], l[1][2] = dtmp[0][1], l[2][2] = dtmp[0][2];
            u[2][2] = ltmp[0][2], u[2][1] = ltmp[1][2], u[2][0] = ltmp[2][2];
            /* 자체 회전 */
            f[0][0] = ftmp[2][0], f[0][1] = ftmp[1][0], f[0][2] = ftmp[0][0];
            f[1][0] = ftmp[2][1], f[1][1] = ftmp[1][1], f[1][2] = ftmp[0][1];
            f[2][0] = ftmp[2][2], f[2][1] = ftmp[1][2], f[2][2] = ftmp[0][2];
         }
         else if (cmd[i][0] == 'B') {
            u[0][0] = rtmp[0][2], u[0][1] = rtmp[1][2], u[0][2] = rtmp[2][2];
            r[0][2] = dtmp[2][2], r[1][2] = dtmp[2][1], r[2][2] = dtmp[2][0];
            d[2][2] = ltmp[2][0], d[2][1] = ltmp[1][0], d[2][0] = ltmp[0][0];
            l[2][0] = utmp[0][0], l[1][0] = utmp[0][1], l[0][0] = utmp[0][2];
            /* 자체 회전 */
            b[0][0] = btmp[2][0], b[0][1] = btmp[1][0], b[0][2] = btmp[0][0];
            b[1][0] = btmp[2][1], b[1][1] = btmp[1][1], b[1][2] = btmp[0][1];
            b[2][0] = btmp[2][2], b[2][1] = btmp[1][2], b[2][2] = btmp[0][2];
         }
         else if (cmd[i][0] == 'L') {
            f[0][0] = utmp[0][0], f[1][0] = utmp[1][0], f[2][0] = utmp[2][0];
            d[2][0] = ftmp[2][0], d[1][0] = ftmp[1][0], d[0][0] = ftmp[0][0];
            b[0][2] = dtmp[2][0], b[1][2] = dtmp[1][0], b[2][2] = dtmp[0][0];
            u[2][0] = btmp[0][2], u[1][0] = btmp[1][2], u[0][0] = btmp[2][2];
            /* 자체회전 */
            l[0][0] = ltmp[2][0], l[0][1] = ltmp[1][0], l[0][2] = ltmp[0][0];
            l[1][0] = ltmp[2][1], l[1][1] = ltmp[1][1], l[1][2] = ltmp[0][1];
            l[2][0] = ltmp[2][2], l[2][1] = ltmp[1][2], l[2][2] = ltmp[0][2];
         }
         else if (cmd[i][0] == 'R') {
            u[0][2] = ftmp[0][2], u[1][2] = ftmp[1][2], u[2][2] = ftmp[2][2];
            f[0][2] = dtmp[0][2], f[1][2] = dtmp[1][2], f[2][2] = dtmp[2][2];
            d[0][2] = btmp[2][0], d[1][2] = btmp[1][0], d[2][2] = btmp[0][0];
            b[2][0] = utmp[0][2], b[1][0] = utmp[1][2], b[0][0] = utmp[2][2];
            /* 자체 회전 */
            r[0][0] = rtmp[2][0], r[0][1] = rtmp[1][0], r[0][2] = rtmp[0][0];
            r[1][0] = rtmp[2][1], r[1][1] = rtmp[1][1], r[1][2] = rtmp[0][1];
            r[2][0] = rtmp[2][2], r[2][1] = rtmp[1][2], r[2][2] = rtmp[0][2];
         }
      }
      else if (cmd[i][1] == '-') {
         if (cmd[i][0] == 'U') {
            r[0][0] = ftmp[0][0], r[0][1] = ftmp[0][1], r[0][2] = ftmp[0][2];
            b[0][0] = rtmp[0][0], b[0][1] = rtmp[0][1], b[0][2] = rtmp[0][2];
            l[0][0] = btmp[0][0], l[0][1] = btmp[0][1], l[0][2] = btmp[0][2];
            f[0][0] = ltmp[0][0], f[0][1] = ltmp[0][1], f[0][2] = ltmp[0][2];
            /* 자체 회전 */
            u[0][0] = utmp[0][2], u[0][1] = utmp[1][2], u[0][2] = utmp[2][2];
            u[1][0] = utmp[0][1], u[1][1] = utmp[1][1], u[1][2] = utmp[2][1];
            u[2][0] = utmp[0][0], u[2][1] = utmp[1][0], u[2][2] = utmp[2][0];
         }
         else if (cmd[i][0] == 'D') {
            f[2][0] = rtmp[2][0], f[2][1] = rtmp[2][1], f[2][2] = rtmp[2][2];
            l[2][0] = ftmp[2][0], l[2][1] = ftmp[2][1], l[2][2] = ftmp[2][2];
            b[2][0] = ltmp[2][0], b[2][1] = ltmp[2][1], b[2][2] = ltmp[2][2];
            r[2][0] = btmp[2][0], r[2][1] = btmp[2][1], r[2][2] = btmp[2][2];
            /* 자체 회전 */
            d[0][0] = dtmp[0][2], d[0][1] = dtmp[1][2], d[0][2] = dtmp[2][2];
            d[1][0] = dtmp[0][1], d[1][1] = dtmp[1][1], d[1][2] = dtmp[2][1];
            d[2][0] = dtmp[0][0], d[2][1] = dtmp[1][0], d[2][2] = dtmp[2][0];
         }
         else if (cmd[i][0] == 'F') {
            u[2][0] = rtmp[0][0], u[2][1] = rtmp[1][0], u[2][2] = rtmp[2][0];
            r[0][0] = dtmp[0][2], r[1][0] = dtmp[0][1], r[2][0] = dtmp[0][0];
            d[0][2] = ltmp[2][2], d[0][1] = ltmp[1][2], d[0][0] = ltmp[0][2];
            l[2][2] = utmp[2][0], l[1][2] = utmp[2][1], l[0][2] = utmp[2][2];
            /* 자체 회전 */
            f[0][0] = ftmp[0][2], f[0][1] = ftmp[1][2], f[0][2] = ftmp[2][2];
            f[1][0] = ftmp[0][1], f[1][1] = ftmp[1][1], f[1][2] = ftmp[2][1];
            f[2][0] = ftmp[0][0], f[2][1] = ftmp[1][0], f[2][2] = ftmp[2][0];
         }
         else if (cmd[i][0] == 'B') {
            r[0][2] = utmp[0][0], r[1][2] = utmp[0][1], r[2][2] = utmp[0][2];
            d[2][0] = rtmp[2][2], d[2][1] = rtmp[1][2], d[2][2] = rtmp[0][2];
            l[0][0] = dtmp[2][0], l[1][0] = dtmp[2][1], l[2][0] = dtmp[2][2];
            u[0][2] = ltmp[0][0], u[0][1] = ltmp[1][0], u[0][0] = ltmp[2][0];
            /* 자체 회전 */
            b[0][0] = btmp[0][2], b[0][1] = btmp[1][2], b[0][2] = btmp[2][2];
            b[1][0] = btmp[0][1], b[1][1] = btmp[1][1], b[1][2] = btmp[2][1];
            b[2][0] = btmp[0][0], b[2][1] = btmp[1][0], b[2][2] = btmp[2][0];
         }
         else if (cmd[i][0] == 'L') {
            u[0][0] = ftmp[0][0], u[1][0] = ftmp[1][0], u[2][0] = ftmp[2][0];
            f[0][0] = dtmp[0][0], f[1][0] = dtmp[1][0], f[2][0] = dtmp[2][0];
            d[0][0] = btmp[2][2], d[1][0] = btmp[1][2], d[2][0] = btmp[0][2];
            b[2][2] = utmp[0][0], b[1][2] = utmp[1][0], b[0][2] = utmp[2][0];
            /* 자체 회전 */
            l[0][0] = ltmp[0][2], l[0][1] = ltmp[1][2], l[0][2] = ltmp[2][2];
            l[1][0] = ltmp[0][1], l[1][1] = ltmp[1][1], l[1][2] = ltmp[2][1];
            l[2][0] = ltmp[0][0], l[2][1] = ltmp[1][0], l[2][2] = ltmp[2][0];
         }
         else if (cmd[i][0] == 'R') {
            f[0][2] = utmp[0][2], f[1][2] = utmp[1][2], f[2][2] = utmp[2][2];
            d[2][2] = ftmp[2][2], d[1][2] = ftmp[1][2], d[0][2] = ftmp[0][2];
            b[0][0] = dtmp[2][2], b[1][0] = dtmp[1][2], b[2][0] = dtmp[0][2];
            u[2][2] = btmp[0][0], u[1][2] = btmp[1][0], u[0][2] = btmp[2][0];
            /* 자체 회전 */
            r[0][0] = rtmp[0][2], r[0][1] = rtmp[1][2], r[0][2] = rtmp[2][2];
            r[1][0] = rtmp[0][1], r[1][1] = rtmp[1][1], r[1][2] = rtmp[2][1];
            r[2][0] = rtmp[0][0], r[2][1] = rtmp[1][0], r[2][2] = rtmp[2][0];
         }
      }
   }

   for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
         cout << u[i][j];
      }
      cout << '\n';
   }
}

int main()
{
   int t, n;
   char cmd[1005][2];
   cin >> t;
   for (int i = 0; i < t; i++) {
      memset(u, 'w', sizeof(u));
      memset(d, 'y', sizeof(d));
      memset(f, 'r', sizeof(f));
      memset(b, 'o', sizeof(b));
      memset(l, 'g', sizeof(l));
      memset(r, 'b', sizeof(r));
      cin >> n;
      getchar();
      for (int j = 0; j < n; j++) {
         scanf("%1c%1c", &cmd[j][0], &cmd[j][1]);
         getchar();
      }
      find_sol(cmd, n);
      memset(cmd, 0, sizeof(cmd));      //명령어 배열 0으로 초기화
   }
   
   return 0;
}
