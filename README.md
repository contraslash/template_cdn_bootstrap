# Template CDN Bootstrap

This is a simple  Django template that uses bootstrap from a CND


Navbar uses the default navbar proposed on [Bootstrap documentation](https://getbootstrap.com/docs/4.0/components/navbar/)

## Usage

Add `template_cdn_bootstrap` to your `INSTALLED_APPS` in your django `settings.py` file

Also if you want to see as an index page add

```python
path(
    '',
    include('template_cdn_bootstrap.urls')
    
)
```

To your `urls.py` file under the `urlpattenrs` list.


To render menus un navbar use the following configuration in each `conf.py` of your installed app

```python
MENUS = {
    "name": _("<menu_dropdown_title>"),
    "url_reversed": "reverse_lazy(<your_url_name>)",
    "permissions": ["<permission_to_access_the_view>"]
    "sub_menus": [
        {
            "name": _("<submenu_name>"),
            "url_reversed": reverse_lazy(<your_url_name>),
            "permissions": ["<permission_to_access_the_view>"]

        }
    ]
}
```