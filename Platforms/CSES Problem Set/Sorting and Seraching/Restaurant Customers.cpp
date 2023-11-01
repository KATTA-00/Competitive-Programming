#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int n;
    std::cin >> n;

    std::vector<std::pair<int, int>> times;

    for (int i = 0; i < n; i++)
    {
        int x, y;
        std::cin >> x >> y;
        times.push_back(std::make_pair(x, 1));
        times.push_back(std::make_pair(y, -1));
    }

    std::sort(times.begin(), times.end());

    int max_count = 0;
    int count = 0;

    for (const std::pair<int, int> &event : times)
    {
        count += event.second;

        if (max_count < count)
        {
            max_count = count;
        }
    }

    std::cout << max_count << std::endl;

    return 0;
}
