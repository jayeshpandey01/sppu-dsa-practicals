'''
  A classic problem that can be solved by backtracking is called the Eight Queens problem, 
which comes from the game of chess. The chess board consists of 64 square arranged in 
an 8 by 8 grid. The board normally alternates between black and white square, but this is 
not relevant for the present problem. The queen can move as far as she wants in any 
direction, as long as she follows a straight line, Vertically, horizontally, or diagonally. 
Write C++ program with recursive function for generating all possible configurations for 
4-queen's problem.

  '''
  #include <iostream>
#include <vector>

// Function to check if a queen can be placed at position (row, col)
bool isSafe(std::vector<int>& board, int row, int col) {
    // Check if there is a queen in the same column
    for (int i = 0; i < row; i++) {
        if (board[i] == col)
            return false;
    }

    // Check if there is a queen in the same diagonal (upper left)
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i] == j)
            return false;
    }

    // Check if there is a queen in the same diagonal (upper right)
    for (int i = row, j = col; i >= 0 && j < 4; i--, j++) {
        if (board[i] == j)
            return false;
    }

    return true;
}

// Recursive function to generate all possible configurations for the 4-Queens problem
void solveNQueens(std::vector<int>& board, int row, std::vector<std::vector<int>>& solutions) {
    // Base case: If all queens are placed, add the current configuration to the solutions
    if (row == 4) {
        solutions.push_back(board);
        return;
    }

    // Try placing the queen at each column in the current row
    for (int col = 0; col < 4; col++) {
        if (isSafe(board, row, col)) {
            board[row] = col;  // Place the queen in the current position

            // Recur for the next row
            solveNQueens(board, row + 1, solutions);

            board[row] = 0;  // Backtrack and remove the queen from the current position
        }
    }
}

// Function to print a solution
void printSolution(const std::vector<int>& board) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (board[i] == j)
                std::cout << "Q ";
            else
                std::cout << ". ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

int main() {
    std::vector<int> board(4, 0);
    std::vector<std::vector<int>> solutions;

    solveNQueens(board, 0, solutions);

    // Print all solutions
    for (const auto& solution : solutions) {
        printSolution(solution);
    }

    return 0;
}
