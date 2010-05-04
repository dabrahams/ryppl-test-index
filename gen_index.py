from boost import repos
import os, shutil, sys
here = os.path.dirname(
    os.path.join(os.path.curdir, __file__ or os.getcwd()))

# Delete any existing subdirectories
for d in (x for x in os.listdir(here) if os.path.isdir(x) and not x.startswith('.')):
    shutil.rmtree(d)

index_template = """<html><head><title>Links for boost-python</title></head><body><h1>Links for %(name)s</h1><a href="git+http://git.%(url_tail)s#egg=%(normal_name)s">Git Repository</a><br/> 
<a href="http://www.boost.org/doc/libs/1_42_0/libs/%(name_tail)s/doc/index.html" rel="homepage">1.42.0 home_page</a><br/> 
</body></html>"""

for name,url in repos.iteritems():
    normal_name = name.replace('.','-')
    os.mkdir(os.path.join(here,normal_name))
    assert url.startswith('git://')
    url_tail = url[len('git://'):]
    name_tail = name[name.find('.')+1:]
    open(os.path.join(here,normal_name,'index.html'), 'w').write(
        index_template % locals())
