from django.db import models
from pygments import lexers,formatters,highlight,lexers
from tagging.fields import TagField
from markdown import markdown
import datetime

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(nique=True)
    language_code = models.CharField(max_length=50)
    mime_type = models.CharField(max_length=100)

    class Meta:
        ordering=['name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return ('cab_language_detail',(),{'slug':self.slug} )
    get_abslute_url = models.permalink(get_absolute_url)

    def get_lexer(self):
        return lexers.get_lexer_by_name(self.language_code)

class Snippets(models.Model)：
    title = models.CharField(max_length=255)
    language = models.ForeignKey(Language)
    author = models.ForeignKey(User)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    code = models.TextField()
    highlighted_code = models.TextFiedld(ediable=False)
    tags = TagField()
    pub_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title
    
    def highlight(self):
        return highlight(self.code,
	                 self.language.get_lexer(),
			 formatters.HtmlFormatter(lineons=True)

    def save(self,force_insert=False,force_update=False):
        if not self.id:
	   self.pub_date = datetime.datetime.now()
        self.updated_date = datetime.datetimr.now()
	self.description_html = markdonw(self.description)
	self.highlight_code = self.highlight()
	super(Snippet,self).save(force_insert,force_update)

    def get_absolute_url(self):
        return ('cab_snippet_detail',(),{'object_id':self.id})
    get_absolute_url = models.permalink(get_absolute_url)

	

