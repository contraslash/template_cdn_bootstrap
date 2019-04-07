# Pro Sidebar

This is a simple  Django template that uses bootstrap from a CND

Sidebar was created based on [Pro Sidebar](https://bootsnipp.com/snippets/Q0dAX)
by [Bootsnip](https://bootsnipp.com/)

To use sidebar use the next schema in your `conf.py`

```
MENUS = {
    "name": _("<menu_dropdown_title>"),
    "fa_icon": "fa-<some_awesome_font>",
    "sub_menus": [
        {
            "name": _("<submenu_name>"),
            "url_reversed": reverse_lazy(<your_url_name>),
            "permissions": ["<permission_to_access_the_view>"]

        }
    ]
}
```

Also add `applications.base_template.context_processors.menus` to your
context processors.
