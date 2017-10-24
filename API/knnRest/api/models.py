from django.db import models

class KnnList(models.Model):
    """ This class represents the knnList model.  """
    objectName = models.CharField(max_length=255)
    firstDetail = models.CharField(max_length=255)
    importantDetail = models.BooleanField(default=0)

    def __str__(self):
        """ Return a human readable representation of the model instance.  """
        return "{}".format(self.objectName)
