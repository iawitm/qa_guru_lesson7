import zipfile
import pytest, os

RESOURCES_DIR = os.path.abspath('resources')
RAW_FILES_DIR = os.path.join(RESOURCES_DIR, 'raw_files')
ZIP_FILES_DIR = os.path.join(RESOURCES_DIR, 'zip_files')

@pytest.fixture(scope="module")
def create_zip_dir():
    if not os.path.isdir(ZIP_FILES_DIR):
        os.mkdir(ZIP_FILES_DIR)

@pytest.fixture(scope="module")
def create_zip(create_zip_dir):
    zip_file_name = f'{ZIP_FILES_DIR}/ZIP_example.zip'
    files = os.listdir(RAW_FILES_DIR)

    if not os.path.isfile(zip_file_name):
        with zipfile.ZipFile(zip_file_name, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file:
            for file in files:
                file_path = os.path.join(RAW_FILES_DIR, file)
                zip_file.write(file_path, file)
    yield zip_file_name

    if os.path.isfile(zip_file_name):
        os.remove(zip_file_name)
