from autode import reactions
import pytest


def test_classify():

    addition = reactions.classify([0, 0], [0])
    assert addition.name == 'addition'

    dissociation = reactions.classify([0], [0, 0])
    assert dissociation.name == 'dissociation'

    substitution = reactions.classify([0, 0], [0, 0])
    assert substitution.name == 'substitution'

    elimination = reactions.classify([0, 0], [0, 0, 0])
    assert elimination.name == 'elimination'

    rearrangement = reactions.classify([0], [0])
    assert rearrangement.name == 'rearrangement'

    with pytest.raises(SystemExit):
        bad_reaction = reactions.classify([], [])