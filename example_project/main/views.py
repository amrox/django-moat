import datetime

from django.http import HttpResponse


HTML = """
<html>
<h1 style="color: green;">Access Granted</h1>
<br />
<em>{page_type}</em>&nbsp;/&nbsp;{now}
</html>
"""

def home(request):
    now = datetime.datetime.now()
    html = HTML.format(page_type="private", now=now)
    return HttpResponse(html)

def public(request):
    now = datetime.datetime.now()
    html = HTML.format(page_type="public", now=now)
    return HttpResponse(html)