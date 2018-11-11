#include<iostream>

using namespace std;

int main(){
    int size;
    cin >> size;

    int *a = new int[size];
    for(int i=0;i<size;i++)
        cin>>a[i];
    int count = 1;
    for(int i=0;i<size-1;i++)
        if(a[i] != a[i+1])
            count++;

        cout<<count<<endl;

    return 0;
}