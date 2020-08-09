import pytest
import requests
from bs4 import BeautifulSoup


@pytest.fixture
def MELI_xiaomi_data():
    return [' New Xiaomi Redmi Note 8 Azulado (3/32gb) Triple Cam 48mpx!! ',
            ' Xiaomi Note 8t 32gb128gb - Cuotas Sin Interés- C/ Gtia (25% Off) ',
            ' Izalo: Xiaomi Redmi Note 9 Pro 128gb + Mercadopago + Local! ',
            ' Xiaomi Note 9 Pro ',
            ' Xiaomi Redmi 9 - 4gb + 64gb - Dual Sim - Gris - Burzaco ',
            ' Xiaomi Redmi Note 8 Pro - 6gb + 64gb - Dual - Blanco Burzaco']


@pytest.fixture
def MELI_xiaomi_data_normalized():
    return ['redmi note 8 azulado 3 32gb',
            'note 8t 32gb 128gb',
            'redmi note 9 pro 128gb',
            'note 9 pro',
            'redmi 9 4gb 64gb dual gris',
            'redmi note 8 pro 6gb 64gb dual blanco']
