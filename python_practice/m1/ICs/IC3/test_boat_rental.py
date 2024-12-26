import pytest
from boat import Boat
from renter import Renter
from dock import Dock

def test_itr_1():
    dock = Dock('The Rowing Dock', 3)

    kayak1 = Boat('kayak', 20)
    patrick = Renter('Patrick Star', '4242424242424242')
    kayak1 = Boat('kayak', 20)

    assert kayak1.type == 'kayak'
    assert kayak1.price_per_hour == 20
    assert kayak1.hours_rented == 0
    
    for _ in range(3):
        kayak1.add_hour()
    assert kayak1.hours_rented == 3 
    
    assert patrick.name == 'Patrick Star'
    assert patrick.credit_card_number == '4242424242424242'

def test_itr_2():
    dock = Dock('The Rowing Dock', 3)

    kayak1 = Boat('kayak', 20)
    kayak2 = Boat('kayak', 20)
    board = Boat('stand_up_paddle_board', 15)

    patrick = Renter('Patrick Star', '4242424242424242')
    eugene = Renter('Eugene Krabs', '1313131313131313')

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
        kayak1: {'renter': patrick, 'rented': True},
        kayak2: {'renter': patrick, 'rented': True},
        board: {'renter': eugene, 'rented': True}
    }

def test_itr_3():   
    dock = Dock('The Rowing Dock', 3)

    kayak1 = Boat('kayak', 20)
    kayak2 = Boat('kayak', 20)
    board = Boat('stand_up_paddle_board', 15)

    patrick = Renter('Patrick Star', '4242424242424242')
    eugene = Renter('Eugene Krabs', '1313131313131313')

    dock = Dock('The Rowing Dock', 3)

    kayak1 = Boat('kayak', 20)
    kayak2 = Boat('kayak', 20)
    board = Boat('stand_up_paddle_board', 15)

    patrick = Renter('Patrick Star', '4242424242424242')
    eugene = Renter('Eugene Krabs', '1313131313131313')

    dock.rent(kayak1, patrick)
    dock.rent(kayak1, patrick)
    
    dock.rent(board, eugene)
    
    dock.rent(kayak2, eugene)
    dock.rent(kayak2, eugene)
    dock.rent(kayak2, eugene)
    dock.rent(kayak2, eugene)
    
    assert dock.charge(kayak1) == {'card_number': patrick.credit_card_number, 'amount': 40}
    assert dock.charge(board) == {'card_number': eugene.credit_card_number, 'amount': 15}
    assert dock.charge(kayak2) == {'card_number': eugene.credit_card_number, 'amount': 60}

def test_itr_4():
    dock = Dock('The Rowing Dock', 3)

    kayak1 = Boat('kayak', 20)
    kayak2 = Boat('kayak', 20)
    board = Boat('stand_up_paddle_board', 15)

    patrick = Renter('Patrick Star', '4242424242424242')
    eugene = Renter('Eugene Krabs', '1313131313131313')
    
    dock.rent(kayak1, patrick)
    
    dock.rent(board, eugene)
    dock.rent(board, eugene)
    
    dock.rent(kayak2, eugene)
    dock.rent(kayak2, eugene)
    dock.rent(kayak2, eugene)
    
    assert dock.rental_log == {
        kayak1: {'renter': patrick, 'rented': True},
        kayak2: {'renter': eugene, 'rented': True},
        board: {'renter': eugene, 'rented': True}
    }

    dock.return_boat(kayak1)

    assert dock.rental_log == {
        kayak1: {'renter': patrick, 'rented': False},
        kayak2: {'renter': eugene, 'rented': True},
        board: {'renter': eugene, 'rented': True}
    }
    
    assert kayak1.hours_rented == 1
    assert board.hours_rented == 2
    assert kayak2.hours_rented == 3
    
    dock.log_hour()