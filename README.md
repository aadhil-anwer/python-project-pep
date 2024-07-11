N-Queens Visualizer Using Python and Tkinter
Introduction
This project provides a visual representation of the classic N-Queens problem using Python and Tkinter. The N-Queens problem involves placing N chess queens on an N×N chessboard so that no two queens threaten each other. This implementation uses a backtracking algorithm to find all possible solutions and visualizes the process in real-time.

Features
Interactive Visualization: Watch the backtracking algorithm in action as it attempts to place the queens.
Customizable Board Size: Enter the desired number of queens to see the corresponding board size.
Real-Time Updates: The board updates in real-time to show the algorithm's progress.
Statistics: Display the number of solutions found, iterations performed, and the time taken to solve the problem.
Graphical Interface: Utilizes Tkinter for the GUI and PIL for image handling to replace text-based queens with images.
Installation
Clone the repository:
Bash
git clone https://github.com/yourusername/n-queens-visualizer.git
Use code with caution.
content_copy
Navigate to the project directory:
Bash
cd n-queens-visualizer
Use code with caution.
content_copy
Install the required dependencies:
Bash
pip install tkinter pillow
Use code with caution.
content_copy
Usage
Run the main.py script:
Bash
python main.py
Use code with caution.
content_copy
Enter the number of queens when prompted.
Project Structure
main.py: The main script to run the N-Queens visualizer.
README.md: Project documentation and instructions.
queen.png: Image file used to represent the queens on the board (ensure this image is in the same directory as the script).
How It Works
Backtracking Algorithm: The core logic uses a recursive backtracking algorithm to explore all possible positions for the queens.
Tkinter for GUI: The Tkinter library is used to create the graphical user interface, providing a visual representation of the board.
PIL for Images: The Python Imaging Library (PIL) is used to load and display images in place of text-based queens.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Inspired by the classic N-Queens problem in computer science.
Special thanks to the developers and maintainers of Tkinter and PIL libraries.
