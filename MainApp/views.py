from django.shortcuts import render
from .models import Portfolio, PortfolioDetail, PortfolioSection, AboutDetail, SkillDetail, ResumeDetail, ResumeDetailList, FactSection, SkillSection, AboutSection, ResumeSection, SocialLink, PortfolioCategory

def home(request, pk):
    my_portfolio = Portfolio.objects.get(id=pk)
    portfolio_category = PortfolioCategory.objects.filter()
    context = {'portfolio': my_portfolio,
               'category': portfolio_category}
    return render(request, "ProjectsApi/index.html", context)

def detail(request, pk):
    my_portfolio_detail = PortfolioDetail.objects.get(id=pk)
    context = {'detail': my_portfolio_detail}
    return render(request, "ProjectsApi/portfolio-details.html", context)