# Little Lemon Restaurant — Back-End Booking Web Application

## Project Title
**Little Lemon Full-Stack Restaurant Booking and Reservation System**

---

## Overview
This project is the completed final assessment for the Meta Back-End Developer / Django Web Framework course. It implements a complete full-stack reservation system for the Little Lemon restaurant, featuring:
- Django backend with a modular `restaurant` app.
- Database models for `Booking` and `Menu`.
- Comprehensive MySQL configuration with automatic SQLite compatibility for local testing and review.
- Dynamic JavaScript-powered booking form with the `fetch` API.
- Slot conflict detection and duplicate booking prohibition.
- All Reservations page rendering serialized JSON data with Google Maps integration.
- Standalone `/bookings?date=YYYY-MM-DD` API endpoint returning date-filtered JSON.

---

## Rubric Compliance Checklist

| Assessment Rubric Criterion | Implementation Details | Status |
|-----------------------------|------------------------|:------:|
| **Is the app added to the installed apps list in settings?** | `'restaurant'` is registered in `INSTALLED_APPS` in `littlelemon/settings.py`. | ✅ |
| **Is the database configuration updated inside settings?** | `DATABASES` is configured with `django.db.backends.mysql` pointing to `littlelemon` on port `3306`. | ✅ |
| **Were migrations performed?** | `restaurant/migrations/0001_initial.py` created and applied. | ✅ |
| **Are there 3 fields in the booking form?** | First name (`first_name`), Reservation date (`reservation_date`), Reservation slot (`reservation_slot`). | ✅ |
| **Does a date selector open on click?** | `<input type="date" id="reservation_date">` opens the browser's native date picker. | ✅ |
| **Are all bookings available as JSON on reservations page?** | `http://127.0.0.1:8000/reservations/` displays all bookings as formatted JSON. | ✅ |
| **Is duplicate booking prohibited?** | Backend checks `.filter(reservation_date=..., reservation_slot=...).exists()` and rejects duplicate requests. | ✅ |
| **Does changing the date refresh booking data?** | `addEventListener('change', ...)` triggers `getBookings()` to fetch fresh data for the selected date. | ✅ |
| **Is booked slot unavailable/grey?** | Reserved slots are assigned `class="booked"` and `disabled` in the dropdown options. | ✅ |
| **Can you display bookings for a specific date via API?** | `GET /bookings?date=2022-12-13` returns JSON records for that specific date. | ✅ |
| **Does "No bookings" show when empty?** | Displays `<p>No bookings</p>` whenever zero reservations exist for the chosen date. | ✅ |
| **Was fetch API used to retrieve data?** | `fetch("{% url 'bookings' %}" + "?date=" + selectedDate)` handles all API requests. | ✅ |
| **Is current date automatically selected on load?** | Automatically initialized using `new Date()` formatted to `YYYY-MM-DD`. | ✅ |

---

## Project Structure & 3 Core Exercise Files

```
littlelemon/
├── manage.py
├── Pipfile
├── requirements.txt
├── README.md
├── littlelemon/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           <-- (Exercise 1: Installed app, MySQL DB config)
│   ├── urls.py
│   └── wsgi.py
└── restaurant/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py             <-- (Exercise 1: Booking & Menu models)
    ├── forms.py              <-- (Exercise 1: BookingForm ModelForm)
    ├── urls.py               <-- (Exercise 2: URL routing for book, reservations, bookings)
    ├── views.py              <-- (Exercise 2: Views for reservations, book, bookings API)
    ├── migrations/
    │   └── 0001_initial.py   <-- Migration history
    ├── static/
    │   ├── css/style.css
    │   └── img/logo.svg
    └── templates/
        ├── base.html
        ├── index.html
        ├── about.html
        ├── menu.html
        ├── menu_item.html
        ├── book.html         <-- (Exercise 3: Fetch API, date picker, slot disabling)
        ├── reservations.html <-- (Exercise 2: JSON display + Map)
        └── partials/
            ├── _header.html
            └── _footer.html
```

---

## Instructions for Peer Reviewers

1. Open the project folder in VS Code.
2. Open a terminal and activate the environment:
   ```bash
   pipenv shell
   pipenv install
   ```
   *(Or alternatively: `pip install -r requirements.txt`)*
3. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Start the local development server:
   ```bash
   python manage.py runserver
   ```
5. Open your web browser and visit:
   - **Booking Page:** [http://127.0.0.1:8000/book/](http://127.0.0.1:8000/book/)
   - **All Reservations:** [http://127.0.0.1:8000/reservations/](http://127.0.0.1:8000/reservations/)
   - **Specific Date API:** [http://127.0.0.1:8000/bookings?date=2022-12-13](http://127.0.0.1:8000/bookings?date=2022-12-13)
