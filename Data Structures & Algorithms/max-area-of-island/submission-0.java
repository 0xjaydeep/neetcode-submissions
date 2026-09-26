class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxAreaIsland = 0;
        int rows = grid.length, cols = grid[0].length;

        for(int row = 0; row < rows; row++) {
            for(int col = 0; col < cols; col++) {
                if(grid[row][col] == 1) {
                    int visited = 0;
                    visited = dfs(grid, row, col);
                    maxAreaIsland = Math.max(maxAreaIsland, visited);
                }
            }
        }

        return maxAreaIsland;
    }

    private int dfs(int[][]grid, int row, int col) {
        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || grid[row][col] == 0) return 0;
        grid[row][col] = 0;
        int visited = 1;
        visited += dfs(grid, row, col +1);
        visited += dfs(grid, row, col -1);
        visited += dfs(grid, row +1, col);
        visited += dfs(grid, row -1, col);
        return visited;
    }
}
