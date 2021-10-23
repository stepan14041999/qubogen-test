# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import qubogen


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    edges = [[0, 1], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
    n_nodes = 5
    g = qubogen.Graph(edges=edges, n_nodes=n_nodes)

    q = qubogen.qubo_tsp(g, n_color=5)
    print(q)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
