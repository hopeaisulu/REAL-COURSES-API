from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Category(models.Model):
	name = models.TextField()
	imgpath = models.TextField()


class Course (models.Model):
	name = models.TextField()
	description = models.TextField()
	category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
	logo = models.TextField()
	


class Branch (models.Model):
	latitude = models.TextField()
	longitude = models.TextField()
	address = models.TextField()
	course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE)


MAKE_CHOICE = (
	(1, 'PHONE'),
	(2, 'FACEBOOK'),
	(3, 'EMAIL'),
)

class Contact(models.Model):
	type = models.IntegerField(choices=MAKE_CHOICE)
	value = models.TextField()
	course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE)




    # class Meta:
    #     ordering = ('created',)
