import pytest

from src.libs.calculator import initial_views, click_count, share_count, update_views, Views, calculator


class TestCalculator:

    @pytest.mark.parametrize(
        'investment,views,clicks,shares',
        [
            (1, 0, 0, 0),
            (3, 0, 0, 0),
            (4, 1, 0, 0),
            (10, 3, 0, 0),
            (100, 30, 3, 0),
            (196, 58, 6, 0),
            (197, 99, 11, 1),
            (227, 108, 12, 1),
            (240, 112, 13, 1),
            (256, 116, 13, 1),
            (257, 157, 18, 2),
            (289, 166, 19, 2),
            (290, 207, 24, 3),
            (349, 224, 26, 3),
            (350, 225, 27, 4),
            (386, 235, 28, 4),
            (387, 236, 28, 4),
            (390, 277, 33, 4),
            (1000, 740, 88, 13),
            (2000, 1520, 182, 27),
            (5000, 3900, 468, 70),
            (10000, 7800, 936, 140),
            (50000, 39160, 4699, 704),
            (100000, 78320, 9398, 1409),
        ]
    )
    def test_calculator(self, investment, views, clicks, shares):
        result = calculator(investment)

        assert (views, clicks, shares) == result


class TestInitialViews:

    @pytest.mark.parametrize(
        'input_value,expected',
        [
            (0, 0),
            (3, 0),
            (4, 1),
            (10, 3),
            (100, 30),
            (250, 75),
            (400, 120),
            (556, 166),
            (750, 225),
            (1000, 300),
            (10000, 3000),
        ]
    )
    def test_initial_views(self, input_value, expected):
        result = initial_views(input_value)
        assert result == expected


class TestClickCount:

    @pytest.mark.parametrize(
        'input_value,expected',
        [
            (8, 0),
            (9, 1),
            (16, 1),
            (17, 2),
            (25, 3),
            (33, 3),
            (34, 4),
            (104, 12),
            (235, 28),
            (300, 36),
            (500, 60),
            (660, 79),
            (740, 88),
        ]
    )
    def test_click_count(self, input_value, expected):
        result = click_count(input_value)
        assert result == expected


class TestShareCount:

    @pytest.mark.parametrize(
        'input_value,expected',
        [
            (6, 0),
            (7, 1),
            (13, 1),
            (14, 2),
            (20, 3),
            (26, 3),
            (27, 4),
        ]
    )
    def test_share_count(self, input_value, expected):
        result = share_count(input_value)
        assert result == expected


class TestUpdateViews:

    def test_same_views(self):
        views = Views()
        views.value = 58
        views.isChanged = False
        views.shares = 0

        update_views(views)

        assert views.value == 58
        assert views.isChanged is False
        assert views.shares == 0

    def test_update_views_one_time(self):
        views = Views()
        views.value = 59
        views.isChanged = False
        views.shares = 0

        update_views(views)

        assert views.value == 99
        assert views.isChanged is True
        assert views.shares == 1

        update_views(views)

        assert views.value == 99
        assert views.isChanged is False
        assert views.shares == 1

    def test_update_views_two_times(self):
        views = Views()
        views.value = 77
        views.isChanged = False
        views.shares = 0

        update_views(views)

        assert views.value == 117
        assert views.isChanged is True
        assert views.shares == 1

        update_views(views)

        assert views.value == 157
        assert views.isChanged is True
        assert views.shares == 2

        update_views(views)

        assert views.value == 157
        assert views.isChanged is False
        assert views.shares == 2

    def test_update_views_three_times(self):
        views = Views()
        views.value = 105
        views.isChanged = False
        views.shares = 0
        views.clicks = 0

        update_views(views)

        assert views.value == 145
        assert views.isChanged is True
        assert views.shares == 1
        assert views.clicks == 12

        update_views(views)

        assert views.value == 185
        assert views.isChanged is True
        assert views.shares == 2
        assert views.clicks == 17

        update_views(views)

        assert views.value == 225
        assert views.isChanged is True
        assert views.shares == 3
        assert views.clicks == 22
