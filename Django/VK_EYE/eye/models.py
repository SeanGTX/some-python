from django.db import models

class Public(models.Model):

    name = models.CharField('name', max_length=50)
    surname = models.CharField('surname', max_length=50)
    VKLink = models.CharField('VKLink', max_length=50)

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getVKLink(self):
        return self.VKLink

    def getListOfRecord(self):
        return [self.name, self.surname, self.VKLink]

    def getChildClassesName():
        classes = [cls_name for cls_name, cls_obj in inspect.getmembers(sys.modules['Browser.models']) if
                   inspect.isclass(cls_obj)]
        classes.remove('Public')
        classes.remove('favorites')
        return classes

    class Meta:
        abstract = True
