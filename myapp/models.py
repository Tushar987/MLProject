# encoding: utf-8
from django.db import models


#.................
class Music(models.Model):
    """
    Model to upload music file

    """
    
    file = models.FileField(upload_to="audio")
    slug = models.SlugField(max_length=50, blank=True)

    def __str__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(Music, self).save(*args, **kwargs)
        

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file.delete(False)
        super(Music, self).delete(*args, **kwargs)
