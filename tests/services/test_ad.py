import pytest

from schema import SchemaError
from datetime import date
import src

from src.services.ad import Ad

@pytest.fixture(autouse=True)
def ad():
    return Ad()


class TestAdAdd:
    def test_passes_correct_values(self, mocker, ad):
        mocker.patch('src.services.ad.add_reg')

        ad.add(
            name='test name',
            client='test client',
            start='5-4-2021',
            end='7-5-2021',
            investment=500
        )

        src.services.ad.add_reg.assert_called_with(
            name='test name',
            client='test client',
            start=date(2021, 4, 5),
            end=date(2021, 5, 7),
            investment=500
        )

    def test_name_must_be_str(self, ad):
        with pytest.raises(SchemaError) as exception:
            ad.add(
                name=31,
                client='test client',
                start='5-4-2021',
                end='7-5-2021',
                investment=500
            )

        assert 'name must be str' in [err for err in exception.value.errors]

    def test_client_is_str(self, ad):
        with pytest.raises(SchemaError) as exception:
            ad.add(
                name='test name',
                client=31,
                start='5-4-2021',
                end='7-5-2021',
                investment=500
            )

        assert 'client must be str' in [err for err in exception.value.errors]

    def test_start_is_formated_str(self, ad):
        with pytest.raises(SchemaError) as exception:
            ad.add(
                name='test name',
                client='test client',
                start=31,
                end='7-5-2021',
                investment=500
            )

        assert 'start date must be str' in [err for err in exception.value.errors]

        with pytest.raises(SchemaError) as exception:
            ad.add(
                name='test name',
                client='test client',
                start='',
                end='7-5-2021',
                investment=500
            )

        assert 'start date must be in the format dd-mm-yyyy' in [err for err in exception.value.errors]

    def test_end_is_formated_str(self, ad):
        with pytest.raises(SchemaError) as exception:
            ad.add(
                name='test name',
                client='test client',
                start='5-4-2021',
                end=31,
                investment=500
            )

        print(exception.value.autos)
        assert 'end date must be str' in [err for err in exception.value.errors]

        with pytest.raises(SchemaError) as exception:
            ad.add(
                name='test name',
                client='test client',
                start='5-4-2021',
                end='',
                investment=500
            )

        assert 'end date must be in the format dd-mm-yyyy' in [err for err in exception.value.errors]

    def test_investment_is_positive_int(self, ad):
        with pytest.raises(SchemaError) as exception:
            ad.add(
                name='test name',
                client='test client',
                start='5-4-2021',
                end='7-5-2021',
                investment='500'
            )

        assert 'investment must be int' in [err for err in exception.value.errors]

        with pytest.raises(SchemaError) as exception:
            ad.add(
                name='test name',
                client='test client',
                start='5-4-2021',
                end='7-5-2021',
                investment=-500
            )

        assert 'investment must be positive' in [err for err in exception.value.errors]

    def test_add_without_args(self, ad):
        with pytest.raises(SchemaError):
            ad.add()
