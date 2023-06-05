import json

import pytest

pytestmark = pytest.mark.django_db


class TestCompanyEndPoints:
    endpoint = "/api/companies/"

    def test_company_get(self, company_factory, api_client):
        company_factory.create_batch(3)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3
