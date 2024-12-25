import pytest
from boat import Boat
from renter import Renter
from dock import Dock

def test_itr_1():
    kayak = Boat('kayak', 20)
    renter = Renter('Patrick Star', '4242424242424242')
    
    assert kayak.type == 'kayak'
    assert kayak.price_per_hour == 20
    assert kayak.hours_rented == 0
    
    for _ in range(3):
        kayak.add_hour()
    assert kayak.hours_rented == 3 
    
    assert renter.name == 'Patrick Star'
    assert renter.credit_card_number == '4242424242424242'

def test_itr_2():
    dock = Dock('The Rowing Dock', 3)
    
    kayak1 = Boat('kayak', 20)
    kayak2 = Boat('kayak', 20)
    board = Boat('stand_up_paddle_board', 15)
    
    patrick = Renter('Patrick Star', '4242424242424242')
    eugene = Renter('Eugene Krabs', '1313131313131313')

    assert dock.name == 'The Rowing Dock'
    assert dock.max_rental_time == 3
    
    dock.rent(kayak1, patrick)
    dock.rent(kayak2, patrick)
    dock.rent(board, eugene)
    
    assert dock.rental_log == {
        kayak1: patrick,
        kayak2: patrick,
        board: eugene
    }

def test_itr_3():
    dock = Dock('The Rowing Dock', 3)
    
    kayak1 = Boat('kayak', 20)
    # kayak2 = Boat('kayak', 20)
    # board = Boat('stand_up_paddle_board', 15)
    
    patrick = Renter('Patrick Star', '4242424242424242')
    # eugene = Renter('Eugene Krabs', '1313131313131313')
    
    dock.rent(kayak1, patrick)
    # dock.rent(kayak1, patrick)
    # dock.rent(board, eugene)
    
    # assert dock.charge(kayak1) == {patrick.credit_card_number: 20}