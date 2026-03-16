
from src.circle import has_intersection, radius_sum
import pytest

def test_intersection_normal_true():
    assert has_intersection((0,0,5), (4,0,5)) == True


def test_intersection_normal_false():
    assert has_intersection((0,0,2), (10,0,2)) == False


def test_intersection_touching():
    assert has_intersection((0,0,5), (10,0,5)) == True


def test_intersection_same_center():
    assert has_intersection((0,0,5), (0,0,3)) == True


def test_intersection_wrong_expected():  # záměrně failující
    assert has_intersection((0,0,1), (5,0,1)) == True


def test_radius_sum():
    assert radius_sum(3, 4) == 7


