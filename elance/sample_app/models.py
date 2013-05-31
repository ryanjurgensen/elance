from django.db import models

ARTICLE_TYPES = (
	('static', 'Static'),
	('blog', 'blog'),
)

class ArticleUser(AbstractUser):
	stripe_id = models.CharField(max_length=255)
	subscribed = models.BooleanField(default=False)

class Article(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField()
	article_type = models.CharField(max_length=255, choices=ARTICLE_TYPES)
	positive_ratings = models.ManyToManyField(ArticleUser, related_name='positive_ratings')
	negative_ratings = models.ManyToManyField(ArticleUser, related_name='negative_ratings')

	@staticmethod
	def get_top_articles_by_type(self, type):
		'''
		Given a string type, like "blog", return the top 5 articles with the most positive ratings.
		'''
		pass
