from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):       # created_at : 언제 만들었는지 표시
    list_display = ("title", "created_at") #어드민 페이지에서 보여줄 필드
    search_fields = ("title", "content") # 제목이나 내용 검색 필드
    list_filter = ("created_at",) # 필터링 기능 필드
    date_hierarchy = "created_at" # 날짜 계층 구조 표시
    ordering = ("-created_at",) # 정렬 순서 표시