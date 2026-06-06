# HelpHands (হেল্পহ্যান্ডস)

**Bangladesh's trusted domestic helper marketplace** — a Django-powered platform connecting families with verified domestic helpers across all 8 divisions of Bangladesh.

---

## Features

### For Users (হেল্পার খুঁজছেন)
- **Browse & Search** — Filter helpers by division, district, upazila, service type, rating, and price
- **Proximity Search** — GPS-based nearby helper discovery using Haversine distance calculation
- **Helper Profiles** — View photos, bio, services, ratings, reviews, and verification status
- **Hiring System** — Request, accept, complete, and cancel hiring with status tracking
- **Reviews & Ratings** — Submit reviews (1-5 stars) after completed hirings

### For Helpers (হেল্পার)
- **Registration** — Sign up with service types, experience, rates, and NID verification
- **Dashboard** — Track pending/active/completed hirings, profile completeness score
- **Availability Management** — Toggle available/busy status dynamically

### Platform Features
- **Admin Verification** — NID verification, helper approval, trust badges
- **Ad Management** — Banner/popup/inline/sidebar ads with impression/click tracking, scheduling, priority
- **Progressive Web App (PWA)** — Offline cache via service worker, installable on mobile
- **Dark Mode** — System preference + manual toggle, persisted in localStorage
- **Favorites** — localStorage-based helper wishlist with heart toggle
- **Bangla UI** — Full Bengali language interface with Noto Serif Bengali font
- **Responsive Design** — Mobile-first layout with reveal animations and skeleton loading
- **SEO Optimized** — Open Graph, Twitter Cards, JSON-LD structured data, XML sitemap, `llms.txt`
- **SOS Banner** — Emergency helper finder call-to-action

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django 6.0.6, Python 3.14+ |
| **Database** | SQLite (dev), PostgreSQL (prod) |
| **Template Engine** | Django Templates (Jinja-like) |
| **CSS** | Pure CSS (58KB, no frameworks), CSS custom properties |
| **JS** | Vanilla JS (29KB, no jQuery) |
| **Admin Panel** | Django Jazzmin (Cosmo/Darkly themes) |
| **Static Files** | Whitenoise with compression |
| **File Storage** | Backblaze B2 (S3-compatible) via django-storages |
| **Email** | Anymail + Resend |
| **PWA** | django-pwa + custom service worker |
| **Auth** | Custom user model (`AbstractUser`), session-based |

---

## Project Structure

```
ArkHelps/
├── accounts/                  # Users, profiles, authentication
│   ├── models.py             # User, UserProfile, HelperProfile, SiteConfiguration
│   ├── views.py              # signup, login, dashboard, edit_profile, edit_helper_profile
│   ├── forms.py              # SignupForm, LoginForm, UserProfileForm, HelperProfileForm
│   ├── urls.py               # 7 URL patterns
│   └── admin.py              # UserProfileAdmin, HelperProfileAdmin, SiteConfigurationAdmin
│
├── helpers/                   # Browse & search helpers
│   ├── views.py              # home, helper_list, helper_detail, AJAX endpoints, nearby helpers API
│   ├── urls.py               # 8 URL patterns (home, list, detail, 3 AJAX, 1 API)
│   ├── choices.py            # BD location data: 8 divisions, 64 districts, hundreds of upazilas
│   └── admin.py              # (managed in accounts app)
│
├── hirings/                   # Hiring workflow & reviews
│   ├── models.py             # Hiring, Review
│   ├── views.py              # create_hiring, my_hirings, submit_review, cancel/accept/complete
│   ├── urls.py               # 6 URL patterns
│   └── admin.py              # HiringAdmin, ReviewAdmin
│
├── ads/                       # Advertisement management
│   ├── models.py             # Ad, AdClick, AdImpression
│   ├── views.py              # get_ads, track_impression, track_click
│   ├── urls.py               # 2 URL patterns (tracking)
│   ├── admin.py              # AdAdmin, AdClickAdmin, AdImpressionAdmin
│   └── templatetags/
│       └── ad_tags.py        # {% get_ads %}, {% get_popup_ads %}, {% get_banner_ads %}
│
├── helphands/                 # Django project root
│   ├── settings.py           # 215-line config
│   ├── urls.py               # 13 URL patterns
│   ├── context_processors.py # SiteConfiguration context
│   └── sitemap.py            # StaticSitemap, HelperSitemap, HiringSitemap
│
├── templates/
│   ├── base.html             # Master layout (navbar, footer, messages, ads, theme toggle)
│   ├── helpers/              # home.html, helper_list.html, helper_detail.html
│   ├── accounts/             # signup, login, dashboard, edit_profile, edit_helper_profile
│   ├── hirings/              # create_hiring, my_hirings, submit_review
│   ├── ads/                  # ad_display.html
│   ├── pages/                # about, terms, privacy
│   └── emails/               # verification.html
│
├── static/
│   ├── css/style.css         # 58KB — all styles, dark mode, animations, responsive
│   ├── js/main.js            # 29KB — global JS, filters, favorites, geolocation, toasts
│   ├── img/logo.svg          # SVG logo (was missing, created in fix)
│   └── llms.txt              # AI SEO optimization
│
├── sw.js                     # PWA service worker
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies (12 packages)
├── pyproject.toml            # Project metadata
└── .env.example              # Environment template
```

---

## Database Models

### User (AbstractUser)
- Custom user model (`AUTH_USER_MODEL = 'accounts.User'`)
- Method: `get_initials()` → initials from name/username

### UserProfile (OneToOne → User)
- Account type, phone, location (division/district/upazila/place_type), GPS coordinates
- Address builder: `get_full_address()` → concatenates house → area → upazila → district → division
- Email verification, terms acceptance timestamps

### HelperProfile (OneToOne → UserProfile)
- Services (comma-separated codes), experience, rates (hourly/monthly)
- NID card image + verification, admin verification
- Rating/review stats (auto-calculated from reviews)
- `get_services_list()` → `['cooking', 'cleaning']`
- `get_display_services()` → `['রান্না করা', 'ঘর পরিষ্কার']`

### Hiring (FK → UserProfile + HelperProfile)
- Statuses: `pending` → `active` → `completed` or `cancelled`
- `can_review()` → requires status == 'completed'

### Review (OneToOne → Hiring)
- Rating 1-5, comment text
- On create: recalculates helper's `average_rating` + `total_reviews`

### Ad
- Types: popup, banner, sidebar, inline
- Placements: home, helpers list, helper detail, footer
- Scheduling: start/end dates, impression limits, priority
- `can_show` property checks all conditions

### SiteConfiguration
- Singleton model (always pk=1), stores site name, contact info, social links, legal page content

---

## Location Data (choices.py)

Comprehensive Bangladesh geographical data:

| Level | Count | Example |
|-------|-------|---------|
| **Divisions** | 8 | ঢাকা, চট্টগ্রাম, রাজশাহী, খুলনা, বরিশাল, সিলেট, রংপুর, ময়মনসিংহ |
| **Districts** | 64 | All districts across all divisions |
| **Upazilas** | 500+ | All upazilas mapped to parent districts |

Helper functions:
- `get_districts_by_division(code)` → list of district tuples
- `get_upazilas_by_district(code)` → list of upazila tuples

AJAX endpoints: `/get-districts/`, `/get-upazilas/`, `/ajax/districts/`, `/ajax/upazilas/`

---

## API Endpoints

### Location AJAX
| Endpoint | Method | Params | Returns |
|----------|--------|--------|---------|
| `/get-districts/` | GET | `division` | `{districts: [[code, name], ...]}` |
| `/get-upazilas/` | GET | `district` | `{upazilas: [[code, name], ...]}` |
| `/ajax/districts/` | GET | `division` | `{districts: [{code, name}, ...]}` |
| `/ajax/upazilas/` | GET | `district` | `{upazilas: [{code, name}, ...]}` |

### Nearby Helpers API
```http
GET /api/nearby-helpers/?lat=23.8103&lng=90.4125&radius=10
```
Returns up to 20 nearby verified, available helpers within radius (km). Uses bounding box pre-filter + Haversine exact filter.

### Ad Tracking
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/ads/track/impression/<id>/` | POST | Record ad impression |
| `/ads/track/click/<id>/` | POST | Record ad click + redirect |

---

## URL Reference

### Namespace: `helpers:`
| Name | URL | View |
|------|-----|------|
| `home` | `/` | `home` |
| `helper_list` | `/helpers/` | `helper_list` |
| `helper_detail` | `/helpers/<pk>/` | `helper_detail` |

### Namespace: `accounts:`
| Name | URL | View |
|------|-----|------|
| `signup` | `/accounts/signup/` | `signup` |
| `login` | `/accounts/login/` | `login_view` |
| `logout` | `/accounts/logout/` | `logout_view` |
| `dashboard` | `/accounts/dashboard/` | `dashboard` |
| `edit_profile` | `/accounts/dashboard/edit-profile/` | `edit_profile` |
| `edit_helper_profile` | `/accounts/dashboard/edit-helper-profile/` | `edit_helper_profile` |

### Namespace: `hirings:`
| Name | URL | View |
|------|-----|------|
| `create_hiring` | `/hirings/hire/<helper_id>/` | `create_hiring` |
| `my_hirings` | `/hirings/my-hirings/` | `my_hirings` |
| `submit_review` | `/hirings/hirings/<hiring_id>/review/` | `submit_review` |
| `cancel_hiring` | `/hirings/hirings/<hiring_id>/cancel/` | `cancel_hiring` |
| `accept_hiring` | `/hirings/hirings/<hiring_id>/accept/` | `accept_hiring` |
| `complete_hiring` | `/hirings/hirings/<hiring_id>/complete/` | `complete_hiring` |

### No Namespace
| Name | URL | Template |
|------|-----|----------|
| `about` | `/about/` | `pages/about.html` |
| `terms` | `/terms/` | `pages/terms.html` |
| `privacy` | `/privacy/` | `pages/privacy.html` |

---

## Setup

```bash
cd C:\Users\ASUS\ArkHelps
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# → http://localhost:8000
```

### Environment Variables (`.env`)
```
SECRET_KEY=django-insecure-helphands-dev-key-2026-change-in-prod
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=
SITE_URL=http://localhost:8000
RESEND_API_KEY=
```

### Production Build
```bash
python manage.py collectstatic --noinput
python manage.py runserver  # or deploy via WSGI
```

---

## Configuration Notes

- **Database**: Uses `DATABASE_URL` if set, otherwise defaults to SQLite (`db.sqlite3`)
- **Storage**: S3-compatible (Backblaze B2) when `AWS_STORAGE_BUCKET_NAME` is set; falls back to local `media/`
- **Email**: Anymail + Resend backend; requires `RESEND_API_KEY`
- **PWA**: Icons point to `/static/img/logo.svg`; service worker caches core assets
- **allauth**: Package installed but NOT configured in `INSTALLED_APPS` or `urls.py`
- **Security**: CSRF/Session cookies are secure when `DEBUG=False`; HSTS, XSS, nosniff enabled

---

## Known Gaps

1. **Tests**: `*/tests.py` files exist but are empty — no pytest/Django TestCase yet
2. **Messaging**: No internal messaging between users and helpers
3. **Real-time**: No WebSocket/SSE — polling via page reload only
4. **Notifications**: No push notifications (polling on page load only)
5. **allauth**: Installed but not wired up — social login not available
6. **DRF**: All AJAX via `JsonResponse` (intentional, but limits API scalability)

---

## License

MIT
