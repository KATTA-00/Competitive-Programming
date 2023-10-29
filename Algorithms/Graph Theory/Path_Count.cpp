#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

int countPaths(
    const unordered_map<int, vector<int>> &graph,
    int source, int destination,
    unordered_set<int> &visited)
{

    if (source == destination)
    {
        return 1;
    }

    if (visited.find(source) != visited.end())
    {
        return 0;
    }

    int count = 0;
    visited.insert(source);

    for (int neighbor : graph.at(source))
    {
        if (visited.find(neighbor) == visited.end())
        {
            count += countPaths(graph, neighbor,
                                destination, visited);
        }
    }

    visited.erase(source);
    return count;
}

int main()
{
    // Original inputs
    unordered_map<int, vector<int>> graph = {{0, {1, 2, 4}},
                                             {1, {3, 4}},
                                             {2, {3, 1}},
                                             {3, {2}}};
    int source = 0;
    int destination = 4;
    unordered_set<int> visited;

    int count = countPaths(graph, source, destination, visited);

    cout << count << endl;

    return 0;
}
