void dfs(vector<vector<int>> &v, int node, vector<int> &visited)
{
    visited[node] = 1;
    for (int nbr = 0; nbr < v.size(); ++nbr)
    {
        if (!visited[nbr] && v[node][nbr])
            dfs(v, nbr, visited);
    }
}
int countGroups(vector<string> &related)
{
    int ans = 0;
    int n = related.size();
    vector<vector<int>> graph(n,vector<int>(n,0));
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            
            if (related[i][j] == '1')   
            {
                graph[i][j]=1;
            }
        }
    }

    vector<int> visit(n, 0);
    for (int i = 0; i < n; ++i)
    {
        if (!visit[i])
            dfs(graph, i, visit), ans++;
    }
    return ans;
}
