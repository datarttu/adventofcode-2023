from day_07 import *


def test_card_value_mapping():
    m = card_value_mapping()
    assert m["2"] == 2
    assert m["A"] == 14


def test_hand_type_scores():
    assert Hand("AAAAA").type_score == 60000000000
    assert Hand("AAQQ2").type_score == 20000000000
    assert Hand("A2345").type_score == 0


def test_hand_card_scores():
    assert Hand("22222").card_score == 202020202
    assert Hand("AAAAA").card_score == 1414141414
    assert Hand("2A233").card_score == 214020303


def test_hand_total_scores():
    assert Hand("AAAAA").total_score == 61414141414
    assert Hand("2A233").total_score == 20214020303
    assert Hand("99999").total_score == 60909090909


def test_hand_sorting():
    hands = [Hand("AAAAA"), Hand("33445"), Hand("99999")]
    expected = [Hand("33445"), Hand("99999"), Hand("AAAAA")]
    assert sorted(hands) == expected


def test_play():
    assert play("../inputs/day_07_example.txt") == 6440
