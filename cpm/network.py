import copy
from typing import Self, NamedTuple


class Node:
    def __init__(self, id_: str, prev_nodes: [Self, ], duration: float):
        self.id_: str = id_  # Czynność
        self.prev_nodes: [Self, ] = copy.deepcopy(prev_nodes)
        self.duration: float = duration

        self.early_start: float = 0
        self.early_final: float = 0
        self.late_start: float = 0
        self.late_final: float = 0
        self.possible_delay: float = 0

class Network:
    nodes: [Node, ] = []
    critical_paths: [[Node, ], ] = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def solve(self):
        pass
