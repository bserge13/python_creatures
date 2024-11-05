import pytest 
from centaur import Centaur 

def test_name():
    centaur = Centaur('George', 'Palomino')
    assert centaur.name == 'George'

def test_breed():
    centaur = Centaur('George', 'Palomino')
    assert centaur.breed == 'Palomino'

def test_bow_skills():
    centaur = Centaur('George', 'Palomino')
    assert centaur.shoot() == 'Twang!!!'

def test_running_sounds():
    centaur = Centaur('George', 'Palomino')
    assert centaur.run() == 'Clop clop clop clop!'

def test_not_default_cranky():
    centaur = Centaur('George', 'Palomino')
    assert centaur.is_cranky() == False

def test_default_standing():
    centaur = Centaur('George', 'Palomino')
    assert centaur.is_standing() == True

def test_tired_running_or_shooting():
    centaur = Centaur('George', 'Palomino')
    assert centaur.is_cranky() == False

    centaur.run()
    centaur.shoot()
    centaur.run()

    assert centaur.is_cranky() == True

def test_no_shooting_tired():
    centaur = Centaur('George', 'Palomino')

    for _ in range(3):
        centaur.shoot()

    assert centaur.shoot() == 'NO!'

def test_no_sleep_standing():
    centaur = Centaur('George', 'Palomino')

    assert centaur.is_standing() == True
    assert centaur.sleep() == 'NO!'

def test_no_standing_laying_down():
    centaur = Centaur('George', 'Palomino')

    assert centaur.is_standing() == True
    assert centaur.is_laying() == False

    centaur.lay_down()

    assert centaur.is_standing() == False
    assert centaur.is_laying() == True

def test_sleeps_laying_down():
    centaur = Centaur('George', 'Palomino')

    centaur.lay_down()

    assert centaur.is_laying() == True
    assert centaur.sleep() != 'NO!'

def test_no_shooting_laying():
    centaur = Centaur('George', 'Palomino')

    centaur.lay_down()
    assert centaur.is_laying() == True

    assert centaur.shoot() != 'Twang!!!'
    assert centaur.shoot() == 'NO!'

def test_no_running_laying():
    centaur = Centaur('George', 'Palomino')

    centaur.lay_down()
    assert centaur.is_laying() == True

    assert centaur.run() != 'Clop clop clop clop!'
    assert centaur.run() == 'NO!'

def test_stands():
    centaur = Centaur('George', 'Palomino')

    centaur.lay_down()
    assert centaur.is_laying() == True

    centaur.stand_up()
    assert centaur.is_standing() == True

def test_sleeps():
    centaur = Centaur('George', 'Palomino')

    centaur.run()
    centaur.shoot()
    centaur.run()
    assert centaur.is_cranky() == True

    centaur.lay_down()
    centaur.sleep()
    assert centaur.is_cranky() == False

    centaur.stand_up()
    assert centaur.shoot() == 'Twang!!!'
    assert centaur.run() == 'Clop clop clop clop!'
