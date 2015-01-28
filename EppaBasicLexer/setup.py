from setuptools import setup, find_packages
 
setup (
	name='eppabasiclexer',
	packages=find_packages(),
	entry_points =
	"""
	[pygments.lexers]
	eppabasiclexer = eppabasiclexer.lexer:EppaBasicLexer
	""",
)