"""
Copyright (C) 2023 TH Köln – University of Applied Sciences

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import sys

import pygame.freetype

import ComponentAssembly.ComponentAssembler
from GraphContent import GraphContent
from GraphModel.Graph import Graph
from View.ApplicationLoopManager import ApplicationLoopManager

if __name__ == '__main__':
    # Graph
    graph = Graph()
    graph.team_name = "Deez"
    graph_content = GraphContent(graph)

    # Application
    component_assembler = ComponentAssembly.ComponentAssembler.ComponentAssembler(graph, False)
    main = ApplicationLoopManager(component_assembler)
    # pygame beenden
    pygame.quit()
    sys.exit()
