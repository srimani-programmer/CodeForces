#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int val;
    vector<int> vec;
    for(int i=0;i<3;i++){
        cin>>val;
        vec.push_back(val);
    }
    sort(vec.begin(),vec.end());

    cout<<vec[2] - vec[0]<<endl;

    return 0;
}