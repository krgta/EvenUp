from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.common import SuccessResponse
from schemas.dashboard import DashboardResponse
from repository.expense_repository import ExpenseRepository
from repository.group_member_repository import GroupMemberRepository
from repository.group_repository import GroupRepository


async def sync_user_expenses(user_id: UUID, group_id: UUID, db: AsyncSession) -> SuccessResponse[DashboardResponse]:
      expense_repo = ExpenseRepository(db)
      group_repo = GroupRepository(db)
      member_repo = GroupMemberRepository(db)

      if not await member_repo.is_member(user_id, group_id):
            raise HTTPException(status_code=403, detail="Member is not authorised")

      group = await group_repo.get_by_id(group_id)
      if not group:
            raise HTTPException(status_code=404, detail="Group not found")
      
      expenses_paid_by_user = await expense_repo.get_expense_paid_by_user(group_id, user_id, 20)
      
      return