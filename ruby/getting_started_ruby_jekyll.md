Getting Started with Ruby and Jekyll
====================================

After getting some experience with server-side architecture -- getting a VPS with Linode, serving a static site with Apache, serving a dynamic site with Flask -- I wanted to learn a tool that made the creation of websites easier. I found myself spending lots of time building standard website architecture that could be better spent on making content.

I settled on [Jekyll](https://jekyllrb.com/), as it seems to abstract content from style templates in a way I grew to love in [Flask](http://flask.pocoo.org/), but in the end just produces a bunch of static files that should make deployment and scalability easier for a single-person operation.

The easiest solution I found to install Ruby 2+ on Ubuntu 14.04 was [Brightbox](https://www.brightbox.com/blog/2016/01/06/ruby-2-3-ubuntu-packages/):
```bash
sudo apt-add-repository ppa:brightbox/ruby-ng
sudo apt-get update
sudo apt-get install ruby2.3 ruby2.3-dev
```

Make sure the install worked:
```bash
ruby -v
gem -v
```

Then install Jekyll, create a new test site, and serve it to localhost:
```bash
sudo gem install jekyll
jekyll new testsite
cd testsite
jekyll serve
```

Open up the test site in your browser, then follow along with the official Jekyll docs to get a feel for it. The interesting stuff related to customizing content starts [here](https://jekyllrb.com/docs/frontmatter/).
