# Reusable profile components

The Profile page uses Python macros from `main.py` for its company and role timeline. Add or update verified resume entries using the structure below.

```jinja
{% call profile_experience(title="Experience", show_title=False) %}

{% call profile_company(
  name="Company name",
  total_duration="4 yrs 6 mos",
  location="Ukraine - Hybrid",
  logo="../assets/images/companies/company-name.png",
  website="https://company.example"
) %}

{{ profile_role(
  title="Senior Technical Writer",
  employment_type="Full-time",
  dates="Sep 2023 - Present",
  duration="2 yrs 11 mos",
  location="Ukraine - Hybrid",
  description="Describe the role, product area, audience, and ownership scope.",
  highlights=[
    "Documented a complex integration workflow.",
    "Improved a measurable documentation outcome."
  ],
  skills=["API documentation", "Fintech", "MkDocs"]
) }}

{{ profile_role(
  title="Technical Writer",
  employment_type="Full-time",
  dates="Feb 2022 - Aug 2023",
  duration="1 yr 7 mos",
  description="Add the earlier position at the same company here."
) }}

{% endcall %}

{% call profile_company(
  name="Previous company",
  total_duration="2 yrs",
  initials="PC"
) %}

{{ profile_role(
  title="Technical Writer",
  dates="2020 - 2022",
  description="Add verified resume content here."
) }}

{% endcall %}

{% endcall %}
```

`logo` is optional. When it is omitted, the component generates a monogram from the company name. The `highlights` and `skills` lists are optional.
