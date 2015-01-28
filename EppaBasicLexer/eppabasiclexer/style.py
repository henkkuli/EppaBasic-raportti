from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic

class EppaBasicStyle(Style):
    default_style = ""
	
    styles = {
        Comment:                '#133',
        Keyword:                '#0069EF',
        Name:                   '#111221',
		Operator:				'#FF308F',
        String:                 '#58C554',
		Number:					'#58C554'
    }