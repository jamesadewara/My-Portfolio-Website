from django.contrib import admin
from .models import Portfolio, PortfolioDetail, PortfolioSection, FactDetail, AboutDetail, SkillDetail, ResumeDetail, ResumeDetailList, FactSection, SkillSection, AboutSection, ResumeSection, SocialLink

admin.site.register(Portfolio)
admin.site.register(PortfolioDetail)
admin.site.register(PortfolioSection)
admin.site.register(FactDetail)
admin.site.register(AboutDetail)
admin.site.register(SkillDetail)
admin.site.register(ResumeDetail)
admin.site.register(ResumeDetailList)
admin.site.register(FactSection)
admin.site.register(SkillSection)
admin.site.register(AboutSection)
admin.site.register(ResumeSection)
admin.site.register(SocialLink)

