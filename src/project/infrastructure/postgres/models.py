from sqlalchemy.orm import Mapped, mapped_column
from project.infrastructure.postgres.database import Base

class Meals(Base):
    __tablename__ = "meals"

    id_meal: Mapped[str] = mapped_column(primary_key=True)
    count_ingredients: Mapped[int] = mapped_column(nullable=False)
    gruppa: Mapped[str] = mapped_column(nullable=False)
    season: Mapped[str] = mapped_column(nullable=False)
    weigth: Mapped[int] = mapped_column(nullable=False)
    count_pors: Mapped[int] = mapped_column(nullable=False)
    prepering_time: Mapped[int] = mapped_column(nullable=False)