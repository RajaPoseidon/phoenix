from typing import Optional

import strawberry
from strawberry import UNSET
from strawberry.relay import GlobalID
from strawberry.scalars import JSON

from .DatasetExampleInput import DatasetExampleInput


@strawberry.input
class AddExamplesToDatasetInput:
    dataset_id: GlobalID
    examples: list[DatasetExampleInput]
    dataset_version_description: Optional[str] = UNSET
    dataset_version_metadata: Optional[JSON] = UNSET
