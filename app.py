from st_pages import Page, show_pages
from frontend.form import create_form


show_pages(
    [
        Page("app.py", "Home"),
        Page("frontend/form.py", "Form"),
        Page("frontend/pages/admin_v2.py", "Servers"),
    ]
)


if __name__ == "__main__":
    create_form()
