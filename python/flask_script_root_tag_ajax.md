Add a Script Root Tag in Flask to Support AJAX
==============================================

**from the official [Flask documentation](http://flask.pocoo.org/docs/0.10/patterns/jquery/)**

When building a website with Flask, you'll eventually run into a task that is easier accomplish with JavaScript than with Python[1]. Although the official documentation suggests jQuery, I found it sufficient to just use vanilla JS for the actual `.js` scripts assuming they are small enough.

In order to direct calls to the Flask endpoint consistently, whether on development or production servers, you should embed the following tag in your `base.html` Jinja template, before the links to any other JavaScript files.

```python
<script type=text/javascript>
    SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
</script>
```

Then, when building the URL in JavaScript to send to the Flask server, just reference the `SCRIPT_ROOT` global which will equal the current location of the Flask endpoint.

[1] I wanted to have a button that, when clicked, would make a call to the server with a dynamic value from an associated `<input>` field (one that was not part of an HTML form)
