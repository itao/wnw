import json

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader


def add(request):
    h = loader.get_template('pages/app/klasses/create_header.html')
    t = loader.get_template('pages/app/klasses/create.html')
    c = RequestContext(
        request,
        {}
    )
    header = h.render(c)
    body = t.render(c)

    return HttpResponse(
        json.dumps({
            'header': header,
            'body': body,
        }),
        mimetype="application/json"
    )

