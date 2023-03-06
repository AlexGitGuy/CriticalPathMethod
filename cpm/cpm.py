import data_input
from cpm.network import Network


class CPM:
    def __init__(self):
        self.network: Network = Network()
    def load_data_from_file(self, path: str = "test_data/cpm/simple_test.txt", sep: str = ";"):
        read_data = data_input.load_data_from_file()

        for data in read_data.items():
            print(f"{data[0]}\n\t" + "\n\t".join([str(elem) for elem in data[1]]))

        # Work in progress

    def load_data_from_user(self):
        pass

    def solve(self):
        self.network.solve()

    def print_result_network(self):
        pass

    def show_result_network(self):
        pass