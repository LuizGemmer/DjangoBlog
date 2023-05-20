from django.db import models



# Create your models here.
class Media(models.Model):
    file_path = models.FileField("media", upload_to="post_media/%y/%m/%d/")
    type = models.CharField(max_length=40)

    def __str__(self):
        return self.file_path.name
    

class Post(models.Model):
    text = models.TextField("post")
    media = models.ManyToManyField(Media, blank=True)

    date_posted = models.DateTimeField("posted", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("last modified", auto_now=True, editable=False)


    in_response_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    #author = models.ForeignKey()

    def __str__(self):
        return f"{self.text[:20]} by not implemented"



