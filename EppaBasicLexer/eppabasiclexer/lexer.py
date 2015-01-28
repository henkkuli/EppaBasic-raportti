import re

from pygments.lexer import RegexLexer, bygroups, default, words, include
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Generic
            
class EppaBasicLexer(RegexLexer):
    name = 'EppaBasic'
    aliases = ['eb']
    filenames = ['*.eb']
    mimetypes = ['text/eb']
	
    flags = re.IGNORECASE

    tokens = {
        'root': [
        #    include('baselevelstatement')
            (r'\'[^\n]*', Comment),
            (r'<>|<=?|>=?|=|\+|-|\*|\/|\\|\^|&|MOD\b|AND\b|OR\b|XOR\b|NOT\b', Operator),
            (r'-?\d*\.?\d+', Number),
            (r'"(.*?)"', String),
            (r',', Punctuation),
            (r'\(|\)', Punctuation),
			(r'\s', Text.Whitespace),
            
			(r'for|to|step|next|do|loop|until|while|if|then|else\s*if|else|end\s*if|dim|as|function|return|end\s*function|sub|end\s*sub', Keyword.Reserved),
			(r'integer|number|double|string', Name.Type),
			
            (r'[_\w][_\w\d]*', Name)
        ]
    }