from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, Integer, Boolean

class Base(DeclarativeBase):
    ...

class Project(Base):
    __tablename__ = "project"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60))
    description: Mapped[Optional[str]] = mapped_column(String(30))
    created_at= mapped_column(DateTime)
    project_id: Mapped[List["Task"]] = relationship(
        back_populates="project", cascade="all, delete-orphan"
    )

class Task(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(60))
    priority: Mapped[int] = mapped_column(Integer)
    completed: Mapped[bool] = mapped_column(Boolean) # (boolean, default False)
    due_date: Mapped[Optional[DateTime]] = mapped_column(DateTime)  # (date, optional)

    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"))