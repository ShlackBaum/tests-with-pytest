import pytest
from yandex_folder_testing import create_folder, check_folder_created

folders_names = ["TestFolder1", "TestFolder1", "TestFolder2"]

FIXTURE=[(folders_names[0], 201), (folders_names[1], 409), (folders_names[2], 201)]
FIXTURE2=[(folders_names[0], 1),
          (folders_names[1], 1),
          (folders_names[2], 1),
          ("RandomFileOrFolderName", 0)]

@pytest.mark.parametrize("folder_name, result", FIXTURE)
def test_create_folder(folder_name, result):
    assert create_folder(folder_name) == result

@pytest.mark.parametrize("folder_name, result", FIXTURE2)
def test_check_folder_created(folder_name, result):
    assert check_folder_created(folder_name) == result