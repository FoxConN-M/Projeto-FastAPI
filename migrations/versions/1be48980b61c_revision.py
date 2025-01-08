"""revision

Revision ID: 1be48980b61c
Revises: e35f4cd93e67
Create Date: 2025-01-08 19:05:06.740365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1be48980b61c'
down_revision: Union[str, None] = 'e35f4cd93e67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
