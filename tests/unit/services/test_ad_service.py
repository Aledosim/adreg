import pytest

from schema import SchemaError
from datetime import date
import src

from src.services.adservice import AdService


class TestAdAdd:
    def test_passes_correct_values(self, ad_input, mocker):
        mocker.patch('src.services.adservice.AdReg')
        mocker.patch('src.services.adservice.AdInputDTO')

        service = AdService()
        service.add(
            name=ad_input.name,
            client=ad_input.client,
            start='5-4-2021',
            end='7-5-2021',
            investment=ad_input.investment,
        )

        ad_dto = src.services.adservice.AdInputDTO
        ad_dto.assert_called_once_with(
            name=ad_input.name,
            client=ad_input.client,
            start=date(2021, 4, 5),
            end=date(2021, 5, 7),
            investment=ad_input.investment,
        )

        adreg = src.services.adservice.AdReg()
        adreg.create_adreg.assert_called_once_with(ad_dto())

    def test_name_is_str(self, ad_input):
        service = AdService()

        with pytest.raises(SchemaError) as exception:
            service.add(
                name=31,
                client=ad_input.client,
                start=ad_input.start,
                end=ad_input.end,
                investment=ad_input.investment,
            )

        assert 'name must be str' in [err for err in exception.value.errors]

    def test_client_is_str(self, ad_input):
        service = AdService()

        with pytest.raises(SchemaError) as exception:
            service.add(
                name=ad_input.name,
                client=31,
                start=ad_input.start,
                end=ad_input.end,
                investment=ad_input.investment,
            )

        assert 'client must be str' in [err for err in exception.value.errors]

    def test_start_is_formated_str(self, ad_input):
        service = AdService()

        with pytest.raises(SchemaError) as exception:
            service.add(
                name=ad_input.name,
                client=ad_input.client,
                start=31,
                end=ad_input.end,
                investment=ad_input.investment,
            )

        assert 'start date must be str' in [err for err in exception.value.errors]

        with pytest.raises(SchemaError) as exception:
            service.add(
                name=ad_input.name,
                client=ad_input.client,
                start='',
                end=ad_input.end,
                investment=ad_input.investment,
            )

        assert 'start date must be in the format dd-mm-yyyy' in [err for err in exception.value.errors]

    def test_end_is_formated_str(self, ad_input):
        service = AdService()

        with pytest.raises(SchemaError) as exception:
            service.add(
                name=ad_input.name,
                client=ad_input.client,
                start=ad_input.start,
                end=31,
                investment=ad_input.investment,
            )

        print(exception.value.autos)
        assert 'end date must be str' in [err for err in exception.value.errors]

        with pytest.raises(SchemaError) as exception:
            service.add(
                name=ad_input.name,
                client=ad_input.client,
                start=ad_input.start,
                end='',
                investment=ad_input.investment,
            )

        assert 'end date must be in the format dd-mm-yyyy' in [err for err in exception.value.errors]

    def test_investment_is_positive_int(self, ad_input):
        service = AdService()

        with pytest.raises(SchemaError) as exception:
            service.add(
                name=ad_input.name,
                client=ad_input.client,
                start=ad_input.start,
                end=ad_input.end,
                investment='500',
            )

        assert 'investment must be int' in [err for err in exception.value.errors]

        with pytest.raises(SchemaError) as exception:
            service.add(
                name=ad_input.name,
                client=ad_input.client,
                start=ad_input.start,
                end=ad_input.end,
                investment=-500,
            )

        assert 'investment must be positive' in [err for err in exception.value.errors]

    def test_add_without_args(self):
        service = AdService()
        with pytest.raises(SchemaError):
            service.add()
