#include <iostream>
#include <set>

using namespace std;

int main()
{
	set<long int> set1;
	long int n;
	cin>> n;
	for (int i=0;i<n;i++){
		long int num;
		cin>> num;
		set1.insert(num);
	}

	long int ans=set1.size();
	cout<< ans << "\n";

	return 0;
}