#include<bits/stdc++.h>
using namespace std;

int main(){
    int rows,cols;
    cin>>rows>>cols;
    int mat[rows][cols];
    bool zero_rows[rows];
    memset(zero_rows,false,rows);
    bool zero_cols[cols];
    memset(zero_cols,false,cols);
    for(int i=0;i<rows;i++)
        for(int j=0;j<cols;j++){
            cin>>mat[i][j];
            if (mat[i][j]==0){
                zero_rows[i] = true;
                zero_cols[j] = true;
            }
        }
    for(int i=0;i<rows;i++)
        if(zero_rows[i])
            for(int j=0;j<cols;j++)
                mat[i][j] = 0;

    for(int i=0;i<cols;i++)
        if(zero_cols[i])
            for(int j=0;j<rows;j++)
                mat[j][i] = 0;

    cout<<"matrix is:"<<endl;
    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++)
            cout<<mat[i][j]<<"  ";
        cout<<endl;
    }
    return 0;
}