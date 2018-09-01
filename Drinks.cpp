#include<iostream>
#include<vector>
#include<iomanip>

using namespace std;

int main(){
    int size;
    vector<int> vec;
    cin>>size;
    int val;
    for(int i=0;i<size;i++){
        cin>>val;
        vec.push_back(val);
    }

    double sum = 0;
    for(int i=0;i<size;i++)
        sum = sum + vec[i];

    cout<<fixed<<setprecision(12)<<sum/size<<endl;

    return 0;
}