from dataclasses import dataclass
from typing import List


@dataclass
class Lesson:
    discipline: str
    workType: str
    auditoriumNumber: str  # 8-227
    vmestimost: int
    prepod: str


@dataclass
class SubjectTuple:
    subject: str
    lessons: List[Lesson]


@dataclass
class LessonTuple:
    time: str
    lesson: SubjectTuple


@dataclass
class Raspisanie:
    date: str
    lessonsToTime: List[LessonTuple]
