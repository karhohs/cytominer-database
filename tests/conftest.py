import pytest


def pytest_addoption(parser):
    parser.addoption("--dataset", action="store", help="dataset to test")


def pytest_generate_tests(metafunc):
    if "dataset" in metafunc.fixturenames:
        if metafunc.config.option.dataset is None:
            metafunc.parametrize("dataset", ["htqc", "cellpainting", "qc"], indirect=True)
        else:
            assert metafunc.config.option.dataset in ["htqc", "cellpainting", "qc"]

            metafunc.parametrize("dataset", [metafunc.config.option.dataset], indirect=True)


@pytest.fixture
def cellpainting():
    return {
        "config": "config.ini",
        "data_dir": "tests/data_b",
        "image_csv": "Image.csv",
        "ingest": [
            {
                "ncols": 586,
                "nrows": 40,
                "table": "Cells"
            },
            {
                "ncols": 572,
                "nrows": 40,
                "table": "Cytoplasm"
            },
            {
                "ncols": 6,
                "nrows": 4,
                "table": "image"
            },
            {
                "ncols": 595,
                "nrows": 40,
                "table": "Nuclei"
            }
        ],
        "munge": False
    }

@pytest.fixture
def htqc():
    return {
        "config": "config.ini",
        "data_dir": "tests/data_a",
        "munged_dir": "tests/data_a_munged",
        "image_csv": "image.csv",
        "ingest": [
            {
                "ncols": 294,
                "nrows": 40,
                "table": "Cells"
            },
            {
                "ncols": 279,
                "nrows": 40,
                "table": "Cytoplasm"
            },
            {
                "ncols": 229,
                "nrows": 8,
                "table": "image"
            },
            {
                "ncols": 287,
                "nrows": 40,
                "table": "Nuclei"
            }
        ],
        "munge": True
    }


@pytest.fixture
def qc():
    return {
        "config": None,
        "data_dir": "tests/data_c",
        "image_csv": "Image.csv",
        "ingest": [
            {
                "nrows": 8,
                "ncols": 229,
                "table": "Image"
            }
        ],
        "munge": True
    }


@pytest.fixture
def dataset(request):
    if request.param == "htqc":
        return htqc()

    if request.param == "cellpainting":
        return cellpainting()

    if request.param == "qc":
        return qc()

    raise ValueError("No such dataset: {}".format(request.param))
