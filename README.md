# Bookly — Django SaaS Appointment Booking

A production-ready, multi-tenant booking system built with Django 5.2 LTS. Any business can sign up, set up their services, and start accepting appointments in minutes.

**Live demo:** https://web-production-56997.up.railway.app  
**Demo account:** email `demo@bookly.com` / password `Demo1234!`

---

## Features

- **Multi-tenant architecture** — each business sees only their own bookings and services, enforced at the ORM level
- **Business dashboard** — manage services, availability, and incoming bookings from one place
- **Service management** — add services with custom duration and price
- **Availability scheduling** — set working hours per day of the week
- **Public booking page** — customers book at `yourdomain.com/your-business/` with no account required
- **Double-booking prevention** — time slot locks after first booking via `unique_together` constraint
- **Booking lifecycle** — Pending → Confirmed → Cancelled with one-click actions
- **Production-ready** — deployed on Railway with PostgreSQL, Gunicorn, and WhiteNoise

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.2 LTS, Python 3.12 |
| Database | PostgreSQL (via psycopg2) |
| Frontend | Tailwind CSS (utility-first) |
| Auth | Django Allauth |
| Deployment | Railway, Gunicorn, WhiteNoise |
| Config | dj-database-url |

---

## Architecture Highlights

Multi-tenancy is enforced at the queryset level — every dashboard view filters by `business__owner=request.user`. URL manipulation is prevented via `get_object_or_404(Service, id=service_id, business__owner=request.user)`.

Double-booking is prevented at the database level using `unique_together = ['business', 'date', 'start_time']` on the Booking model — not just in application logic.

Public booking pages use slugs auto-generated from business names, giving each tenant a clean shareable URL with no configuration needed.

---

## Local Setup

```bash
git clone https://github.com/jiki07/bookly.git
cd bookly
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
psql -U postgres -c "CREATE DATABASE bookly_db;"
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```