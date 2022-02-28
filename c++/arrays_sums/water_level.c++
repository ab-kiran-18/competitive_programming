#include<bits/stdc++.h>
using namespace std;

int water_volume(vector<int> vec,int n){
    if (n==1 || n==2)
        return 0;
    int i = 1, j = n-2;
    int volume = 0;
    int left_max = vec[0];
    int right_max = vec[n-1];
    while(i <= j){
        if(left_max < right_max){
            if (vec[i] < left_max)
                volume += left_max - vec[i];
            else
                left_max = vec[i];
            i++;
        }else{
            if (vec[j] < right_max)
                volume += right_max - vec[j];
            else
                right_max = vec[j];
            j--;
        }
    }
    return volume;
}

int main(){
    vector <int> vec {1,2,1,2,3,1,0,1,2,0,1,0};
    int n = vec.size();
    int water_vol = water_volume(vec,n);
    cout<<water_vol<<endl;
}