#include<iostream>

using namespace std;

int main(){
    int val;
    cin>>val;

    if(val%2 == 0 && val > 2)
        cout<<"YES";
    else
        cout<<"NO";
}