from django.db import models

class Room(models.Model):
    # 강의 테이블 구현
    lecture_id = models.IntegerField(primary_key=True)      # 강의 ID
    lecture_name = models.CharField(max_length=200)         # 강의 이름
    professor_id = models.IntegerField()                    # 강사 ID
    is_online = models.BooleanField()                      # 온오프라인 여부
    prerequisite = models.CharField(max_length=200, null=True, blank=True)  # 사전 강의

    def __str__(self): # 강의 이름을 문자열로 반환
        return f"[{self.lecture_id}] {self.lecture_name}" # 강의 ID와 강의 이름을 함께 반환