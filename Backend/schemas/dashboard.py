from decimal import Decimal

from pydantic import BaseModel

from schemas.expense_split import ExpenseOweResponse, ExpensePaidResponse
from schemas.groups import GroupResponse
from schemas.user import UserResponse


class ExpenseDashboardResponse(BaseModel):
    paid_by: list[ExpensePaidResponse]
    owed: list[ExpenseOweResponse]


class DashboardResponse(BaseModel):
    user: UserResponse
    groups: list[GroupResponse]
    expenses: list[ExpenseDashboardResponse]
    total_expense: Decimal
    total_owed: Decimal
