import re
from html import escape
from pathlib import Path


def render_inline_code(text):
    """Escape text, then render only backtick-wrapped fragments as inline code."""
    if not text:
        return ""

    escaped = escape(str(text))

    return re.sub(
        r"`([^`]+)`",
        r"<code>\1</code>",
        escaped,
    )


def define_env(env):
    def esc(value):
        return escape(str(value), quote=True)

    def requirement_class(value):
        value = str(value or "").lower()

        if value == "required":
            return "api-field__requirement api-field__requirement--required"

        return "api-field__requirement"

    def field_header(name, field_type=None, requirement=None, format=None):
        parts = [f'<span class="api-field__name">{esc(name)}</span>']

        if field_type:
            parts.append(f'<span class="api-field__type">{esc(field_type)}</span>')

        if format:
            parts.append(f'<span class="api-field__format">· {esc(format)}</span>')

        if requirement:
            parts.append(
                f'<span class="{requirement_class(requirement)}">{esc(requirement)}</span>'
            )

        return '<div class="api-field__line">' + "\n".join(parts) + "</div>"

    def field_details(description="", default=None, example=None, enum=None, constraints=None):
        html = []

        if description:
            html.append(f'<p class="api-field__description">{render_inline_code(description)}</p>')

        if default is not None:
            html.append(
                f'<p class="api-field__meta">Default: <code>{esc(default)}</code></p>'
            )

        if example is not None:
            html.append(
                f'<p class="api-field__meta">Example: <code>{esc(example)}</code></p>'
            )

        if enum:
            enum_values = "".join(f"<code>{esc(value)}</code>" for value in enum)
            html.append(
                f'<p class="api-field__meta">Possible values:</p>'
                f'<div class="api-field__enum">{enum_values}</div>'
            )

        if constraints:
            html.append(
                f'<p class="api-field__meta">Constraints: <code>{esc(constraints)}</code></p>'
            )

        return "\n".join(html)

    @env.macro
    def api_schema(title="Body", content_type="application/json", description="", caller=None):
        body = caller().strip() if caller else ""

        description_html = (
            f'<p class="api-schema__description">{render_inline_code(description)}</p>'
            if description
            else ""
        )

        return f"""
<section class="api-doc api-schema">
  <div class="api-schema__header">
    <h2 class="api-schema__title">{esc(title)}</h2>
    <span class="api-schema__content-type">{esc(content_type)}</span>
  </div>
  {description_html}
  <div class="api-schema__body">
    {body}
  </div>
</section>
"""
    @env.macro
    def api_body(
        title="Body",
        description="",
        content_type="application/json",
        caller=None,
    ):
        body = caller().strip() if caller else ""

        description_html = (
            f'<p class="api-schema__description">{render_inline_code(description)}</p>'
            if description
            else ""
        )

        return f"""
<section class="api-doc api-schema">
  <div class="api-schema__header">
    <h2 class="api-schema__title">{esc(title)}</h2>

    <details class="api-content-type-dropdown">
      <summary>{esc(content_type)}</summary>
      <div class="api-content-type-dropdown__menu">
        <span class="api-content-type-dropdown__option">{esc(content_type)}</span>
      </div>
    </details>
  </div>

  {description_html}

  <div class="api-schema__body">
    {body}
  </div>
</section>
"""

    @env.macro
    def api_field(
        name,
        field_type=None,
        requirement="optional",
        description="",
        format=None,
        default=None,
        example=None,
        enum=None,
        constraints=None,
        enum_collapsed=False,
        open=True,
        caller=None,
        **kwargs,
    ):
        field_type = field_type or kwargs.get("type", "")
        enum = enum if enum is not None else kwargs.get("enum")
        nested = caller().strip() if caller else ""

        nested_html = (
            f'''
  <div class="api-object__nested">
    {nested}
  </div>
'''
            if nested
            else ""
        )

        return f"""
<div class="api-field">
  {field_header(name, field_type, requirement, format)}
  {field_details(description, default, example, enum, constraints)}
  {nested_html}
</div>
"""
    @env.macro
    def api_authorizations(
        scheme="basicAuth",
        field_name="Authorization",
        field_type="string",
        requirement="required",
        description="Merchant API uses Basic Authentication. Include your account username and password, encoded in Base64, within the Authorization header.",
    ):
        return f"""
<section class="api-doc api-section">
  <div class="api-section__header">
    <h2 class="api-section__title">Authorizations</h2>

    <details class="api-auth-dropdown">
      <summary>{esc(scheme)}</summary>
      <div class="api-auth-dropdown__menu">
        <span class="api-auth-dropdown__option">{esc(scheme)}</span>
      </div>
    </details>
  </div>

  <div class="api-section__body">
    <div class="api-field">
      {field_header(field_name, field_type, requirement)}
      {field_details(description)}
    </div>
  </div>
</section>
"""

    @env.macro
    def api_parameters(title="Path parameters", caller=None):
        body = caller().strip() if caller else ""

        return f"""
<section class="api-doc api-section">
  <div class="api-section__header">
    <h2 class="api-section__title">{esc(title)}</h2>
  </div>
  <div class="api-section__body">
    {body}
  </div>
</section>
"""

    @env.macro
    def api_param(
        name,
        field_type="string",
        requirement="optional",
        description="",
        format=None,
        default=None,
        example=None,
        enum=None,
        constraints=None,
        caller=None,
    ):
        nested = caller().strip() if caller else ""

        nested_html = (
            f'''
  <div class="api-object__nested">
    {nested}
  </div>
'''
            if nested
            else ""
        )

        return f"""
<div class="api-field">
  {field_header(name, field_type, requirement, format)}
  {field_details(description, default, example, enum, constraints)}
  {nested_html}
</div>
"""

    @env.macro
    def api_object(
        name,
        requirement="optional",
        description="",
        open=False,
        caller=None,
    ):
        nested = caller().strip() if caller else ""
        open_attr = " open" if open else ""

        return f"""
<details class="api-object"{open_attr}>
  <summary>
    <div class="api-object__main">
      {field_header(name, "object", requirement)}
      {field_details(description)}
    </div>
    <span class="api-object__toggle"></span>
  </summary>
  <div class="api-object__nested">
    {nested}
  </div>
</details>
"""

    @env.macro
    def api_array(
        name,
        item_type="object",
        requirement="optional",
        description="",
        open=False,
        caller=None,
    ):
        nested = caller().strip() if caller else ""
        open_attr = " open" if open else ""
        array_type = f"array<{item_type}>"

        nested_html = (
            f'<div class="api-object__nested">{nested}</div>'
            if nested
            else ""
        )

        return f"""
<details class="api-object"{open_attr}>
  <summary>
    <div class="api-object__main">
      {field_header(name, array_type, requirement)}
      {field_details(description)}
    </div>
    <span class="api-object__toggle"></span>
  </summary>
  {nested_html}
</details>
"""

    @env.macro
    def api_root_array(
        item_type="object",
        description="",
        open=True,
        items_open=True,
        caller=None,
    ):
        nested = caller().strip() if caller else ""
        open_attr = " open" if open else ""
        items_open_attr = " open" if items_open else ""
        array_type = f"array<{item_type}>"

        return f"""
<details class="api-object api-object--root-array"{open_attr}>
  <summary>
    <div class="api-object__main">
      {field_header("", array_type, None)}
      {field_details(description)}
    </div>
    <span class="api-object__toggle"></span>
  </summary>
  <div class="api-object__nested">
    <details class="api-object api-object--array-items"{items_open_attr}>
      <summary>
        <div class="api-object__main">
          {field_header("Items", item_type, None)}
        </div>
        <span class="api-object__toggle"></span>
      </summary>
      <div class="api-object__nested">
        {nested}
      </div>
    </details>
  </div>
</details>
"""

    @env.macro
    def api_responses(caller=None):
        body = caller().strip() if caller else ""

        return f"""
<section class="api-doc api-responses">
  <h2 class="api-responses__title">Responses</h2>
  <div class="api-responses__list">
    {body}
  </div>
</section>
"""

    @env.macro
    def api_response(
        status,
        description,
        content_type="application/json",
        open=False,
        caller=None,
    ):
        body = caller().strip() if caller else ""
        open_attr = " open" if open else ""

        status_int = int(status)
        status_class = "success" if 200 <= status_int < 300 else "error"

        body_html = (
            f'<div class="api-response__body">{body}</div>'
            if body
            else ""
        )

        return f"""
<details class="api-response"{open_attr}>
  <summary>
    <span class="api-response__chevron"></span>
    <span class="api-status api-status--{status_class}">{esc(status)}</span>
    <span class="api-response__summary-text">{esc(description)}</span>
    <span class="api-response__content-type">{esc(content_type)}</span>
  </summary>
  {body_html}
</details>
"""

    @env.macro
    def api_response_description(text):
        return f'<p class="api-response__description">{render_inline_code(text)}</p>'

    @env.macro
    def api_reference_page(caller=None):
        body = caller().strip() if caller else ""

        return f"""
<div class="api-reference-page">
{body}
</div>
"""

    @env.macro
    def api_reference_row(caller=None):
        body = caller().strip() if caller else ""

        return f"""
<section class="api-reference-row">
{body}
</section>
"""

    @env.macro
    def api_reference_main(caller=None):
        body = caller().strip() if caller else ""

        return f"""
<div class="api-reference-main">
{body}
</div>
"""

    @env.macro
    def api_reference_aside(sticky=True, caller=None):
        body = caller().strip() if caller else ""
        sticky_class = " api-reference-aside--sticky" if sticky else ""

        return f"""
<aside class="api-reference-aside{sticky_class}">
{body}
</aside>
"""

    @env.macro
    def api_request_code_group(
        method="GET",
        path="",
        default_label="HTTP",
        aside=False,
        caller=None,
    ):
        body = caller().strip() if caller else ""
        aside_class = " api-code-card--aside" if aside else ""

        return (
            f'<section class="api-code-card api-code-tabs{aside_class}" data-api-code-type="request">\n'
            '  <div class="api-code-card__header">\n'
            '    <div class="api-code-card__endpoint">\n'
            f'      <span class="api-code-method api-code-method--{esc(method).lower()}">{esc(method)}</span>\n'
            f'      <code>{esc(path)}</code>\n'
            '    </div>\n'
            '    <details class="api-code-select">\n'
            f'      <summary>{esc(default_label)}</summary>\n'
            '      <div class="api-code-select__menu"></div>\n'
            '    </details>\n'
            '  </div>\n'
            '  <div class="api-code-card__body">\n'
            f'    {body}\n'
            '  </div>\n'
            '</section>'
        )

    @env.macro
    def api_response_code_group(
        default_status="200",
        default_text="OK",
        default_content_type="application/json",
        aside=False,
        caller=None,
    ):
        body = caller().strip() if caller else ""
        status_int = int(default_status)
        status_class = "success" if 200 <= status_int < 300 else "error"
        aside_class = " api-code-card--aside" if aside else ""

        return (
            f'<section class="api-code-card api-code-tabs{aside_class}" data-api-code-type="response">\n'
            '  <div class="api-code-card__header">\n'
            '    <div class="api-code-card__endpoint api-code-card__response-current">\n'
            f'      <span class="api-code-status api-code-status--{status_class}">{esc(default_status)}</span>\n'
            f'      <span class="api-code-card__response-text">{esc(default_text)}</span>\n'
            '    </div>\n'
            '    <details class="api-code-select">\n'
            f'      <summary>{esc(default_status)}</summary>\n'
            '      <div class="api-code-select__menu"></div>\n'
            '    </details>\n'
            '  </div>\n'
            '  <div class="api-code-card__body">\n'
            f'    {body}\n'
            '  </div>\n'
            '</section>'
        )

    @env.macro
    def api_code_option(
        label,
        language="json",
        active=False,
        status=None,
        status_text="",
        content_type="application/json",
        caller=None,
    ):
        code = caller().strip("\n") if caller else ""
        active_class = " is-active" if active else ""

        attrs = [
            f'data-label="{esc(label)}"',
            f'data-language="{esc(language)}"',
            f'data-content-type="{esc(content_type)}"',
        ]

        if status is not None:
            attrs.append(f'data-status="{esc(status)}"')

        if status_text:
            attrs.append(f'data-status-text="{esc(status_text)}"')

        return (
            f'<div class="api-code-option{active_class}" {" ".join(attrs)} markdown="1">\n\n'
            f'```{esc(language)}\n'
            f'{code}\n'
            '```\n\n'
            '</div>'
        )

    @env.macro
    def api_code_block(
        title="",
        language="text",
        caller=None,
    ):
        """Standalone GitBook-like code block for guide and overview pages."""
        code = caller().strip("\n") if caller else ""
        title = str(title or "").strip()

        title_html = (
            f'<div class="api-example-card__title">{esc(title)}</div>'
            if title
            else ""
        )

        return (
            '<section class="api-example-card">\n'
            f'{title_html}\n'
            '  <div class="api-example-card__body" markdown="1">\n\n'
            f'```{esc(language)}\n'
            f'{code}\n'
            '```\n\n'
            '  </div>\n'
            '</section>'
        )

    @env.macro
    def api_code_tabs(caller=None):
        """Tabbed GitBook-like code examples for guide and flow pages."""
        body = caller().strip() if caller else ""

        return (
            '<section class="api-example-card api-example-tabs">\n'
            '  <div class="api-example-tabs__nav" role="tablist"></div>\n'
            '  <div class="api-example-tabs__body">\n'
            f'{body}\n'
            '  </div>\n'
            '</section>'
        )

    @env.macro
    def api_code_tab(
        label,
        title="",
        language="text",
        active=False,
        caller=None,
    ):
        code = caller().strip("\n") if caller else ""
        active_class = " is-active" if active else ""
        title = str(title or "").strip()

        title_html = (
            f'<div class="api-example-card__title">{esc(title)}</div>'
            if title
            else ""
        )

        return (
            f'<div class="api-example-option{active_class}" data-label="{esc(label)}" markdown="1">\n'
            f'{title_html}\n'
            '```' + esc(language) + '\n'
            f'{code}\n'
            '```\n\n'
            '</div>'
        )

    @env.macro
    def api_required_headers():
        headers_file = Path(__file__).parent / "docs/_shared/api-required-headers.md"
        rows = []

        for line in headers_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()

            if not line.startswith("|") or "---" in line:
                continue

            cells = [cell.strip() for cell in line.strip("|").split("|")]

            if not cells or cells[0].lower() == "name":
                continue

            rows.append(cells)

        body = "\n".join(
            api_param(
                name=name,
                field_type=field_type,
                format=format_value or None,
                requirement=requirement,
                description=description,
            )
            for name, field_type, format_value, requirement, description in rows
        )

        return api_parameters("Headers", caller=lambda: body)

    @env.macro
    def api_page_link(
        title,
        href,
        icon=None,
        description=None,
    ):
        """GitBook-style page link card."""

        def page_link_icon(icon_name):
            icons = {
                "s2s": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7h12l-3-3 1.4-1.4L22.8 8l-5.4 5.4L16 12l3-3H7V7z"></path><path d="M17 17H5l3 3-1.4 1.4L1.2 16l5.4-5.4L8 12l-3 3h12v2z"></path></svg>',
                "payment-gateway": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 11h12l-3.5-3.5L14 6l6 6-6 6-1.5-1.5L16 13H4v-2z"></path><path d="M21 5h2v14h-2V5z"></path></svg>',
                "payout-gateway": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h2v14H3V5z"></path><path d="M20 11H8l3.5-3.5L10 6l-6 6 6 6 1.5-1.5L8 13h12v-2z"></path></svg>',
                "card": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5.5A2.5 2.5 0 0 1 5.5 3h13A2.5 2.5 0 0 1 21 5.5v3H3v-3z"></path><path d="M3 10.5h18v8A2.5 2.5 0 0 1 18.5 21h-13A2.5 2.5 0 0 1 3 18.5v-8zm3 5.5v1.5h5V16H6zm10.5 0a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3z"></path></svg>',
                "authentication": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 4 5.5v5.8c0 5 3.4 9.6 8 10.7 4.6-1.1 8-5.7 8-10.7V5.5L12 2zm0 2.2 6 2.7v4.4c0 3.9-2.4 7.4-6 8.5-3.6-1.1-6-4.6-6-8.5V6.9l6-2.7z"></path><path d="M10 10a2 2 0 1 1 3 1.7V15h-2v-3.3A2 2 0 0 1 10 10z"></path></svg>',
                "webhook": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4a3 3 0 1 1 2.8 4H8v3h5.2a3 3 0 1 1 0 2H8v3h1.8a3 3 0 1 1 0 2H6v-5H3v-2h3V6h3.8A3 3 0 0 1 7 4zm0 2a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm9 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"></path></svg>',
                "wallet": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h14a2 2 0 0 1 2 2v2h-2V7H4v10h14v-2h2v2a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z"></path><path d="M14 9h7v6h-7a3 3 0 0 1 0-6zm0 2a1 1 0 0 0 0 2h5v-2h-5z"></path></svg>',
            }
            return icons.get(icon_name)

        title = str(title or "").strip()
        href = str(href or "").strip()
        description = str(description).strip() if description else ""

        if not title or not href:
            return ""

        preset_icon = page_link_icon(icon)

        if preset_icon:
            icon_html = f'<span class="api-page-link__icon">{preset_icon}</span>'
        elif icon:
            icon_html = f'<span class="api-page-link__icon">{esc(icon)}</span>'
        else:
            icon_html = ""

        description_html = (
            f'<span class="api-page-link__description">{render_inline_code(description)}</span>'
            if description
            else ""
        )

        return (
            f'<a class="api-page-link" href="{esc(href)}">'
            f'{icon_html}'
            '<span class="api-page-link__body">'
            f'<span class="api-page-link__title">{esc(title)}</span>'
            f'{description_html}'
            '</span>'
            '<span class="api-page-link__arrow">›</span>'
            '</a>'
        )

    @env.macro
    def profile_experience(
        title="Experience",
        empty_message="",
        show_title=True,
        caller=None,
    ):
        """Container for resume-style company and role entries."""
        body = caller().strip() if caller else ""
        title = str(title or "Experience").strip()
        title_id = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-") or "experience"

        if not body and empty_message:
            body = (
                '<div class="profile-experience__empty">'
                f'<p>{render_inline_code(empty_message)}</p>'
                '</div>'
            )

        heading_html = (
            f'<h2 class="profile-experience__title" id="profile-{esc(title_id)}">{esc(title)}</h2>'
            if show_title
            else ""
        )
        section_class = (
            "profile-experience"
            if show_title
            else "profile-experience profile-experience--continuation"
        )
        section_label = (
            f'aria-labelledby="profile-{esc(title_id)}"'
            if show_title
            else f'aria-label="{esc(title)}"'
        )

        return (
            f'<section class="{section_class}" {section_label}>'
            f'{heading_html}'
            f'<div class="profile-experience__list">{body}</div>'
            '</section>'
        )

    @env.macro
    def profile_company(
        name,
        total_duration="",
        location="",
        logo="",
        logo_alt="",
        initials="",
        website="",
        caller=None,
    ):
        """Company header with an optional logo and one or more role entries."""
        roles = caller().strip() if caller else ""
        name = str(name or "").strip()

        if not name:
            return ""

        if logo:
            alt = logo_alt or f"{name} logo"
            logo_html = (
                '<span class="profile-company__logo">'
                f'<img src="{esc(logo)}" alt="{esc(alt)}" loading="lazy">'
                '</span>'
            )
        else:
            words = re.findall(r"[^\W_]+", name, flags=re.UNICODE)
            fallback = "".join(word[0] for word in words[:2]).upper() or "C"
            monogram = str(initials or fallback).strip()[:3].upper()
            logo_html = (
                '<span class="profile-company__logo profile-company__logo--monogram" '
                'aria-hidden="true">'
                f'{esc(monogram)}'
                '</span>'
            )

        if website:
            name_html = (
                f'<a class="profile-company__name-link" href="{esc(website)}">'
                f'{esc(name)}</a>'
            )
        else:
            name_html = esc(name)

        meta = "".join(
            f'<span>{esc(value)}</span>'
            for value in (total_duration, location)
            if value
        )
        meta_html = f'<div class="profile-company__meta">{meta}</div>' if meta else ""

        return (
            '<article class="profile-company">'
            f'{logo_html}'
            '<div class="profile-company__body">'
            '<header class="profile-company__header">'
            f'<h3 class="profile-company__name">{name_html}</h3>'
            f'{meta_html}'
            '</header>'
            f'<div class="profile-company__roles">{roles}</div>'
            '</div>'
            '</article>'
        )

    @env.macro
    def profile_role(
        title,
        employment_type="",
        dates="",
        duration="",
        location="",
        description="",
        highlights=None,
        skills=None,
    ):
        """Timeline role within a company experience entry."""
        title = str(title or "").strip()

        if not title:
            return ""

        date_parts = [str(value).strip() for value in (dates, duration) if value]
        dates_html = (
            '<p class="profile-role__dates">'
            + '<span aria-hidden="true"> &middot; </span>'.join(esc(value) for value in date_parts)
            + '</p>'
            if date_parts
            else ""
        )
        employment_html = (
            f'<p class="profile-role__employment">{esc(employment_type)}</p>'
            if employment_type
            else ""
        )
        location_html = (
            f'<p class="profile-role__location">{esc(location)}</p>'
            if location
            else ""
        )
        description_html = (
            f'<p class="profile-role__description">{render_inline_code(description)}</p>'
            if description
            else ""
        )
        highlights_html = (
            '<ul class="profile-role__highlights">'
            + "".join(f'<li>{render_inline_code(item)}</li>' for item in highlights)
            + '</ul>'
            if highlights
            else ""
        )
        skills_html = (
            '<div class="profile-role__skills" aria-label="Skills">'
            '<span class="profile-role__skills-label">Skills</span>'
            + "".join(f'<span class="profile-role__skill">{esc(skill)}</span>' for skill in skills)
            + '</div>'
            if skills
            else ""
        )

        return (
            '<section class="profile-role">'
            '<span class="profile-role__marker" aria-hidden="true"></span>'
            f'<h4 class="profile-role__title">{esc(title)}</h4>'
            f'{employment_html}{dates_html}{location_html}{description_html}'
            f'{highlights_html}{skills_html}'
            '</section>'
        )

