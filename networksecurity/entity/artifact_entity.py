from dataclasses import dataclass

@dataclass
# @dataclass creates the __init__() for you automatically.
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str

# print(dataingestionartifact)

# because DataIngestionArtifact is a dataclass, Python automatically gives it a readable __repr__().

# For example, if you created it like this:

# dataingestionartifact = DataIngestionArtifact(
#     trained_file_path="train.csv",
#     test_file_path="test.csv"
# )

# print(dataingestionartifact)

# it prints:

# DataIngestionArtifact(trained_file_path='train.csv', test_file_path='test.csv')

# That's exactly why you previously got:

# DataIngestionArtifact(trained_file_path='Artifacts\\08_09_2026_23_35_13\\data_ingestion\\ingested\\train.csv',
#                       test_file_path='Artifacts\\08_09_2026_23_35_13\\data_ingestion\\ingested\\test.csv')



@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str