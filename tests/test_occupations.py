import unittest
import json

from routing_service.utils import occ_graph_path

from routing_service.add_occupations import AddOccupations
from routing_service.datahandler import get_paths


class Test(unittest.TestCase):

    def test_add_occupations_to_skill_graph_data(self):
        with open(occ_graph_path, "r") as file:
            graph_data = json.load(file)

            graph_data_extended = AddOccupations.addOccRelations(graph_data)
    
            destination = "specialist nurse"
            origin_skills = ["focus", "tet node not in graph"]

            result_skill_labels = get_paths(destination, origin_skills)

