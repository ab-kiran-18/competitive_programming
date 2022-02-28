#include<bits/stdc++.h>
using namespace std;

int kth_smallest(map<int,int> mp, int k){
    int freq = 0;
    for (auto it = mp.begin(); it != mp.end(); it++){
        freq += (it->second);
        if (freq > k){
            return it->first;
        }
    }
    return -1;
}

// here we used maps because they are sorted by default so if we traverse through them we can get 
// ans quickly even if we have duplicate in array

int main(){
    int n;  cin>>n;
    int k;  cin>>k;
    vector<int> vec;
    map<int,int> mp;
    for(int i=0;i<n;i++)
    {   
        int x;
        cin>>x;
        mp[x]++;
        vec.push_back(x);
    }
    int ans = kth_smallest(mp,k);
    cout<<"kth smallest element in given array is:"<<ans<<endl;
}