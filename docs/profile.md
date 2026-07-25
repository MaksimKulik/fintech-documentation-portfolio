# Maksym Kulyk

<p class="profile-role-label">Technical Writer</p>

<p class="portfolio-lead">Technical writer experienced in product, user, API, and integration documentation for complex software platforms. I turn product requirements, developer input, interface behavior, and technical specifications into clear documentation for end users, administrators, integrators, and internal teams.</p>

<div class="profile-actions">
  <a class="profile-action profile-action--primary" href="../assets/files/Maksym-Kulyk-CV.pdf" download>Download resume</a>
  <a class="profile-action" href="#profile-experience">View experience</a>
</div>

<div class="profile-overview">
  <section class="profile-overview__section" aria-labelledby="contact-heading">
    <h2 id="contact-heading">Contact</h2>
    <dl class="profile-contact-list">
      <div><dt>Email</dt><dd><a href="mailto:maksimkulik55@gmail.com">maksimkulik55@gmail.com</a></dd></div>
      <div><dt>Phone</dt><dd><a href="tel:+380992380654">+380 99 238 0654</a></dd></div>
      <div><dt>LinkedIn</dt><dd><a href="https://www.linkedin.com/in/%D0%BC%D0%B0%D0%BA%D1%81%D0%B8%D0%BC-%D0%BA%D1%83%D0%BB%D0%B8%D0%BA-ab55b8186" target="_blank" rel="noopener">Professional profile</a></dd></div>
      <div><dt>Facebook</dt><dd><a href="https://www.facebook.com/maksim.kulik.2025/" target="_blank" rel="noopener">Personal profile</a></dd></div>
    </dl>
  </section>
  <section class="profile-overview__section" aria-labelledby="focus-heading">
    <h2 id="focus-heading">Professional focus</h2>
    <p>Documentation architecture, fintech and payment workflows, API reference, business logic, release notes, diagrams, and documentation quality assurance.</p>
  </section>
</div>

## Experience

{% call profile_experience(title="Experience", show_title=False) %}

{% call profile_company(name="SPRiBE", initials="SP") %}
{{ profile_role(
  title="Technical Writer",
  employment_type="Full-time",
  dates="November 2025 - Present",
  description="Own full-cycle product documentation for platform products, with an emphasis on business logic clarity, operational workflows, configuration transparency, and consistent information architecture.",
  highlights=[
    "Create structured documentation for BackOffice, User Management, Admin Area, CRM, CMS, Risk Management, Payments, and other complex product modules.",
    "Describe UI elements, workflows, tables, validation rules, configuration logic, system behavior, and edge cases.",
    "Prepare release notes with clear functional impact and classification.",
    "Analyze Jira tasks, videos, demos, and backend changes, then validate the resulting documentation with developers, QA engineers, and product managers.",
    "Standardize terminology, field descriptions, and documentation patterns across product modules."
  ],
  skills=["Product documentation", "Release notes", "Jira", "Business logic", "Documentation QA"]
) }}
{% endcall %}

{% call profile_company(name="Sensus", initials="SE") %}
{{ profile_role(
  title="Technical Writer",
  employment_type="Part-time",
  dates="February 2026 - Present",
  description="Create and maintain technical, API, integration, and product documentation for payment-processing and payment-orchestration platforms.",
  highlights=[
    "Transform OpenAPI specifications, Jira requirements, source documents, screenshots, demos, and developer input into structured guidance for merchants, integrators, operations teams, and platform administrators.",
    "Document platform configuration, merchants, payment methods, providers, routing, balances, orders, transactions, access control, and operational monitoring.",
    "Produce endpoint references covering authentication and request signing, parameters, nested schemas, request and response examples, statuses, validation rules, errors, and webhooks.",
    "Build reusable documentation components for schemas, code samples, tables, admonitions, and responsive API layouts using Material for MkDocs, Markdown, HTML, CSS, Python, and Jinja templates.",
    "Create evidence-based conceptual models and developer-style diagrams for complex financial entities and workflows.",
    "Maintain documentation in Git and Bitbucket, support CI/CD publishing, and troubleshoot navigation, styling, assets, local environments, and hosted builds."
  ],
  skills=["API documentation", "OpenAPI", "Fintech", "Material for MkDocs", "Python", "HTML/CSS", "Git"]
) }}
{% endcall %}

{% call profile_company(name="Finamp", total_duration="Fintech company", initials="FI") %}
{{ profile_role(
  title="Technical Writer",
  employment_type="Part-time",
  dates="July 2025 - January 2026",
  description="Created structured business and system documentation for a fintech mobile application.",
  highlights=[
    "Prepared BRD and SRS documentation covering business logic, user flows, and system behavior.",
    "Documented holders, users, devices, stored-value accounts, wallets, bonuses, vouchers, gift certificates, and digital stamps.",
    "Defined wallet rules for activation, expiration, holds, freezes, and partial redemption.",
    "Documented Admin Panel behavior, including dynamic fields, CRUD operations, entity management, and configuration rules.",
    "Worked with product and development teams on diagrams and scenarios for onboarding, KYC, loyalty, and transactions."
  ],
  skills=["BRD", "SRS", "Fintech", "User flows", "Admin systems"]
) }}
{% endcall %}

{% call profile_company(name="Yellow Duck Coders", initials="YD") %}
{{ profile_role(
  title="Technical Writer",
  employment_type="Full-time",
  dates="February 2025 - November 2025",
  description="Produced documentation and supported requirements work across social platforms, transportation, mobile applications, fintech products, and other custom software.",
  highlights=[
    "Created BRDs, UI/UX descriptions, technical specifications, and concise API overviews.",
    "Gathered and clarified requirements, refined functionality, and supported product decisions.",
    "Designed diagrams, flowcharts, system maps, and user-flow scenarios for teams and stakeholders.",
    "Communicated directly with clients to clarify design, functionality, and documentation details.",
    "Collaborated with developers and QA engineers and wrote clear Jira tasks for backend and frontend teams."
  ],
  skills=["Technical specifications", "Requirements", "Diagrams", "Jira", "Client communication"]
) }}
{% endcall %}

{% call profile_company(name="GeeksForLess", initials="GL") %}
{{ profile_role(
  title="Technical Support Specialist",
  employment_type="Full-time",
  dates="May 2024 - February 2025",
  description="Provided technical support to customers and partners and created clear end-user instructions for hosting and infrastructure services.",
  highlights=[
    "Investigated technical issues with internal tools, tested software behavior, and handled ticket escalation in Jira.",
    "Supported domain registration, WHOIS, transfers, renewals, DNS, virtual machines, FTP, file management, and .htaccess configuration.",
    "Troubleshot POP3, IMAP, SMTP, SPF, DKIM, DMARC, mail clients, logs, and email headers using tools such as Telnet and OpenSSL.",
    "Supported SSL installation and troubleshooting, MySQL, and phpMyAdmin."
  ],
  skills=["Technical support", "DNS", "Email systems", "Web hosting", "Troubleshooting"]
) }}
{% endcall %}

{% call profile_company(name="Delta Express / Ontrack Transportation", initials="DO") %}
{{ profile_role(
  title="Safety Department Specialist",
  employment_type="Full-time",
  dates="February 2022 - April 2024",
  description="Handled transportation safety operations, claims, customer communication, and documentation in a time-sensitive environment.",
  highlights=[
    "Managed problem-solving, crisis response, compliance, claims, and loss mitigation.",
    "Prepared claim presentations, denial letters, letters of exclusivity, cargo release letters, and temperature and humidity reports.",
    "Coordinated with contractors, brokers, customers, and insurance companies.",
    "Contributed to the planning, coordination, and implementation of a refrigerated-goods transportation project."
  ],
  skills=["Operations", "Claims", "Documentation", "Customer support", "Project coordination"]
) }}
{% endcall %}

{% endcall %}

## Skills

<section class="profile-band profile-band--continuation" aria-label="Skills">
  <div class="profile-skill-groups">
    <div><h3>Documentation</h3><p>Technical documentation, user guides, API and integration documentation, BRD and SRS, technical specifications, release notes, test documentation, and information architecture.</p></div>
    <div><h3>Tools and formats</h3><p>Confluence, Notion, Jira, Google Docs, Material for MkDocs, Markdown, HTML/CSS, Python, Jinja templates, Swagger/OpenAPI, JSON, Git, Bitbucket, Miro, Draw.io, Lightshot, and ScreenToGif.</p></div>
    <div><h3>Methods</h3><p>Requirements clarification, diagramming, documentation QA, software testing for documentation validation, stakeholder collaboration, and structured analysis of product behavior.</p></div>
    <div><h3>Languages</h3><p>English: B2 spoken, C1-C2 written. Ukrainian and Russian: native.</p></div>
  </div>
</section>

## Education

<section class="profile-band profile-band--continuation" aria-label="Education">
  <div class="profile-record-list">
    <article><h3>Master's degree in Philosophy</h3><p>Taras Shevchenko National University of Kyiv <span aria-hidden="true">&middot;</span> Graduated in 2025</p></article>
    <article><h3>Master's degree in Applied Mechanics</h3><p>Sumy State University <span aria-hidden="true">&middot;</span> Graduated in 2025</p></article>
  </div>
</section>

## Additional training

<section class="profile-band profile-band--continuation" aria-label="Additional training">
  <ul class="profile-training-list">
    <li>Technical Writing: How to Write Software Documentation, Udemy</li>
    <li>English Language Course, English Prime, 1.5 years</li>
    <li>Python Essentials, Cisco Networking Academy - <a href="https://github.com/MaksimKulik/Python-projects/" target="_blank" rel="noopener">Python projects</a></li>
    <li>HTML/CSS for documentation - <a href="https://maksimkulik.github.io/Portfolio_rep/" target="_blank" rel="noopener">published portfolio</a> and <a href="https://github.com/MaksimKulik/Portfolio_rep" target="_blank" rel="noopener">source repository</a></li>
    <li>SQL course, Codecademy</li>
  </ul>
</section>

## Publications

<section class="profile-band profile-band--continuation" aria-label="Publications">
  <ol class="profile-publications">
    <li>Kulyk, M. R. (2020). <em>The Epistemology of Severinus Boethius: Main Concepts and Meanings in the Context of Medieval Theology.</em> Bulletin of V. N. Karazin Kharkiv National University, Philosophy series, issue 63, pp. 109-118.</li>
    <li>Kulyk, M. R. (2020). <em>The Concepts of Divina Intellegentia and Simplicia Forma in the Theological Epistemology of Severinus Boethius.</em> Proceedings of the International Scientific Conference "Days of Science of the Faculty of Philosophy - 2020," part 1, pp. 10-11. In Ukrainian.</li>
    <li>Kulyk, M. R. (2025). <em>The Concepts of Intellectus Possibilis and Intellectus Agens in the Theory of Knowledge of Thomas Aquinas.</em> Proceedings of the International Scientific Conference "Days of Science of the Faculty of Philosophy - 2025," part 1, pp. 59-61. In English.</li>
  </ol>
</section>

## Documentation samples

{{ api_page_link(title="Explore the selected samples", href="../#selected-samples", icon="s2s", description="Review product guidance, API reference, and integration examples.") }}
