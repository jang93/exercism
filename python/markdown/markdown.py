import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        line = replace_headers(line)
        line, in_list, in_list_append = replace_list(line, in_list, in_list_append)
        line = replace_paragraph(line)
        line = replace_bold(line)
        line = replace_italic(line)
        if in_list_append:
            line = f'</ul>{line}'
        res += line
    if in_list:
        res += '</ul>'
    return res

def replace_headers(line):
    m = re.match('(#+) (.*)', line)
    if m:
        count = len(m.group(1))
        line = f'<h{count}>{line[count+1:]}</h{count}>'
    return line

def replace_list(line, in_list, in_list_append):
    m = re.match(r'\* (.*)', line)
    if m:
        content = m.group(1)
        if not in_list:
            in_list = True
            line = f'<ul><li>{content}</li>'
        else:
            line = f'<li>{content}</li>'
    else:
        if in_list:
            in_list_append = True
            in_list = False
    return line, in_list, in_list_append

def replace_paragraph(line):
    m = re.match('<h|<ul|<p|<li', line)
    if not m:
        line = f'<p>{line}</p>'
    return line

def replace_bold(line):
    m = re.match('(.*)__(.*)__(.*)', line)
    if m:
        line = f'{m.group(1)}<strong>{m.group(2)}</strong>{m.group(3)}'
    return line

def replace_italic(line):
    m = re.match('(.*)_(.*)_(.*)', line)
    if m:
        line = f'{m.group(1)}<em>{m.group(2)}</em>{m.group(3)}'
    return line
