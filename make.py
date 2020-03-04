# -*- coding: utf-8 -*-

from os.path import exists
from subprocess import Popen, PIPE
from jinja2 import Template

import hashlib


def _hash(src):
    md5 = hashlib.md5()
    md5.update(str(src).encode('utf8'))
    return md5.hexdigest()


def _make_ass(type, sentences):
    with open('static/video/{}/template.tpl'.format(type)) as fp:
        template = fp.read()

    ass = 'static/cache/{}.ass'.format(type)
    with open(ass, "w", encoding="utf8") as fp:
        fp.write(Template(template).render(sentences=sentences))
    return ass


def make_gif(type, sentences):
    ass = _make_ass(type, sentences)
    gif = 'static/cache/' + type + '-' + _hash(sentences) + '.gif'
    if exists(gif): return gif

    mp4 = 'static/video/{}/template.mp4'.format(type)
    cmd = 'ffmpeg -i {} -r 8 -vf ass={},scale=300:-1 -y {}'.format(mp4, ass, gif)

    ppoen = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    ppoen.communicate()

    return gif if ppoen.returncode == 0 else None
