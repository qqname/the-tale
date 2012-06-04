# coding: utf-8
from django.test import TestCase

from game.quests.quests_generator.knowlege_base import KnowlegeBase
from game.quests.quests_generator.exceptions import QuestGeneratorException, RollBackException


class KnowlegeBaseInitializationTest(TestCase):

    def setUp(self):
        self.base = KnowlegeBase()

    def test_after_constuction(self):
        self.assertEqual(self.base.persons, {})
        self.assertEqual(self.base.places, {})

    def test_add_place(self):
        self.base.add_place('place_1', external_data={'id': 1, 'name': 'place_1_name'})
        self.assertRaises(QuestGeneratorException, self.base.add_place, 'place_1', external_data={'id': 1, 'name': 'place_1_name'})
        self.base.initialize()


    def test_add_person(self):
        self.base.add_place('place_1', external_data={'id': 1, 'name': 'place_1_name'})
        self.base.add_person('person_1', place='place_1', external_data={'id': 1, 'name': 'person_1_name'})
        self.assertRaises(QuestGeneratorException, self.base.add_person, 'person_1', external_data={'id': 1, 'name': 'person_1_name'})
        self.base.initialize()

    def test_wrong_consistency(self):
        self.base.add_place('place_1', external_data={'id': 1, 'name': 'place_1_name'})
        self.base.add_person('person_2', place='place2', external_data={'id': 1, 'name': 'person_2_name'})
        self.assertRaises(QuestGeneratorException, self.base.initialize)


class KnowlegeBaseTest(TestCase):

    def setUp(self):
        self.base = KnowlegeBase()

        self.base.add_place('place_1', external_data={'id': 1, 'name': 'place_1_name'})
        self.base.add_place('place_2', external_data={'id': 2, 'name': 'place_2_name'})
        self.base.add_place('place_3', external_data={'id': 3, 'name': 'place_3_name'})

        self.base.add_person('person_2_1', place='place_2', external_data={'id': 1, 'name': 'person_2_1_name'})
        self.base.add_person('person_2_2', place='place_2', external_data={'id': 2, 'name': 'person_2_2_name'})
        self.base.add_person('person_3', place='place_3', external_data={'id': 3, 'name': 'person_3_name'})

        self.base.initialize()

    def test_after_initialization(self):
        self.assertEqual(self.base.places['place_1']['persons'], set())
        self.assertEqual(self.base.places['place_2']['persons'], set(['person_2_1', 'person_2_2']))
        self.assertEqual(self.base.places['place_3']['persons'], set(['person_3']))

    def test_get_random_place(self):
        unchoosen_places = set(['place_1', 'place_2', 'place_3'])
        for i in xrange(100):
            unchoosen_places.discard(self.base.get_random_place())
        self.assertEqual(unchoosen_places, set())

    def test_get_random_place_rollback(self):
        self.assertRaises(RollBackException, self.base.get_random_place, exclude=['place_1', 'place_2', 'place_3'])

    def test_get_random_person(self):
        unchoosen_places = set(['person_2_1', 'person_2_2', 'person_3'])
        unchoosen_places.discard(self.base.get_random_person(place='place_3'))
        for i in xrange(100):
            unchoosen_places.discard(self.base.get_random_person(place='place_2'))
        self.assertEqual(unchoosen_places, set())

    def test_get_random_person_rollback(self):
        self.assertRaises(RollBackException, self.base.get_random_person, place='place_1')
        self.assertRaises(RollBackException, self.base.get_random_person, place='place_2', exclude=['person_2_1', 'person_2_2'])
