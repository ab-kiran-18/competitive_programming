#include<bits/stdc++.h>
using namespace std;

int maxProfit(vector<int>& vec) {
    int min = vec[0];
    int profit = 0;
    int max_profit = 0;
    for(int i=0;i<vec.size();i++){
        if (vec[i] < min){
            min = vec[i];
        }
        profit = vec[i] - min;
        max_profit = max(profit,max_profit);
    }
    return max_profit;
}

int main(){
    int n;
    cin>>n;
    vector<int> vec;
    for(int i=0;i<n;i++){
        int x;  cin>>x;
        vec.push_back(x);
    }
    cout<<maxProfit(vec)<<" ";
}   