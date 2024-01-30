from django.db import models
from django.utils.html import mark_safe
from django.utils import timezone

class Portfolio(models.Model):
    uid = models.URLField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="thumbnail/img/portfolios/")
    social_links = models.ManyToManyField("SocialLink")
    about = models.ForeignKey("AboutSection", on_delete = models.CASCADE)
    facts = models.ForeignKey("FactSection", on_delete = models.CASCADE)
    skills = models.ForeignKey("SkillSection", on_delete = models.CASCADE)
    resume = models.ForeignKey("ResumeSection", on_delete = models.CASCADE)
    portfolio = models.ForeignKey("PortfolioSection", on_delete = models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="thumbnail/img/portfolios/about/")
    subtitle = models.CharField(max_length=255)
    subdescription = models.TextField()
    detail = models.ManyToManyField("AboutDetail")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AboutDetail(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class FactSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    detail = models.ManyToManyField("FactDetail")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class FactDetail(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    rate = models.IntegerField(max_length=255)
    icon = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class SkillSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    detail = models.ManyToManyField("SkillDetail")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class SkillDetail(models.Model):
    title = models.CharField(max_length=255)
    percentage_rate = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ResumeSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    detail = models.ManyToManyField("ResumeDetail")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ResumeDetail(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    detail_list = models.ManyToManyField("ResumeDetailList")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class ResumeDetailList(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.description


class PortfolioSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    detail = models.ManyToManyField("PortfolioDetail")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PortfolioDetail(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    project_date = models.DateTimeField(default=timezone.now)
    project_url = models.URLField()
    image = models.ImageField(upload_to="thumbnail/img/portfolios/portfolio/")
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class SocialLink(models.Model):
    icon = models.CharField(max_length=255)
    url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]


    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
