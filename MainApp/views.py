from django.shortcuts import render
from .models import Portfolio, PortfolioDetail, PortfolioSection, FactDetail, AboutDetail, SkillDetail, ResumeDetail, ResumeDetailList, FactSection, SkillSection, AboutSection, ResumeSection, SocialLink

def home(request, pk):
    my_portfolio = Portfolio.objects.get(uid=pk)
    context = {'portfolio': my_portfolio}
    return render(request, "index.html", context)

def detail(request, pk):
    my_portfolio_detail = PortfolioDetail.objects.get(id=pk)
    context = {'detail': my_portfolio_detail}
    return render(request, "portfolio-details.html", context)