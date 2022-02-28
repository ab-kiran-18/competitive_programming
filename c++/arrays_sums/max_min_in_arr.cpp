#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main(){
    int n;
    cin>>n;
    int arr[n];
    ll mini = INT_MAX;
    ll maxi = INT_MIN;
    for(int i=0;i<n;i++){
        cin>>arr[i];
        if (arr[i] > maxi)
            maxi = arr[i];
        if (arr[i] < mini)
            mini = arr[i];
    }
    cout<<"max_element is:"<<" "<<maxi<<"  "<<"min_element is:"<<mini<<endl;
}