/////////////////////////////////////////
// iterate vectors
for (auto element : grid[i])
{
    cout << element << " ";
}

///////////////////////////////////
// fill arrays
bool visited[MAX];
fill(begin(visited), begin(visited) + n, false);