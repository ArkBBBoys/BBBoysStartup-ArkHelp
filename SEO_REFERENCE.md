# HelpHands SEO Reference Guide

## File Structure Summary

```
helphands/
├── robots.txt                    # SEO: Robots file
├── sitemap.py                    # SEO: XML Sitemap
└── urls.py                       # SEO: Sitemap & llms.txt routes

templates/
├── base.html                     # All SEO meta tags & JSON-LD schemas
└── helpers/
    ├── home.html                 # FAQPage + Service schemas
    ├── helper_list.html          # BreadcrumbList schema
    └── helper_detail.html        # Person + AggregateRating schemas
```

## Meta Tag Blocks Available

Templates can use these blocks in `{% block %}...{% endblock %}`:

| Block | Purpose | Example |
|-------|---------|---------|
| `meta_description` | SEO meta description | 150-160 chars Bengali |
| `canonical_url` | Canonical URL | `{% url 'helpers:home' %}` |
| `og_type` | Open Graph type | `website`, `profile` |
| `og_title` | Open Graph title | Max 60 chars |
| `og_description` | Open Graph description | Max 155 chars |
| `og_image` | Open Graph image | Image URL |
| `twitter_title` | Twitter Card title | Max 70 chars |
| `twitter_description` | Twitter Card description | Max 200 chars |
| `twitter_image` | Twitter Card image | Image URL |
| `faq_schema` | FAQPage JSON-LD | See home.html example |
| `breadcrumb_schema` | BreadcrumbList JSON-LD | See helper_list.html |
| `service_schema` | Service/Person JSON-LD | See helper_detail.html |

## Schema Types Used

### Organization (All Pages)
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "HelpHands হেল্পহ্যান্ডস",
  "url": "https://www.helphands.com",
  "areaServed": { "@type": "Country", "name": "Bangladesh" }
}
```

### FAQPage (Home)
6 questions about the platform, hiring process, registration, verification

### Service (Home)
Service catalog with 8 service types:
- রান্না করা (Cooking)
- ঘর পরিষ্কার (House Cleaning)
- শিশু পরিচর্যা (Childcare)
- বৃদ্ধ সেবা (Elderly Care)
- বাগান করা (Gardening)
- গাড়ি ধোয়া (Car Washing)
- কাপড় ধোয়া (Laundry)
- বাজার করা (Shopping)

### Person (Helper Detail)
Individual helper profile with ratings, services, address

### BreadcrumbList (List + Detail)
Navigation breadcrumbs for better SERP display

## Key SEO URLs

| URL | Purpose |
|-----|---------|
| `/sitemap.xml` | XML Sitemap |
| `/robots.txt` | Robots.txt |
| `/llms.txt` | AI context file |

## Bengali Keywords

### Primary Keywords
- ডোমেস্টিক হেল্পার
- বাংলাদেশে কাজের লোক
- গৃহস্থালি কর্মী
- হাউস কিপার বাংলাদেশ

### Service Keywords
- রান্নাকারী বাংলাদেশ
- ঘর পরিষ্কার সেবা
- শিশু দেখভাল
- বৃদ্ধ সেবা

### Location Keywords
- ঢাকায় হেল্পার
- চট্টগ্রামে হেল্পার
- সকল বিভাগে হেল্পার

## Validation URLs

1. **Schema.org Validator**: https://validator.schema.org/
2. **Google Rich Results Test**: https://search.google.com/test/rich-results
3. **Google Mobile-Friendly**: https://search.google.com/test/mobile-friendly
4. **PageSpeed Insights**: https://pagespeed.web.dev/
5. **Google Search Console**: https://search.google.com/search-console
