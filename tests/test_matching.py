import unittest

from routing_service.matching import LoadMatchingData, MatchLRs


class Test(unittest.TestCase):

    def test_matching(self):
        skill_label_list = [
            'logical thinking skills', 'visualization', 'vocabulary', 'visual design', 
            'writing ability', 'writing'
        ]

        result_lr_dict = MatchLRs.match(skill_label_list, offline=True)

        assert(type(result_lr_dict)==dict)