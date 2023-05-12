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
class SubjectLessons:
    subject: str
    lesssons: List[Lesson]

@dataclass
class LessonTuple:
    time: str
    subjectsLessons: List[SubjectLessons]


@dataclass
class Raspisanie:
    date: str
    subjects: List[str]
    lessonsToTime: List[LessonTuple]

    # {
    #   date: str,
    #   subjects: [str],
    #   lessonsToTime: [
    #       {
    #            time: str,
    #            subjustsLessons: [
    #                {
    #                    subject: str,
    #                    lessons: [
    #                        {
    #                            discipline: str
    #                            workType: str
    #                            auditoriumNumber: str
    #                            vmestimost: int
    #                            prepod: str
    #                        }
    #                    ]
    #                }
    #            ]
    #       }
    #    ]
