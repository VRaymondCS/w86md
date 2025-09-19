# W86MD Web development with **PATH** stack

| Stack               | Function               |
| :------------------ | :--------------------- |
| **Python-FastHTML** | Web application        |
| **AlpineJS**        | Frontend interactivity |
| **TailwindCSS**     | CSS framework          |
| **HTMX**            | Frontend framework     |

---

### Initiate node_modules

- Install nodeJS
- Install npm
- On project root run:

```
npm install
```

### Initiate python virtual environment

- Install python
- Install pip
- On project root run:
    - Windows machine:
    ```
    python -m venv .venv
    .venv\scripts\activate
    pip install -r .\package-pip.txt
    ```

    - Linux machine:
    ```
    python3 -m venv .venv
    source .venv\bin\activate
    sudo pip -r install .\package-pip.txt
    ```

---

# History

### Version 1.0.0

- Add main.py as main entry point
- Add controllers, helpers, models, views, src directories
- Add \_\_init\_\_.py to controllers, helpers, and models directories:

```
    * Set controllers as Python module
    * Add basic Controller class
    * Add basic homepage (landing page)
```

- Set models as Python module

```
    * Set helpers as Python module
        * Add MSSQL helper
        * Add functions helper
```

- Set views template structure

```
    * Add bases, functions, layouts, pages, and templates directories
    * Add basic base HTML template
    * Add home index.html
```

- Add CSS configuration

```
    * Add Custom CSS
    * Add Modules CSS
    * Add TailwindCSS configuration
        * DaisyUI plugins (TailwindCSS components)
        * TailwindCSS Typography plugins
```

- Add JavaScripts configuration

```
    * Add Custom JS
    * Add JavaScript Modules
        * AlpineJS
        * HTMX
        * Highcharts
        * Datatables
        * Lucide Icons
    * Set those modules as DOM's window object
```

- Add prettier configuration
- Add webpack configuration

