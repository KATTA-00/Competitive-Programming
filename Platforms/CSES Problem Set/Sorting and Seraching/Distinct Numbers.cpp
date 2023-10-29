#include <iostream>
#include <set>
#include <vector>

int main()
{
    int n;
    std::cin >> n;

    std::set<int> numbers;
    for (int i = 0; i < n; i++)
    {
        int num;
        std::cin >> num;
        numbers.insert(num);
    }

    std::cout << numbers.size() << std::endl;

    return 0;
}
