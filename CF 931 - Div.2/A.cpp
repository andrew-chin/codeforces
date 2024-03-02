// Problem: E. Weird LCM Operations
// Contest: Codeforces - Codeforces Round 931 (Div. 2)
// URL: https://codeforces.com/contest/1934/problem/E
// Memory Limit: 256 MB
// Time Limit: 2000 ms


#include <bits/stdc++.h>
using namespace std;
#define int long long
const int MXN = 100005;


signed main(){
    int t;
    cin >> t;
    
    for(int i = 0; i < t; i++){
    	int n;
    	cin >> n;
    	int arr[n];
    	int a, b, c, d;
    	for(int j = 0; j < n; j++){
    		cin >> arr[j];
    	}
    	sort(arr, arr + n);
    	a = arr[0], b = arr[n - 1], c = arr[1], d = arr[n - 2];
    	
    	cout << abs(a - b) + abs(b - c) + abs(c - d) + abs(d - a) << endl;
    }
}

// i, j, k, l with maximum spacing?

// 8
// 4 2 1 5 2 11 7
