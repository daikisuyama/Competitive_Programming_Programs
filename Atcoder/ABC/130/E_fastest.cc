#pragma GCC optimize("O3")
#include <bits/stdc++.h>

#define int long long int
using namespace std;
#define MOD 1000000007
using namespace std;

int n,m,s[2001],t[2001],sumarray[2001]={0};

signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> t[i];
    }
    int out = 1;

    for (int i = 0; i < m; i++) {
        int temp = 0;
        for (int j = 0; j < n; j++) {
            if(j){
                if (t[i] == s[j]) {
                    int prev = temp + sumarray[j];
                    sumarray[j] += (temp + 1) % MOD;
                    temp = prev;
                } else {
                    temp += sumarray[j];
                }
            } else {
                temp += sumarray[j];
                if (t[i] == s[j]) {
                    sumarray[j] += 1;
                }
            }
        }
    }
    for (int i = 0; i < n; i++) {
        out += sumarray[i];
        out %= MOD;
    }
    cout << out << endl;
    return 0;
}

