#include<bits/stdc++.h>
using namespace std;

struct Interval{
    int start,end;
};

bool CompareInterval(Interval i1, Interval i2){
    return (i1.start < i2.start);
}

void mergeIntervals(Interval arr[], int n){
    if (n<=0){
        return;
    }
    stack<Interval> s;

    sort(arr, arr + n, CompareInterval);

    s.push(arr[0]);

    for(int i=1;i<n;i++){

        Interval top = s.top();

        if (top.end < arr[i].start)
            s.push(arr[i]);

        else if (top.end <= arr[i].end){
                top.end = arr[i].end;
                s.pop();
                s.push(top);
        }
    }
    while (!s.empty()){
        cout<<"{"<<s.top().start<<" "<<s.top().end<<"}"<<endl;
        s.pop();
    }
}

int main(){
    
    int n;
    cout<<"enter n:";
    cin>>n;

    Interval arr[n];
    cout<<"enter pairs";

    for (int i=0;i<n;i++)
        cin>>arr[i].start>>arr[i].end;

    mergeIntervals(arr,n);
}