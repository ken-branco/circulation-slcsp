import pytest
from core.slcsp_by_zip import load_file_data
from core.slcsp_by_zip import calc_zip_rate

load_file_data()


@pytest.fixture(scope="module", params=[
    ("64148", ''),
    ("67118", 212.35),
    ("40813", ''),
    ("18229", ''),
    ("51012", ''),
    ("79168", ''),
    ("54923", 243.77),
    ("67651", 249.44),
    ("49448", 221.63),
    ("27702", ''),
    ("47387", 326.98),
    ("50014", 287.3),
])
def zip_rates(request):
    zip_code, rate = request.param
    yield zip_code, rate


def test_zip_codes(zip_rates):
    zip_code, rate = zip_rates
    zip_rate = calc_zip_rate(zip_code)
    assert zip_rate == rate
