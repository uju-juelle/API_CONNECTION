from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)


    class Meta:
      ordering = ["-date_posted"]  #this is for ordering in which instead of from old to new it will be from new to old
      verbose_name_plural = "News"


    def __str__(self):
        return self.title
    


  

class Movies(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  rating = models.CharField(max_length=100)


  def __str__(self):
     return self.title
