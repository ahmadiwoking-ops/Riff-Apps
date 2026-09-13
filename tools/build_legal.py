import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shell import page, LEGAL  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPDATED = "13 September 2026"

ENTITY = (
    "Riff Apps (&ldquo;Riff Apps&rdquo;, &ldquo;we&rdquo;, &ldquo;us&rdquo;, &ldquo;our&rdquo;), "
    "registered in England and Wales, company number [company number], "
    "registered office [registered office address]"
)


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel)


def legal_page(slug, heading, intro, sections, description):
    toc = "\n".join(
        f'        <li><a href="#{sid}">{stitle}</a></li>' for sid, stitle, _ in sections
    )
    body_sections = "\n".join(
        f'      <h2 id="{sid}">{stitle}</h2>\n{html}' for sid, stitle, html in sections
    )
    body = f"""
<section class="doc-head">
  <div class="shell">
    <h1>{heading}</h1>
    <p>{intro}</p>
    <p class="doc-updated">Last updated {UPDATED}</p>
  </div>
</section>
<hr class="rule">

<section class="band-paper">
  <div class="shell doc-layout">
    <nav class="doc-nav" aria-labelledby="toc-heading">
      <h2 id="toc-heading">On this page</h2>
      <ol>
{toc}
      </ol>
    </nav>
    <div class="prose">
{body_sections}
    </div>
  </div>
</section>
"""
    return page(f"{heading} — Riff Apps", description, f"/legal/{slug}",
                body, css_depth=1)


# ===========================================================================
# PRIVACY POLICY
# ===========================================================================
privacy = [
    ("who-we-are", "Who we are", f"""
      <p>This site is operated by {ENTITY}. We can be reached at <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a>.</p>
      <p>This policy explains what we do with personal data when you visit riff-apps.com, contact us, or work with us as a client. Our own products &mdash; such as Riff and TeachWise AI &mdash; have their own privacy notices covering the data they process, and those notices apply when you use them.</p>
      <p>We are the <strong>controller</strong> for the data described in this policy. When we build or run software for a client, that client is normally the controller and we act as their <strong>processor</strong> under a written data processing agreement.</p>
"""),
    ("what-we-collect", "What we collect", """
      <h3>When you visit this site</h3>
      <p>This site does not run advertising or analytics trackers. Our hosting provider processes technical information as a normal part of serving the site &mdash; including your IP address, the pages requested, the time of the request, and your browser type &mdash; in server logs used for security and reliability.</p>
      <p>Fonts, images, scripts and stylesheets are served from our own domain, so simply loading a page does not share your details with a third-party content network.</p>
      <h3>When you contact us</h3>
      <p>Our enquiry form opens a message in your own email application. Nothing reaches us until you choose to send it. When you do, we receive your name, email address, any organisation you give, the topic you selected and the content of your message.</p>
      <h3>When you become a client</h3>
      <p>We hold business contact details for the people we work with, records of the work, correspondence, and the billing information needed to invoice and be paid.</p>
      <h3>What we do not collect</h3>
      <p>We do not buy personal data from data brokers, we do not build advertising profiles, and we do not ask for special category data (such as health or biometric data) in the course of a business enquiry.</p>
"""),
    ("why-and-lawful-basis", "Why we use it, and our lawful basis", """
      <table>
        <thead><tr><th>Purpose</th><th>Data</th><th>Lawful basis</th></tr></thead>
        <tbody>
          <tr><td>Replying to your enquiry</td><td>Name, email, organisation, message</td><td>Legitimate interests &mdash; responding to someone who has asked us to</td></tr>
          <tr><td>Delivering a project</td><td>Contact details, project records, correspondence</td><td>Performance of a contract</td></tr>
          <tr><td>Invoicing and accounts</td><td>Billing details, transaction records</td><td>Legal obligation &mdash; tax and company law</td></tr>
          <tr><td>Keeping the site secure and available</td><td>Server log data</td><td>Legitimate interests &mdash; protecting our service</td></tr>
          <tr><td>Occasional updates about our work</td><td>Name, email</td><td>Consent &mdash; withdrawable at any time</td></tr>
        </tbody>
      </table>
      <p>Where we rely on legitimate interests, we have considered whether our interest is overridden by your rights, and we have concluded it is not. You can object at any time using the details below.</p>
"""),
    ("ai-and-your-data", "AI and your data", """
      <p>We use AI tools in our own work &mdash; for drafting, code assistance and analysis. Two rules apply without exception:</p>
      <ul>
        <li>We do not put client confidential information or end-user personal data into a general-purpose AI tool that is outside an agreed processing arrangement.</li>
        <li>We do not permit client or end-user content to be used to train third-party models, and we choose providers whose commercial terms reflect that.</li>
      </ul>
      <p>Where a product we build uses AI to process personal data, that use is documented in the product's own privacy notice, along with what the model does, what it does not decide on its own, and how a person can challenge an output. Our <a class="textlink" href="/legal/ai-transparency">AI transparency statement</a> sets out the approach in full.</p>
"""),
    ("sharing", "Who we share it with", """
      <p>We do not sell personal data. We share it only with service providers who help us operate, each under a contract that limits them to our instructions:</p>
      <table>
        <thead><tr><th>Provider</th><th>Purpose</th><th>Where processed</th></tr></thead>
        <tbody>
          <tr><td>Vercel Inc.</td><td>Website hosting and delivery</td><td>EU / US</td></tr>
          <tr><td>Email provider</td><td>Receiving and storing correspondence</td><td>UK / EU</td></tr>
          <tr><td>Accounting software</td><td>Invoicing and statutory records</td><td>UK / EU</td></tr>
        </tbody>
      </table>
      <p>We will also disclose data where we are legally required to &mdash; see our <a class="textlink" href="/legal/law-enforcement">law enforcement guidelines</a> &mdash; or where necessary to establish or defend legal claims. If our business is ever sold or restructured, data may transfer with it, and you will be told before that changes how your data is used.</p>
"""),
    ("transfers", "International transfers", """
      <p>Some providers process data outside the UK. Where that happens we rely on UK adequacy regulations, or on the International Data Transfer Agreement or the UK Addendum to the EU Standard Contractual Clauses, together with an assessment of the protections in the destination country.</p>
      <p>You can ask us for details of the safeguard applied to any particular transfer.</p>
"""),
    ("retention", "How long we keep it", """
      <table>
        <thead><tr><th>Record</th><th>Kept for</th></tr></thead>
        <tbody>
          <tr><td>Enquiries that do not become projects</td><td>12 months from last contact</td></tr>
          <tr><td>Client project records and correspondence</td><td>6 years after the engagement ends</td></tr>
          <tr><td>Invoices and accounting records</td><td>6 years, as required by UK tax law</td></tr>
          <tr><td>Server access logs</td><td>Up to 30 days</td></tr>
          <tr><td>Mailing list details</td><td>Until you unsubscribe</td></tr>
        </tbody>
      </table>
      <p>When a retention period ends, records are deleted or anonymised.</p>
"""),
    ("security", "How we protect it", """
      <p>Data is encrypted in transit and at rest. Access is restricted to the people who need it, on named accounts protected by multi-factor authentication, and reviewed when someone joins or leaves a project. Dependencies are scanned automatically and patched to a defined schedule by severity.</p>
      <p>We maintain an incident response plan. If a breach affects your personal data and is likely to result in a risk to your rights, we will notify the Information Commissioner's Office within 72 hours of becoming aware of it, and tell you directly where the risk is high.</p>
"""),
    ("your-rights", "Your rights", """
      <p>You have the right to access your data, have it corrected, have it deleted, restrict or object to how we use it, receive it in a portable format, and withdraw consent where consent is what we relied on.</p>
      <p>To exercise any of these, email <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a>. We will respond within one month and will not charge you. We may ask for enough information to be confident we are dealing with the right person. Our <a class="textlink" href="/legal/gdpr">GDPR statement</a> explains each right in more detail.</p>
      <div class="callout">
        <p>If we are processing your data on behalf of a client &mdash; for example, as users of an application we built for them &mdash; please direct your request to that organisation. We will pass on anything that reaches us and support them in responding.</p>
      </div>
"""),
    ("children", "Children", """
      <p>This website is aimed at businesses and is not directed at children. We do not knowingly collect personal data from children through it. Products we build that are intended for younger users apply age assurance and additional protections appropriate to their audience, described in their own notices.</p>
"""),
    ("complaints", "Complaints and changes", """
      <p>If you are unhappy with how we have handled your data, tell us first at <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a> and we will try to put it right. You also have the right to complain to the Information Commissioner's Office, the UK supervisory authority, at ico.org.uk.</p>
      <p>We review this policy at least annually. If we make a material change we will update the date at the top of this page and, where the change affects you significantly, tell you directly.</p>
"""),
]

write("legal/privacy-policy.html", legal_page(
    "privacy-policy", "Privacy policy",
    "What personal data Riff Apps collects, why we hold it, who we share it with and the rights you have over it.",
    privacy,
    "Riff Apps privacy policy: what personal data we collect, our lawful basis, retention periods, international transfers and your rights under UK GDPR."))


# ===========================================================================
# TERMS OF SERVICE
# ===========================================================================
terms = [
    ("agreement", "This agreement", f"""
      <p>These terms govern your use of riff-apps.com and, where no separate signed agreement applies, the services provided by {ENTITY}.</p>
      <p>By using this website you accept these terms. If you do not accept them, please stop using the site.</p>
"""),
    ("using-the-site", "Using this website", """
      <p>You may view, download and print material from this site for your own information and for evaluating whether to work with us. You may not republish it as your own, use it commercially without our permission, or attempt to interfere with the site, its security or anyone else's use of it.</p>
      <p>The site is provided for general information. We take care over its accuracy but do not guarantee it is complete or current, and nothing on it is professional, legal or technical advice for your specific situation.</p>
"""),
    ("our-services", "Our services", """
      <p>Work we carry out for clients is governed by a written proposal, statement of work or master services agreement. That document sets out the scope, deliverables, timescales, acceptance criteria and price.</p>
      <p><strong>If anything in a signed statement of work conflicts with these terms, the statement of work takes precedence.</strong></p>
      <p>Estimates of effort and timing are given in good faith based on the information available at the time. Changes to scope are handled through a written change request, priced before work starts.</p>
"""),
    ("your-responsibilities", "What we need from you", """
      <p>Projects depend on both sides. You agree to:</p>
      <ul>
        <li>provide accurate information and timely decisions, feedback and approvals;</li>
        <li>make a person with authority available to answer questions during the engagement;</li>
        <li>give us any access, accounts, content or third-party licences the work requires;</li>
        <li>confirm you have the rights to any material you give us to use;</li>
        <li>comply with the law in how you operate the finished product, including data protection and any sector rules that apply to you.</li>
      </ul>
      <p>Where delay is caused by information or approvals we are waiting on, timescales adjust accordingly.</p>
"""),
    ("intellectual-property", "Intellectual property", """
      <p>On full payment of all sums due, ownership of the bespoke deliverables created specifically for you under a statement of work transfers to you.</p>
      <p>We keep ownership of our pre-existing materials, tools, libraries, frameworks and general know-how, and of anything we develop that is not specific to your project. Where those materials are embedded in a deliverable, you receive a perpetual, worldwide, non-exclusive licence to use them as part of it.</p>
      <p>Third-party and open-source components remain subject to their own licences, which we will identify.</p>
      <p>Unless you ask us not to, we may name you as a client and describe the work in general terms in our portfolio.</p>
"""),
    ("ai-outputs", "AI-generated material", """
      <p>Some of what we build produces content, recommendations or scores using AI models. AI output can be wrong, incomplete or unsuitable for a particular purpose, even when it reads convincingly.</p>
      <p>Where we deliver a feature that uses AI, we will tell you what it does, what it does not decide on its own, how it is evaluated and where human review sits. You remain responsible for how the finished product is operated and for any decisions taken on the basis of its output, in line with the human oversight we design in. See our <a class="textlink" href="/legal/ai-transparency">AI transparency statement</a>.</p>
      <p>The legal position on ownership of AI-generated material is still developing in the UK and elsewhere. We will tell you where an output's status may be uncertain.</p>
"""),
    ("fees", "Fees and payment", """
      <p>Fees, milestones and payment terms are set out in your statement of work. Unless stated otherwise, invoices are payable within 30 days and exclude VAT, which is added where applicable.</p>
      <p>We may suspend work on overdue accounts after written notice, and charge statutory interest on late payment under the Late Payment of Commercial Debts (Interest) Act 1998. Refunds and cancellations are covered by our <a class="textlink" href="/legal/refund-policy">refund policy</a>.</p>
"""),
    ("acceptable-use", "Acceptable use", """
      <p>Our <a class="textlink" href="/legal/acceptable-use">acceptable use policy</a> forms part of these terms and applies to this site and to any product or service we provide. We will not build or maintain software intended for an unlawful purpose, and we may end an engagement if we discover one.</p>
"""),
    ("warranties", "Warranties", """
      <p>We warrant that our services will be performed with reasonable skill and care by suitably qualified people, and that deliverables will materially conform to the specification in the statement of work for 90 days after acceptance. Our obligation for a defect reported in that period is to correct it.</p>
      <p>We do not warrant that software will be free of all defects or uninterrupted, that AI outputs will be accurate in every case, or that third-party services beyond our control will remain available. Except as expressly stated, all implied warranties are excluded to the extent the law allows.</p>
"""),
    ("liability", "Liability", """
      <p>Nothing in these terms limits liability for death or personal injury caused by negligence, for fraud or fraudulent misrepresentation, or for anything else that cannot lawfully be limited.</p>
      <p>Subject to that, neither party is liable for loss of profit, revenue, anticipated savings, business, goodwill or data, or for indirect or consequential loss, however arising.</p>
      <p>Subject to the above, our total liability arising out of an engagement is limited to the total fees paid by you under the relevant statement of work in the 12 months before the claim arose.</p>
      <p>These limits reflect the allocation of risk between two businesses and are taken into account in our prices. They do not affect the statutory rights of a consumer.</p>
"""),
    ("confidentiality", "Confidentiality and data protection", """
      <p>Each party will keep the other's confidential information in confidence, use it only for the engagement, and protect it with at least the care it applies to its own. This does not cover information that is public through no fault of the receiving party, already known, independently developed, or required to be disclosed by law.</p>
      <p>Where we process personal data on your behalf, we do so under a data processing agreement that meets Article 28 of the UK GDPR. Our <a class="textlink" href="/legal/gdpr">GDPR statement</a> sets out how we approach that.</p>
"""),
    ("termination", "Ending an engagement", """
      <p>Either party may end an engagement on 30 days' written notice, or immediately if the other commits a material breach that is not remedied within 14 days of being told about it, or becomes insolvent.</p>
      <p>On termination you pay for work completed and for committed costs we cannot recover. We will hand over deliverables paid for in a reasonable format, and delete or return your data on request.</p>
"""),
    ("general", "General", """
      <p>These terms are the entire agreement between us on their subject matter, alongside any statement of work. If a provision is found unenforceable, the rest continues to apply. A delay in enforcing a right is not a waiver of it. Neither party is liable for failure caused by events outside its reasonable control.</p>
      <p>Nobody other than you and us has rights under these terms. Neither party may assign them without the other's written consent, which will not be unreasonably withheld.</p>
      <p>These terms are governed by the law of England and Wales, and the courts of England and Wales have exclusive jurisdiction.</p>
      <p>We may update these terms. The version in force is the one published here when you use the site or when a statement of work is signed.</p>
"""),
]

write("legal/terms-of-service.html", legal_page(
    "terms-of-service", "Terms of service",
    "The terms covering your use of this website and the services Riff Apps provides.",
    terms,
    "Riff Apps terms of service: use of this website, how engagements work, intellectual property, AI-generated material, liability and governing law."))


# ===========================================================================
# COOKIE POLICY
# ===========================================================================
cookies = [
    ("summary", "The short version", """
      <div class="callout">
        <p><strong>This website sets no advertising, analytics or tracking cookies.</strong> You will not see a consent banner here because there is nothing to consent to.</p>
      </div>
      <p>We built it that way deliberately. A studio that sells governance should not open with a tracking wall. If that changes &mdash; for example if we add privacy-respecting analytics &mdash; we will ask for your consent first and update this page.</p>
"""),
    ("what-cookies-are", "What cookies are", """
      <p>A cookie is a small text file a website stores on your device. Similar technologies &mdash; local storage, session storage and pixels &mdash; do comparable jobs, and where we refer to cookies we mean those too.</p>
      <p>Cookies are grouped by what they are for: <strong>strictly necessary</strong> ones that a site cannot function without, <strong>functional</strong> ones that remember preferences, <strong>analytics</strong> ones that measure use, and <strong>advertising</strong> ones that track people across sites. Under UK law, only strictly necessary cookies can be set without your consent.</p>
"""),
    ("what-we-use", "What this site uses", """
      <table>
        <thead><tr><th>Type</th><th>Used here</th><th>Detail</th></tr></thead>
        <tbody>
          <tr><td>Strictly necessary</td><td>Minimal</td><td>Our host may set a short-lived cookie to route requests and protect against abuse. It carries no profile of you.</td></tr>
          <tr><td>Functional</td><td>None</td><td>The site remembers nothing between visits.</td></tr>
          <tr><td>Analytics</td><td>None</td><td>We do not run Google Analytics or any equivalent.</td></tr>
          <tr><td>Advertising</td><td>None</td><td>We do not advertise or allow third parties to track visitors here.</td></tr>
        </tbody>
      </table>
      <p>Fonts, images, styles and scripts are served from our own domain rather than a third-party network, so loading a page does not reveal your visit to another company.</p>
      <p>Our hosting provider keeps short-term server logs, including IP addresses, for security and reliability. That is described in our <a class="textlink" href="/legal/privacy-policy">privacy policy</a> rather than here, because it does not involve storing anything on your device.</p>
"""),
    ("other-products", "Our other products", """
      <p>Riff, TeachWise AI and other applications we operate are separate services with their own cookie notices and, where relevant, their own consent controls. This policy covers riff-apps.com only.</p>
      <p>Links from this site to third-party sites take you somewhere with its own practices, which we do not control.</p>
"""),
    ("managing", "Managing cookies", """
      <p>You can block or delete cookies in your browser settings, usually under privacy or site data. Blocking strictly necessary cookies may stop parts of some sites working, though this one will continue to function.</p>
      <p>Most browsers also offer a do-not-track or global privacy control signal. We honour such signals by default, since we do not track visitors in the first place.</p>
"""),
    ("changes", "Changes", """
      <p>If we introduce any cookie beyond the strictly necessary, we will add a consent mechanism that asks before setting it, make refusing as easy as accepting, and update this page with the date of the change.</p>
      <p>Questions about this policy: <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a>.</p>
"""),
]

write("legal/cookie-policy.html", legal_page(
    "cookie-policy", "Cookie policy",
    "What this website stores on your device. The short answer is: almost nothing, and nothing that tracks you.",
    cookies,
    "Riff Apps cookie policy. This site sets no advertising, analytics or tracking cookies and serves all assets from its own domain."))


# ===========================================================================
# GDPR
# ===========================================================================
gdpr = [
    ("scope", "Scope of this statement", f"""
      <p>This statement explains how {ENTITY} meets its obligations under the UK GDPR and the Data Protection Act 2018, and under the EU GDPR where it applies to our processing.</p>
      <p>It sits alongside our <a class="textlink" href="/legal/privacy-policy">privacy policy</a>, which describes the specific data we hold. This page is about the framework: our roles, your rights, and what we can evidence if you ask.</p>
"""),
    ("our-roles", "Controller or processor", """
      <p>We act in two capacities, and the distinction matters for where you direct a request.</p>
      <table>
        <thead><tr><th>Situation</th><th>Our role</th><th>Who to contact</th></tr></thead>
        <tbody>
          <tr><td>You enquire, or work with us as a client</td><td>Controller</td><td>Us</td></tr>
          <tr><td>We operate our own products</td><td>Controller</td><td>Us, via that product's notice</td></tr>
          <tr><td>We build or run an application for a client</td><td>Processor</td><td>That client, as controller</td></tr>
        </tbody>
      </table>
      <p>Where we are a processor, we act only on the controller's documented instructions, under a written agreement meeting Article 28. We will tell a controller if we think an instruction breaches data protection law.</p>
"""),
    ("principles", "How we apply the principles", """
      <p>The seven principles in Article 5 are not a poster on the wall; each one has a practical consequence in how we build.</p>
      <ul>
        <li><strong>Lawfulness, fairness and transparency</strong> &mdash; the lawful basis for a feature is identified and recorded before it is built, and users are told in plain language what happens to their data.</li>
        <li><strong>Purpose limitation</strong> &mdash; data collected for one purpose is not quietly repurposed for another.</li>
        <li><strong>Data minimisation</strong> &mdash; a feature gets the fields it needs and no more. Optional fields are genuinely optional.</li>
        <li><strong>Accuracy</strong> &mdash; users can correct their own details in the product wherever that is feasible.</li>
        <li><strong>Storage limitation</strong> &mdash; every category of data has a retention period set when it is first collected, and deletion is automated where possible.</li>
        <li><strong>Integrity and confidentiality</strong> &mdash; encryption, access control, logging and testing, proportionate to the sensitivity of the data.</li>
        <li><strong>Accountability</strong> &mdash; we keep records of processing, decisions and assessments, and can produce them.</li>
      </ul>
"""),
    ("lawful-bases", "Lawful bases", """
      <p>We rely on consent, contract, legal obligation and legitimate interests, depending on the processing. We do not use consent as a catch-all: where consent is the basis, it is specific, informed, given by a clear affirmative action, recorded, and as easy to withdraw as to give.</p>
      <p>Where we rely on legitimate interests, we carry out and document a balancing assessment weighing our interest against the rights of the people concerned. You can ask for a summary of any assessment that affects you.</p>
      <p>Special category data is processed only where an Article 9 condition applies, with additional safeguards and a documented policy where the Data Protection Act requires one.</p>
"""),
    ("your-rights", "Your rights in detail", """
      <table>
        <thead><tr><th>Right</th><th>What it means</th></tr></thead>
        <tbody>
          <tr><td>Access</td><td>A copy of your personal data and an explanation of how it is used.</td></tr>
          <tr><td>Rectification</td><td>Correction of data that is inaccurate or incomplete.</td></tr>
          <tr><td>Erasure</td><td>Deletion where the data is no longer needed, consent is withdrawn, or processing was unlawful.</td></tr>
          <tr><td>Restriction</td><td>Processing paused while a dispute about accuracy or legitimate interests is resolved.</td></tr>
          <tr><td>Portability</td><td>Data you gave us, in a structured, machine-readable format, transferable to another provider.</td></tr>
          <tr><td>Objection</td><td>A right to object to processing based on legitimate interests, and an absolute right to object to direct marketing.</td></tr>
          <tr><td>Automated decisions</td><td>Not to be subject to a solely automated decision with legal or similarly significant effect, and to obtain human intervention where one is made.</td></tr>
        </tbody>
      </table>
      <h3>How to exercise them</h3>
      <p>Email <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a>. No particular form of words is needed. We will acknowledge promptly and respond within one month, extendable by two further months for complex requests, in which case we will explain why within the first month.</p>
      <p>Requests are free. We may ask you to verify your identity before releasing data, and we may decline a request that is manifestly unfounded or excessive, explaining our reasoning and your right to complain.</p>
"""),
    ("automated-decisions", "Automated decisions and profiling", """
      <p>We design against solely automated decisions that have a legal or similarly significant effect on someone. Where a product scores, ranks, matches or classifies people, a human reviews any consequential outcome and can overturn it, and the person affected can ask for that review.</p>
      <p>Our <a class="textlink" href="/legal/ai-transparency">AI transparency statement</a> explains what the models do, how they are evaluated and where the human sits in each product.</p>
"""),
    ("dpia", "Impact assessments and privacy by design", """
      <p>We carry out a data protection impact assessment before processing that is likely to be high risk &mdash; including large-scale profiling, special category data, systematic monitoring, data about children, and the use of innovative technology such as AI in a new context.</p>
      <p>An assessment identifies the necessity and proportionality of the processing, the risks to individuals, and the measures taken to reduce them. Where a high risk remains after mitigation, we consult the Information Commissioner's Office before proceeding.</p>
      <p>Privacy by design means these questions are settled during architecture, not retrofitted. Default settings are the most privacy-protective ones.</p>
"""),
    ("processors", "Sub-processors", """
      <p>We use a small number of sub-processors, each engaged under a written contract imposing equivalent obligations to our own. Where we act as a processor for a client, we maintain a list of sub-processors for that engagement and give advance notice of any change, so the client has an opportunity to object.</p>
      <p>Ask us at any time for the current list relating to your engagement.</p>
"""),
    ("transfers", "International transfers", """
      <p>Transfers outside the UK rely on adequacy regulations where they exist. Otherwise we use the International Data Transfer Agreement, or the UK Addendum to the EU Standard Contractual Clauses, supported by a transfer risk assessment considering the law and practice of the destination country and any supplementary technical measures needed.</p>
"""),
    ("breach", "Personal data breaches", """
      <p>We maintain a breach response plan covering detection, containment, assessment, notification and review, and we keep an internal log of all breaches whether or not they are notifiable.</p>
      <p>As a controller, we notify the Information Commissioner's Office within 72 hours where a breach is likely to result in a risk to people's rights, and we notify affected individuals without undue delay where the risk is high. As a processor, we notify the controller without undue delay and support their response.</p>
"""),
    ("complaints", "Complaints", """
      <p>Raise a concern with us first at <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a>. You also have the right to complain to the Information Commissioner's Office (ico.org.uk), or to the supervisory authority in your EU member state where the EU GDPR applies, and to seek a judicial remedy.</p>
"""),
]

write("legal/gdpr.html", legal_page(
    "gdpr", "GDPR",
    "Our data protection framework: the roles we act in, the rights you hold, and what we can evidence if you ask.",
    gdpr,
    "Riff Apps GDPR statement: controller and processor roles, lawful bases, data subject rights, DPIAs, sub-processors, international transfers and breach handling."))


# ===========================================================================
# AI TRANSPARENCY
# ===========================================================================
ai = [
    ("why", "Why this page exists", """
      <p>We build products that use artificial intelligence. We think anyone affected by one should be able to find out, in plain language, what the technology is doing, what it is not allowed to decide, and how to challenge it.</p>
      <p>This statement covers our own products and the principles we apply to everything we build for clients. It is written to be readable by the people using our software, not only by their lawyers.</p>
"""),
    ("principles", "Our commitments", """
      <ul>
        <li><strong>Disclosure at the point of use.</strong> When you are interacting with AI or reading AI-generated content, the interface tells you there and then. Not once, buried in a policy.</li>
        <li><strong>No impersonation of a person.</strong> We do not build systems designed to make someone believe a machine is a human being.</li>
        <li><strong>A human decides what matters.</strong> Where an output affects money, safety, employment, learning outcomes or access to a service, a person reviews it and can overturn it.</li>
        <li><strong>Explainability.</strong> If a system scores, ranks or matches you, it shows the basis in terms you can understand.</li>
        <li><strong>Contestability.</strong> There is always a route to a human being who can look again.</li>
        <li><strong>Your content is not training data.</strong> We do not allow client or end-user content to be used to train third-party models.</li>
        <li><strong>Measured before it ships.</strong> AI features carry evaluation sets, documented failure modes and production monitoring.</li>
      </ul>
"""),
    ("where-we-use-ai", "Where AI is used in our products", """
      <h3>Riff</h3>
      <p>Riff uses models to match people on their answers, values and communication style, and to produce a compatibility score with a breakdown of why it was reached. It also offers AI companions &mdash; conversational personas available while real matches are found. These are labelled as AI throughout, and they are not presented as real users. Safety systems use automated detection to flag harmful behaviour; enforcement decisions that affect a person's account involve human review.</p>
      <h3>TeachWise AI</h3>
      <p>TeachWise generates and sequences learning material to build a curriculum around a stated goal. Generated content is checked for coherence and prerequisites before a learner sees it. Learning material can contain errors; it supplements rather than replaces qualified teaching, and learners are told the material is AI-generated.</p>
      <h3>Project controls (in development)</h3>
      <p>Our project controls application uses AI to read progress documents, reconcile them against a baseline, highlight variance and draft reporting narrative. It does not approve a forecast, a change or a payment. Every figure remains traceable to its source document and every report is signed off by a named person.</p>
      <h3>In our own work</h3>
      <p>We use AI assistance in writing code, drafting documentation and analysis. A human reviews everything before it reaches a client or production, and confidential material is never placed in tools outside an agreed processing arrangement.</p>
"""),
    ("how-it-works", "How these systems work", """
      <p>Our products use large language models and related machine learning systems provided by established third parties, accessed through their commercial APIs under terms that prohibit training on our data. We add retrieval over relevant content, structured prompting, tool use and validation of outputs before anything is shown to a user.</p>
      <p>We select models on capability, safety record and contractual terms, and we can change provider. Where the choice of provider materially affects how personal data is handled, that is disclosed in the relevant product privacy notice.</p>
"""),
    ("limitations", "Limitations you should know about", """
      <p>These systems have real and well-documented weaknesses. Being clear about them is part of using them responsibly.</p>
      <ul>
        <li><strong>They can be confidently wrong.</strong> A fluent, well-structured answer is not evidence of a correct one.</li>
        <li><strong>They can reflect bias</strong> present in training data, which can produce unequal outcomes across groups. We test for this and monitor it, and we do not claim it is solved.</li>
        <li><strong>They are not deterministic.</strong> The same input can produce different output.</li>
        <li><strong>They have knowledge limits</strong> and may be unaware of recent events unless given current information.</li>
        <li><strong>They are not a professional.</strong> Nothing our products generate is legal, medical, financial or safety-critical advice.</li>
      </ul>
"""),
    ("oversight", "Human oversight", """
      <p>Oversight is designed in rather than promised. For each AI feature we record what it does, the risk if it is wrong, who reviews the output, what that person can see in order to review it meaningfully, and what happens when they disagree.</p>
      <p>Reviewers can override an output, and overrides are logged and fed back into evaluation. A feature that cannot be meaningfully overseen is not a feature we ship in a consequential context.</p>
"""),
    ("governance", "How we govern changes", """
      <p>Prompts, models, retrieval sources and guardrails are version-controlled and change-managed like any other code. A change to an AI component runs against the evaluation set before release, and a regression blocks the release.</p>
      <p>Each AI feature has documentation covering its intended use, the data it draws on, its known limitations, its evaluation results and its oversight design. Clients receive this for features we build for them.</p>
      <p>We follow the direction of travel in UK regulatory guidance and the EU AI Act &mdash; risk-based classification, transparency for systems people interact with, human oversight for high-risk uses, and technical documentation &mdash; and we assess each product against the obligations that apply to it.</p>
"""),
    ("your-choices", "Your choices", """
      <p>You can ask whether AI was involved in an output that affects you, ask for the reasoning behind it, ask a human to review it, and object to processing as described in our <a class="textlink" href="/legal/gdpr">GDPR statement</a>.</p>
      <p>To do any of that, or to report an output you believe is wrong or harmful, email <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a>. Reports of harmful output are treated as defects and investigated.</p>
"""),
]

write("legal/ai-transparency.html", legal_page(
    "ai-transparency", "AI transparency",
    "Where we use artificial intelligence, what it decides, what it does not, and how you can challenge an output.",
    ai,
    "Riff Apps AI transparency statement: where AI is used across our products, its limitations, human oversight, governance of changes and your right to challenge an output."))


# ===========================================================================
# ACCEPTABLE USE
# ===========================================================================
aup = [
    ("scope", "Who this applies to", """
      <p>This policy applies to this website, to any application or service we operate, and to work we carry out for clients. It forms part of our <a class="textlink" href="/legal/terms-of-service">terms of service</a>.</p>
      <p>It is written broadly on purpose. The intention is simple: our software should not be used to harm people.</p>
"""),
    ("prohibited", "What you must not do", """
      <h3>Unlawful activity</h3>
      <ul>
        <li>Break any applicable law, regulation or court order.</li>
        <li>Infringe intellectual property, trade secrets or confidentiality obligations.</li>
        <li>Facilitate fraud, money laundering, sanctions evasion or the sale of prohibited goods.</li>
      </ul>
      <h3>Harm to people</h3>
      <ul>
        <li>Harass, threaten, stalk, bully or intimidate anyone.</li>
        <li>Publish material that is defamatory, or that incites violence or hatred against people on the basis of a protected characteristic.</li>
        <li>Share sexual content involving minors, or any content that sexualises a child. We report this to the authorities without exception.</li>
        <li>Share intimate images of anyone without their consent.</li>
        <li>Encourage self-harm, suicide or disordered eating.</li>
      </ul>
      <h3>Deception</h3>
      <ul>
        <li>Impersonate another person or organisation, or misrepresent your identity, age or affiliation.</li>
        <li>Create fake accounts, manipulate verification, or evade a suspension.</li>
        <li>Send spam or unsolicited bulk messages.</li>
      </ul>
      <h3>Technical abuse</h3>
      <ul>
        <li>Probe, scan or test the security of a system without written permission.</li>
        <li>Introduce malware, attempt denial of service, or interfere with availability for others.</li>
        <li>Access accounts or data you are not authorised to access.</li>
        <li>Scrape at scale, circumvent rate limits, or reverse-engineer a service except where the law expressly permits it.</li>
      </ul>
"""),
    ("ai-specific", "Specific to AI features", """
      <ul>
        <li>Do not use AI features to generate content that sexualises minors, that incites violence, or that helps someone commit a crime.</li>
        <li>Do not use generated material to impersonate a real person or to create deceptive media of them.</li>
        <li>Do not attempt to bypass safety measures, extract system prompts, or manipulate a model into behaviour this policy prohibits.</li>
        <li>Do not present AI-generated output as human-written where doing so would mislead someone to their detriment.</li>
        <li>Do not feed personal data into an AI feature without a lawful basis for doing so.</li>
      </ul>
"""),
    ("client-work", "Work we will not take on", """
      <p>We decline engagements where the purpose of the software conflicts with this policy. In practice that includes systems built for mass surveillance of a population, tools designed to deceive people about who or what they are talking to, dark patterns engineered to extract consent or money, and anything unlawful.</p>
      <p>If this only becomes apparent after work has started, we will raise it and, if it cannot be resolved, end the engagement under our terms.</p>
"""),
    ("enforcement", "Enforcement", """
      <p>Where we operate the service, we may remove content, suspend or terminate access, and report the matter to law enforcement. We act proportionately: a warning for a first minor breach, immediate removal where there is a risk to someone's safety.</p>
      <p>Where a suspension affects your account and you believe it was wrong, you can appeal to <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a> and a person will review the decision.</p>
"""),
    ("reporting", "Reporting a problem", """
      <p>To report a breach of this policy, email <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a> with what you saw, where, and when. Reports involving a risk to someone's safety are prioritised.</p>
      <h3>Security researchers</h3>
      <p>If you believe you have found a vulnerability, tell us at the same address before disclosing it publicly. Give us reasonable time to fix it, do not access or alter data belonging to others, and do not degrade the service while testing. We will not pursue legal action against researchers who act in that spirit, and we will credit you if you would like us to.</p>
      <h3>Child sexual abuse material</h3>
      <p>Report it to us, and also to the Internet Watch Foundation in the UK or to your local law enforcement. We remove it immediately and report it to the relevant authorities.</p>
"""),
]

write("legal/acceptable-use.html", legal_page(
    "acceptable-use", "Acceptable use",
    "What our websites, products and services may not be used for &mdash; and the work we will not take on.",
    aup,
    "Riff Apps acceptable use policy: prohibited activity across our websites and products, AI-specific restrictions, enforcement and how to report a problem."))


# ===========================================================================
# LAW ENFORCEMENT
# ===========================================================================
law = [
    ("purpose", "Purpose of these guidelines", f"""
      <p>These guidelines are for law enforcement agencies and other authorities seeking data from {ENTITY}. They explain what we need in order to act, and what we will and will not do.</p>
      <p>We take both obligations seriously: cooperating properly with lawful investigations, and protecting our users from disclosure that is not lawfully required.</p>
      <p>This page is not legal advice and does not waive any right or defence available to us or to the people whose data we hold.</p>
"""),
    ("contact", "How to reach us", """
      <p>Send requests to <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a> with &ldquo;Law enforcement request&rdquo; in the subject line.</p>
      <p>Requests must come from an official government or agency email address and be on headed paper, signed and dated. We do not accept requests by telephone or social media, and we cannot verify a request made from a personal account.</p>
"""),
    ("what-we-require", "What a valid request needs", """
      <p>We disclose data only where we are legally compelled to, or where a narrow emergency exception applies. Please include:</p>
      <ul>
        <li>the legal instrument relied on &mdash; for UK requests, typically a court order, warrant, or a notice under the Investigatory Powers Act 2018 or Schedule 2 of the Data Protection Act 2018;</li>
        <li>the identity, rank and contact details of the requesting officer, and the agency and case reference;</li>
        <li>precise identifiers for the account or data sought &mdash; a username, registered email address, or transaction reference. We cannot act on a name alone;</li>
        <li>a defined date range, kept as narrow as the investigation allows;</li>
        <li>the specific categories of data sought, rather than a request for &ldquo;all data&rdquo;;</li>
        <li>whether you are asking us to delay notifying the user, and the legal basis for that.</li>
      </ul>
      <p>We will reject or seek clarification on requests that are overly broad, unclear, or unsupported by valid legal process.</p>
"""),
    ("international", "Requests from outside the UK", """
      <p>We are based in the UK and respond to UK legal process. Authorities in other jurisdictions should proceed through a mutual legal assistance treaty, a letter rogatory, or another recognised international cooperation route, so that the request is given effect under UK law.</p>
      <p>We will consider a direct request from an overseas authority where a specific legal framework permits it, but we are not obliged to comply with foreign process that has no effect in the UK.</p>
"""),
    ("emergency", "Emergency disclosure", """
      <p>Where we believe in good faith that disclosure is necessary to prevent an imminent risk of death or serious physical harm, we may disclose the minimum information needed without waiting for legal process.</p>
      <p>Mark the request &ldquo;Emergency disclosure request&rdquo; and set out the nature of the emergency, the risk of harm, the person at risk, and why the information will help prevent it. We assess each on its facts and may decline if the threshold is not met.</p>
"""),
    ("preservation", "Preservation requests", """
      <p>We will preserve data we already hold pending valid legal process, typically for 90 days and extendable once on request. A preservation request does not itself require us to disclose anything, and it does not require us to begin collecting data we do not otherwise hold.</p>
"""),
    ("what-we-hold", "What we may hold", """
      <p>What exists varies by product and is limited by our retention schedules. Depending on the service, it may include registration details, an account's activity metadata, and records of transactions.</p>
      <p>Several things are usually <strong>not</strong> available:</p>
      <ul>
        <li>data already deleted under our retention policy &mdash; we cannot recover it;</li>
        <li>content protected by encryption we cannot reverse;</li>
        <li>data held by a client for whom we act as processor. Direct those requests to the client, who is the controller. We will tell you that is the position, and will tell the client.</li>
      </ul>
      <p>We do not build capabilities for bulk or indiscriminate access, and we will not create new collection to satisfy a request.</p>
"""),
    ("notifying-users", "Telling the user", """
      <p>Our policy is to notify a person whose data has been requested, with enough information to seek legal advice, before we disclose it.</p>
      <p>We will delay or withhold notice where a court order or statute prohibits it, or where we believe notice would create a risk of serious harm to someone or of destruction of evidence. Where notice is delayed by order, we will normally notify once the restriction expires.</p>
"""),
    ("process", "How we handle requests", """
      <p>Each request is logged and reviewed for validity and scope, with legal advice where needed. Valid requests are answered as promptly as we can, usually within 10 working days, and urgent matters faster. Where we disclose, we provide only the data the request covers.</p>
      <p>We keep records of the requests we receive and how we responded, and we may publish aggregate figures about their number and type.</p>
"""),
]

write("legal/law-enforcement.html", legal_page(
    "law-enforcement", "Law enforcement",
    "How authorities should request data from Riff Apps, what a valid request needs, and what we will and will not disclose.",
    law,
    "Riff Apps law enforcement guidelines: how to submit a valid request, requirements, emergency disclosure, preservation, and our policy on notifying users."))


# ===========================================================================
# REFUND POLICY
# ===========================================================================
refund = [
    ("overview", "Overview", """
      <p>Different things we do are refunded differently. Find the section that matches what you paid for.</p>
      <p>Whatever the category, we would rather fix a problem than argue about a refund. If something we delivered is not right, tell us at <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a> and we will look at it properly.</p>
"""),
    ("development", "Development projects", """
      <h3>Discovery sprints</h3>
      <p>Discovery is paid in advance. You may cancel before it starts for a full refund. Once it has started, the fee covers time already spent; if you cancel mid-sprint we refund the unstarted portion on a pro-rata basis and you keep everything produced up to that point.</p>
      <h3>Fixed-scope builds</h3>
      <p>Fixed-scope work is invoiced against milestones. Each milestone is payable when its deliverables meet the acceptance criteria in the statement of work.</p>
      <ul>
        <li>A deposit secures your place in our schedule. It is refundable up to 14 days before the agreed start date, and non-refundable after that, because we will have turned other work away.</li>
        <li>If you cancel mid-project, you pay for work completed and accepted, plus committed costs we cannot recover. Anything paid beyond that is refunded within 30 days.</li>
        <li>If a delivered milestone does not meet its acceptance criteria, we correct it at our cost. If we cannot, that milestone's fee is refunded.</li>
      </ul>
      <h3>Retainers</h3>
      <p>Retainers are billed monthly in advance and cancellable with 30 days' written notice. We do not refund part months, and unused hours do not roll over unless your agreement says they do.</p>
"""),
    ("consumers", "If you are a consumer", """
      <p>Where you buy from us as a consumer rather than a business, you have a statutory right under the Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013 to cancel a distance contract within 14 days of entering it, without giving a reason.</p>
      <p>If you ask us to start work during that period and then cancel, you pay a proportion of the price reflecting what has been delivered. Where a digital service is fully performed within the 14 days with your express agreement and acknowledgement that you lose the right to cancel, the right does not apply.</p>
      <p>Your rights under the Consumer Rights Act 2015 &mdash; that services are performed with reasonable care and skill, and that digital content is of satisfactory quality, fit for purpose and as described &mdash; are not affected by anything in this policy.</p>
"""),
    ("subscriptions", "Product subscriptions", """
      <p>Subscriptions to products we operate are covered by that product's own terms, which take precedence for those purchases. As a general position:</p>
      <ul>
        <li>Subscriptions renew automatically until cancelled. Cancel any time and you keep access to the end of the paid period.</li>
        <li>We do not refund part periods once a billing period has begun, unless the law requires it or the service failed materially.</li>
        <li>Where a free trial is offered, cancelling before it ends means you are not charged.</li>
        <li>If we withdraw a paid feature you are actively paying for, we will refund fairly for the remaining paid period.</li>
      </ul>
      <div class="callout">
        <p><strong>Bought through an app store?</strong> Purchases made through Apple's App Store or Google Play are processed by those companies under their own refund rules, and we cannot issue those refunds ourselves. Request them through Apple or Google. Tell us as well &mdash; we will support a reasonable claim.</p>
      </div>
"""),
    ("not-refundable", "What is not refundable", """
      <ul>
        <li>Work completed and accepted in line with the agreed acceptance criteria.</li>
        <li>Third-party costs already incurred on your behalf &mdash; licences, app store fees, domains, cloud usage.</li>
        <li>Delay or cancellation caused by information, approvals or access we were waiting on from you.</li>
        <li>A change of mind about the commercial direction of a product that was built to specification.</li>
        <li>Dissatisfaction with output that meets the agreed specification, where no change request was raised.</li>
      </ul>
"""),
    ("how-to-request", "How to request a refund", """
      <p>Email <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a> with the invoice or order reference, what you paid for, and why you are requesting a refund.</p>
      <p>We acknowledge within 2 working days and decide within 10 working days, asking for more detail if we need it. Approved refunds are paid to the original payment method within 14 days of the decision, and card refunds may take a few days longer to appear.</p>
"""),
    ("disputes", "If you disagree with our decision", """
      <p>Ask for it to be reviewed and a different person will look at it. If we still cannot agree, we will attempt to resolve the matter in good faith and will consider mediation before either party starts proceedings.</p>
      <p>Nothing here limits your statutory rights or your right to pursue a claim. This policy is governed by the law of England and Wales.</p>
"""),
]

write("legal/refund-policy.html", legal_page(
    "refund-policy", "Refund policy",
    "Cancellations, refunds and billing for development projects, retainers and product subscriptions.",
    refund,
    "Riff Apps refund policy covering discovery sprints, fixed-scope builds, retainers, consumer cancellation rights, subscriptions and app store purchases."))


# ===========================================================================
# LEGAL INDEX
# ===========================================================================
cards = "\n".join(
    f'      <a class="legal-card" href="/legal/{slug}"><strong>{label}</strong><span>{desc}</span></a>'
    for slug, label, desc in LEGAL
)

LEGAL_INDEX = f"""
<section class="doc-head">
  <div class="shell">
    <h1>Legal</h1>
    <p class="lede">Our policies, written to say what we actually do. If anything here is unclear, ask us and we will explain it.</p>
    <p class="doc-updated">Last reviewed {UPDATED}</p>
  </div>
</section>
<hr class="rule">

<section class="band band-paper">
  <div class="shell">
    <div class="legal-index">
{cards}
    </div>
    <div class="callout" style="margin-top:2.5rem">
      <p><strong>Products have their own policies.</strong> Riff and TeachWise AI are separate services with their own privacy notices, terms and cookie controls. The policies on this page cover riff-apps.com and our client work.</p>
      <p>Questions about any of this: <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a>.</p>
    </div>
  </div>
</section>
"""

write("legal/index.html", page(
    "Legal — Riff Apps",
    "Privacy policy, terms of service, cookie policy, GDPR statement, AI transparency, acceptable use, law enforcement guidelines and refund policy.",
    "/legal", LEGAL_INDEX, css_depth=1))
