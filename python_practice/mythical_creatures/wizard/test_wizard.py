import pytest
from wizard import Wizard

def test_has_name():
    wizard1 = Wizard('Gandolf the Grey')
    wizard2 = Wizard('Gandolf the White')

    assert wizard1.name == 'Gandolf the Grey'
    assert wizard2.name == 'Gandolf the White'

def test_default_bearded():
    wizard1 = Wizard('Dumbledore')
    wizard2 = Wizard('Snape', False)

    assert wizard1.is_bearded() == True
    assert wizard2.is_bearded() == False

def test_has_powers():
    wizard1 = Wizard('Dumbledore', True)
    wizard2 = Wizard('Snape', False)

    assert wizard1.incantation('chown ~/bin') == 'sudo chown ~/bin'
    assert wizard2.incantation('rm -rf /home/mirandax') == 'sudo rm -rf /home/mirandax'

def test_default_rested():
    wizard1 = Wizard('Sal')
    wizard2 = Wizard('Oscar', False)

    assert wizard1.is_rested() == True
    assert wizard2.is_rested() == True

def test_casts_spells():
    wizard1 = Wizard('Sal', True)
    wizard2 = Wizard('Oscar', False)

    assert wizard1.cast() == 'MAGIC MISSILE!'
    assert wizard2.cast() == 'MAGIC MISSILE!'

def test_gets_tired():
    wizard = Wizard('Oscar', False)

    assert wizard.spell_count == 0

    for _ in range(2):
        wizard.cast()

    assert wizard.is_rested() == True
    assert wizard.spell_count == 2
    wizard.cast()
    assert wizard.is_rested() == False
    assert wizard.spell_count == 3