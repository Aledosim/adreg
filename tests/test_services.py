import pytest

from schema import SchemaError
import src

from src.services import add_ad

class TestAddAd:
    # TODO
    # test add_ad success
    def test_passes_correct_values(self, mocker):
        mocker.patch('src.services.add_reg')

        add_ad(
            name='test name',
            client='test client',
            start='5-4-2021',
            end='7-5-2021',
            investment=500
        )

        src.services.add_reg.assert_called_with(
            name='test name',
            client='test client',
            start='5-4-2021',
            end='7-5-2021',
            investment=500
        )

    def test_name_must_be_str(self):
        with pytest.raises(SchemaError) as exception:
            add_ad(
                name=31,
                client='test client',
                start='5-4-2021',
                end='7-5-2021',
                investment=500
            )

        assert 'name must be str' in [err for err in exception.value.errors]

    def test_client_is_str(self):
        with pytest.raises(SchemaError) as exception:
            add_ad(
                name='test name',
                client=31,
                start='5-4-2021',
                end='7-5-2021',
                investment=500
            )

        assert 'client must be str' in [err for err in exception.value.errors]

    def test_start_is_formated_str(self):
        with pytest.raises(SchemaError) as exception:
            add_ad(
                name='test name',
                client='test client',
                start=31,
                end='7-5-2021',
                investment=500
            )

        assert 'start date must be str' in [err for err in exception.value.errors]

        with pytest.raises(SchemaError) as exception:
            add_ad(
                name='test name',
                client='test client',
                start='',
                end='7-5-2021',
                investment=500
            )

        assert 'start date must be in the format dd-mm-yyyy' in [err for err in exception.value.errors]

    def test_end_is_formated_str(self):
        with pytest.raises(SchemaError) as exception:
            add_ad(
                name='test name',
                client='test client',
                start='5-4-2021',
                end=31,
                investment=500
            )

        print(exception.value.autos)
        assert 'end date must be str' in [err for err in exception.value.errors]

        with pytest.raises(SchemaError) as exception:
            add_ad(
                name='test name',
                client='test client',
                start='5-4-2021',
                end='',
                investment=500
            )

        assert 'end date must be in the format dd-mm-yyyy' in [err for err in exception.value.errors]

    def test_investment_is_positive_int(self):
        with pytest.raises(SchemaError) as exception:
            add_ad(
                name='test name',
                client='test client',
                start='5-4-2021',
                end='7-5-2021',
                investment='500'
            )

        assert 'investment must be int' in [err for err in exception.value.errors]

        with pytest.raises(SchemaError) as exception:
            add_ad(
                name='test name',
                client='test client',
                start='5-4-2021',
                end='7-5-2021',
                investment=-500
            )

        assert 'investment must be positive' in [err for err in exception.value.errors]

    def test_add_ad_without_args(self):
        with pytest.raises(SchemaError):
            add_ad()
