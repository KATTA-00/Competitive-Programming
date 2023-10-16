#include <bits/stdc++.h>

using namespace std;

int parent[100001] ;
unordered_map<string, int> mapping;
vector<string> rev_mapping;
int c = 0;

int get_or_create_mapping(const string& name) {
    if (mapping.find(name) == mapping.end()) {
        mapping[name] = c;
        rev_mapping.push_back(name);
        c++;
    }

    return mapping[name];
}

int main() {
    int n;
    cin >> n;
    memset(parent, -1, sizeof(parent));
    
    for (int i = 0; i < n; ++i) {
        string a, b;
        cin >> a >> b;

        parent[get_or_create_mapping(a)] = get_or_create_mapping(b);
    }

    int t;
    cin >> t;
    string a, b;

    for (int i = 0; i < t; ++i) {
        char s;
        cin >> s;

        if (s == 'N') {
            cin >> a >> b;
            parent[get_or_create_mapping(b)] = mapping[a];
        } else if (s == 'R') {
            cin >> a;
            parent[mapping[a]] = -1;
        } else {
            int num;
            cin >> a >> num;

            int node = mapping[a];

            for (int j = 0; j < num; ++j) {
                if (node == -1) {
                    break;
                }

                node = parent[node];
            }

            if (node == -1 || node == 0) {
                cout << "None" << endl;
            } else {
                cout << rev_mapping[node] << endl;
            }
        }
    }

    return 0;
}
