
import pydantic
from modules.table.filter_variants import TableFilter

# Validators
class ComparisonStateItem(pydantic.BaseModel):
  name: str
  filter: TableFilter

class ComparisonState(pydantic.BaseModel):
  groups: list[ComparisonStateItem]

__all__ = [
  "ComparisonState",
]