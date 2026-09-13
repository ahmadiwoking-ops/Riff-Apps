import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shell import page  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel)


ICON = {
    "app": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18.5h2"/></svg>',
    "ai": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.2"/><path d="M12 2v3.2M12 18.8V22M2 12h3.2M18.8 12H22M5 5l2.3 2.3M16.7 16.7 19 19M19 5l-2.3 2.3M7.3 16.7 5 19"/></svg>',
    "data": '<svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="6" rx="7.5" ry="3"/><path d="M4.5 6v12c0 1.7 3.4 3 7.5 3s7.5-1.3 7.5-3V6"/><path d="M4.5 12c0 1.7 3.4 3 7.5 3s7.5-1.3 7.5-3"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5 4.5 6v6c0 4.6 3.2 8.4 7.5 9.5 4.3-1.1 7.5-4.9 7.5-9.5V6Z"/><path d="m9 12 2.2 2.2L15.5 10"/></svg>',
    "run": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.5a8.5 8.5 0 1 1-6 2.5"/><path d="M6 2.5v4h4"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>',
}


def chip(kind, colour):
    return f'<span class="tile-chip {colour}" aria-hidden="true">{ICON[kind]}</span>'


# ===========================================================================
# HOME
# ===========================================================================
HOME = """
<section class="hero">
  <div class="shell hero-grid">
    <div>
      <h1>We build AI apps<br><span class="light">that hold up to scrutiny.</span></h1>
      <p class="lede">Riff Apps is a UK studio. We take an idea from first sketch to a product people use every day &mdash; with data protection, accessibility and AI governance designed in from the first sprint, not bolted on the week before launch.</p>
      <div class="btn-row">
        <a class="btn" href="/contact">Start a project</a>
        <a class="btn btn-ghost" href="/work">See what we&rsquo;ve built</a>
      </div>
      <dl class="hero-stats">
        <div>
          <dt>Riff</dt>
          <span>Social app, live on iOS and Android</span>
        </div>
        <div>
          <dt>TeachWise AI</dt>
          <span>Personalised curricula, live on the web</span>
        </div>
        <div>
          <dt>Project controls</dt>
          <span>In build for the energy sector</span>
        </div>
      </dl>
    </div>
    <div class="hero-canvas-wrap">
      <canvas id="hero-canvas" role="img" aria-label="Animated grid of app tiles rippling in the Riff Apps brand colours"></canvas>
      <img class="hero-mark" src="./assets/img/riff-mark.png" alt="" width="240" height="201">
    </div>
  </div>
</section>

<hr class="rule">

<section class="band band-deep">
  <div class="shell">
    <div class="section-head">
      <h2>What we build</h2>
      <p>Five things, done properly, rather than a list of everything. Most engagements combine two or three.</p>
    </div>
    <div class="tile-set">
      <article class="tile tile-wide">
        CHIP_APP
        <h3>Product applications</h3>
        <p>Web and native mobile apps, from first prototype to the App Store and Google Play. React, Next.js and TypeScript, shipped on infrastructure you own and can hand to another team if you ever need to.</p>
      </article>
      <article class="tile tile-wide">
        CHIP_AI
        <h3>AI features that earn their place</h3>
        <p>Conversational assistants, generated content, matching and classification &mdash; built on current frontier models, with evaluation, guardrails and a human path for anything consequential.</p>
      </article>
      <article class="tile">
        CHIP_DATA
        <h3>Data and integrations</h3>
        <p>Schema design, migrations, and connections into the systems your business already runs on.</p>
      </article>
      <article class="tile">
        CHIP_SHIELD
        <h3>Governance and assurance</h3>
        <p>DPIAs, records of processing, model documentation and accessibility audits, produced as the work happens.</p>
      </article>
      <article class="tile">
        CHIP_RUN
        <h3>Run and improve</h3>
        <p>Monitoring, incident response, security patching and a steady release cadence after launch.</p>
      </article>
    </div>
  </div>
</section>

<section class="band band-paper">
  <div class="shell">
    <div class="section-head">
      <h2>Selected work</h2>
      <p>Two products live, one in build. Each one shipped end to end by the same team.</p>
    </div>

    <article class="project">
      <div>
        <h3>Riff</h3>
        <p>A social app that connects people through questions, voice and trust instead of photos and endless scrolling. Twenty&#8209;five questions across values, goals and communication style feed a compatibility model; faces are revealed only when both people are ready.</p>
        <p>It carries the harder parts too &mdash; three&#8209;tier ID verification, liveness checks, encrypted voice and media, and a layered safety system watching for harmful behaviour.</p>
        <div class="project-meta">
          <span class="pill pill-live">Live</span>
          <span class="pill">iOS and Android</span>
          <span class="pill">AI matching</span>
          <span class="pill">ID verification</span>
        </div>
        <a class="textlink" href="https://riff-app.co.uk" rel="noopener">Visit riff-app.co.uk</a>
      </div>
      <div class="frame">
        <div class="frame-rows">
          <div class="frame-row"><i style="background:var(--cyan)"></i> Compatibility <span>4&#8209;layer score</span></div>
          <div class="frame-row"><i style="background:var(--violet)"></i> Voice note <span>0:42</span></div>
          <div class="frame-row"><i style="background:var(--green)"></i> Verification <span>Green</span></div>
          <div class="frame-row"><i style="background:var(--blue)"></i> Reveal <span>Both ready</span></div>
        </div>
      </div>
    </article>

    <article class="project">
      <div>
        <h3>TeachWise AI</h3>
        <p>A learning platform that builds a curriculum for whatever someone needs to learn next. Rather than handing over a fixed course catalogue, it assembles a structured path around a learner&rsquo;s goal and moves with them as they progress.</p>
        <p>The interesting engineering is in keeping generated material coherent across a whole syllabus &mdash; sequencing, prerequisites and consistency between lessons, not just good output one prompt at a time.</p>
        <div class="project-meta">
          <span class="pill pill-live">Live</span>
          <span class="pill">Web</span>
          <span class="pill">Generated curricula</span>
          <span class="pill">Adaptive paths</span>
        </div>
        <a class="textlink" href="https://teachwise-ai.com" rel="noopener">Visit teachwise-ai.com</a>
      </div>
      <div class="frame">
        <div class="frame-rows">
          <div class="frame-row"><i style="background:var(--blue)"></i> Goal <span>Set</span></div>
          <div class="frame-row"><i style="background:var(--indigo)"></i> Curriculum <span>9 modules</span></div>
          <div class="frame-row"><i style="background:var(--amber)"></i> Progress <div class="frame-bar"><i></i></div></div>
          <div class="frame-row"><i style="background:var(--green)"></i> Next lesson <span>Ready</span></div>
        </div>
      </div>
    </article>

    <p style="margin-top:2rem"><a class="btn btn-ghost" href="/work">All projects, including what&rsquo;s next</a></p>
  </div>
</section>

<hr class="rule">

<section class="band">
  <div class="shell">
    <div class="section-head">
      <h2>Coming next: project controls for energy</h2>
      <p>Our current build is a project controls application for the energy sector, with the same approach heading into adjacent industries.</p>
    </div>
    <div class="project" style="padding-top:0">
      <div>
        <p>Capital projects in energy run on cost, schedule, change and risk data that usually lives in a dozen spreadsheets and one very tired planner&rsquo;s head. We&rsquo;re building a single application that holds the baseline, tracks progress against it, and explains variance in plain language.</p>
        <p>AI does the reading &mdash; parsing progress reports, flagging drift, drafting the narrative for a monthly review &mdash; while every number stays traceable to its source and every forecast stays something a human signs off. The same core suits construction, utilities, infrastructure and manufacturing, and we&rsquo;re talking to teams in each.</p>
        <div class="project-meta">
          <span class="pill pill-build">In build</span>
          <span class="pill">Energy sector</span>
          <span class="pill">Cost and schedule</span>
          <span class="pill">Earned value</span>
        </div>
        <a class="textlink" href="/contact">Talk to us about an early pilot</a>
      </div>
      <div class="frame">
        <div class="frame-rows">
          <div class="frame-row"><i style="background:var(--cyan)"></i> Cost performance <span>CPI 0.97</span></div>
          <div class="frame-row"><i style="background:var(--amber)"></i> Schedule float <span>4 weeks</span></div>
          <div class="frame-row"><i style="background:var(--violet)"></i> Open changes <span>12</span></div>
          <div class="frame-row"><i style="background:var(--green)"></i> Forecast <span>Signed off</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band band-paper">
  <div class="shell">
    <div class="section-head">
      <h2>How a project runs</h2>
      <p>Short cycles, working software early, and the compliance paperwork produced alongside the build rather than after it.</p>
    </div>
    <div class="steps">
      <div class="step">
        <div>
          <h3>Frame the problem</h3>
          <p>A week or two of discovery: who the users are, what decision or task the product has to improve, what data exists, and what the regulatory picture looks like. You get a scope, a budget and a risk register &mdash; and an honest answer if we think the idea needs changing.</p>
        </div>
      </div>
      <div class="step">
        <div>
          <h3>Prototype something clickable</h3>
          <p>A working prototype in front of real users before the architecture is locked in. It is far cheaper to discover a flawed assumption in a prototype than in production.</p>
        </div>
      </div>
      <div class="step">
        <div>
          <h3>Build in two&#8209;week cycles</h3>
          <p>Every cycle ends with something deployed to a staging environment you can use. Weekly written updates, a live board, and no surprises at the end of the month.</p>
        </div>
      </div>
      <div class="step">
        <div>
          <h3>Assure before launch</h3>
          <p>Accessibility testing against WCAG 2.2 AA, a security review, penetration testing where the risk warrants it, a data protection impact assessment, and model evaluations for any AI feature that affects users.</p>
        </div>
      </div>
      <div class="step">
        <div>
          <h3>Run it, then improve it</h3>
          <p>Monitoring, alerting, dependency patching and a regular release rhythm. Most of our work is with clients we launched for a year or more ago.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<hr class="rule">

<section class="band band-deep">
  <div class="shell">
    <div class="section-head">
      <h2>Governance is part of the build</h2>
      <p>Anyone can add an AI feature. The work is making it defensible to a regulator, a board and the person on the other end of it.</p>
    </div>
    <div class="tile-set">
      <article class="tile tile-wide">
        <h3>People know when they&rsquo;re talking to AI</h3>
        <p>Generated content and AI participants are labelled in the interface, every time. We don&rsquo;t build products that pass off a model as a person.</p>
      </article>
      <article class="tile tile-wide">
        <h3>Consequential decisions keep a human</h3>
        <p>Where an output affects someone&rsquo;s money, safety, learning or access to a service, a person reviews it and can overturn it. That route is designed in, not promised in a policy.</p>
      </article>
      <article class="tile">
        <h3>Data minimised by default</h3>
        <p>We collect what a feature needs, keep it for a stated period, and document the lawful basis before we write the code.</p>
      </article>
      <article class="tile">
        <h3>Evaluated, not assumed</h3>
        <p>AI features ship with test sets, measured failure modes and monitoring, so quality is a number rather than a feeling.</p>
      </article>
      <article class="tile">
        <h3>Accessible as standard</h3>
        <p>WCAG 2.2 AA is the baseline for everything we deliver, tested with a keyboard and a screen reader.</p>
      </article>
    </div>
    <p style="margin-top:2rem"><a class="btn btn-ghost" href="/governance">Read our governance approach</a></p>
  </div>
</section>

<section class="band">
  <div class="shell">
    <div class="cta">
      <div>
        <h2>Tell us what you&rsquo;re trying to build</h2>
        <p>An idea on the back of an envelope, a prototype that needs finishing, or a platform that needs to pass an audit &mdash; we&rsquo;ll tell you honestly whether we&rsquo;re the right team for it.</p>
      </div>
      <div class="btn-row">
        <a class="btn" href="/contact">Start a project</a>
        <a class="btn btn-ghost" href="mailto:Contact@Riff-Apps.com">Email us</a>
      </div>
    </div>
  </div>
</section>
"""

HOME = (HOME
        .replace("CHIP_APP", chip("app", "c-cyan"))
        .replace("CHIP_AI", chip("ai", "c-violet"))
        .replace("CHIP_DATA", chip("data", "c-blue"))
        .replace("CHIP_SHIELD", chip("shield", "c-green"))
        .replace("CHIP_RUN", chip("run", "c-amber")))

write("index.html", page(
    "Riff Apps — AI-powered application development, built on solid governance",
    "Riff Apps is a UK studio building AI-powered web and mobile applications, with data protection, accessibility and AI governance designed in from the first sprint.",
    "/", HOME, current="/",
    scripts='<script src="./assets/js/hero.js" defer></script>\n'))


# ===========================================================================
# SERVICES
# ===========================================================================
SERVICES = """
<section class="doc-head">
  <div class="shell">
    <h1>Services</h1>
    <p class="lede">We work as a small senior team on a handful of projects at a time. That means you get the people who scoped the work actually building it.</p>
  </div>
</section>
<hr class="rule">

<section class="band">
  <div class="shell stack-lg">
    <div class="project" style="padding-top:0">
      <div>
        <h2>Application development</h2>
        <p>Web applications and native mobile apps, built with React, Next.js, TypeScript and a Postgres&#8209;shaped data layer. We ship to the App Store, Google Play and the web, and we set up the deployment pipeline so releases are routine rather than an event.</p>
        <p>Everything is written to be handed over. Documented architecture, readable code, infrastructure as configuration and accounts in your name &mdash; so you are never locked into us by accident.</p>
      </div>
      <div class="frame">
        <div class="frame-rows">
          <div class="frame-row"><i style="background:var(--cyan)"></i> Discovery and scope <span>1&ndash;2 weeks</span></div>
          <div class="frame-row"><i style="background:var(--blue)"></i> Prototype <span>2&ndash;3 weeks</span></div>
          <div class="frame-row"><i style="background:var(--violet)"></i> Build cycles <span>2 weeks each</span></div>
          <div class="frame-row"><i style="background:var(--green)"></i> Launch and run <span>Ongoing</span></div>
        </div>
      </div>
    </div>

    <hr class="rule-soft">

    <div>
      <div class="section-head">
        <h2>AI engineering</h2>
        <p>We use current frontier models where they genuinely improve the product, and say so plainly when they don&rsquo;t.</p>
      </div>
      <div class="tile-set">
        <article class="tile tile-wide">
          <h3>Assistants and conversation</h3>
          <p>Assistants that hold context, use your data through retrieval, and call real tools rather than guessing. Built with explicit limits on what they can see and do.</p>
        </article>
        <article class="tile tile-wide">
          <h3>Generation with structure</h3>
          <p>Generated documents, lessons, summaries and reports that stay coherent across a whole body of work &mdash; the hard part is consistency, not a single good output.</p>
        </article>
        <article class="tile">
          <h3>Matching and classification</h3>
          <p>Scoring, ranking and routing, with the reasoning surfaced so a user can see why they got a result.</p>
        </article>
        <article class="tile">
          <h3>Evaluation harnesses</h3>
          <p>Test sets and scoring that run in CI, so a prompt or model change can&rsquo;t quietly degrade quality.</p>
        </article>
        <article class="tile">
          <h3>Guardrails and fallbacks</h3>
          <p>Input and output filtering, rate limits, cost ceilings and a defined behaviour for when a model is unavailable.</p>
        </article>
      </div>
    </div>

    <hr class="rule-soft">

    <div>
      <div class="section-head">
        <h2>Governance and assurance</h2>
        <p>Available inside a build, or on its own if you have a product already live and a deadline approaching.</p>
      </div>
      <div class="tile-set">
        <article class="tile">
          <h3>Data protection</h3>
          <p>Records of processing, lawful basis, DPIAs, retention schedules and subject access handling.</p>
        </article>
        <article class="tile">
          <h3>AI documentation</h3>
          <p>Model cards, intended use, known limitations, human oversight design and an audit trail of changes.</p>
        </article>
        <article class="tile">
          <h3>Accessibility</h3>
          <p>WCAG 2.2 AA audit with a prioritised remediation plan and retesting after the fixes land.</p>
        </article>
        <article class="tile tile-wide">
          <h3>Security review</h3>
          <p>Threat modelling, dependency and secrets auditing, authentication and authorisation review, and coordination of third&#8209;party penetration testing where the risk profile calls for it.</p>
        </article>
        <article class="tile tile-wide">
          <h3>Policy set for launch</h3>
          <p>The public documents a product needs on day one &mdash; privacy, terms, cookies, acceptable use, AI transparency &mdash; written to match what the software actually does, then reviewed by your legal advisers.</p>
        </article>
      </div>
    </div>

    <hr class="rule-soft">

    <div>
      <div class="section-head">
        <h2>How we charge</h2>
        <p>Three ways of working. We&rsquo;ll recommend the one that fits the certainty of your scope, not the one that bills most.</p>
      </div>
      <div class="tile-set">
        <article class="tile">
          <h3>Discovery sprint</h3>
          <p>Fixed price, one to two weeks. Scope, prototype, technical approach and a costed plan. You keep everything whether or not you continue with us.</p>
        </article>
        <article class="tile">
          <h3>Fixed&#8209;scope build</h3>
          <p>A defined product for a defined price, staged across milestones. Best once discovery has removed the big unknowns.</p>
        </article>
        <article class="tile">
          <h3>Ongoing team</h3>
          <p>A monthly retainer for continuous development, support and improvement after launch. Cancellable with notice.</p>
        </article>
      </div>
    </div>

    <div class="cta">
      <div>
        <h2>Not sure which you need?</h2>
        <p>Send a paragraph about the problem. We&rsquo;ll reply with what we&rsquo;d do first and a rough range, at no cost.</p>
      </div>
      <div class="btn-row"><a class="btn" href="/contact">Get in touch</a></div>
    </div>
  </div>
</section>
"""

write("services.html", page(
    "Services — Riff Apps",
    "Application development, AI engineering, and governance and assurance for teams building software that has to stand up to scrutiny.",
    "/services", SERVICES, current="/services"))


# ===========================================================================
# WORK
# ===========================================================================
WORK = """
<section class="doc-head">
  <div class="shell">
    <h1>Work</h1>
    <p class="lede">Two products live and one in build. Each was designed, engineered, launched and is still run by the same team.</p>
  </div>
</section>
<hr class="rule">

<section class="band band-paper">
  <div class="shell">
    <article class="project" id="riff" style="padding-top:0">
      <div>
        <span class="pill pill-live">Live on iOS and Android</span>
        <h3 style="margin-top:1rem">Riff</h3>
        <p>Most social apps ask you to judge a photograph. Riff asks twenty&#8209;five questions instead &mdash; about values, goals, perspective and how you communicate &mdash; then matches people on how they think rather than how they look. Conversation starts in text and voice; faces appear only when both people tap ready, at the same moment, so nobody holds the power in the exchange.</p>
        <p>Two modes run in parallel: a one&#8209;to&#8209;one Deep Connection aimed at mentors and collaborators, and a four&#8209;person Friend Circle built around shared ambition. AI companions keep new users company while real matches are found, and they are labelled as AI throughout.</p>
        <h3 style="font-size:1.15rem;margin-top:1.6rem">What made it hard</h3>
        <p>Trust. The product only works if everyone is real, so it carries government ID and live selfie verification, liveness checks with blink and head&#8209;turn capture, a visible trust score, encryption of voice and media in transit and at rest, and a layered detection system for harmful behaviour. Subscriptions, App Store and Play billing, and the full public policy set shipped with it.</p>
        <div class="project-meta">
          <span class="pill">React Native</span>
          <span class="pill">Compatibility modelling</span>
          <span class="pill">ID verification</span>
          <span class="pill">Voice</span>
          <span class="pill">Subscriptions</span>
        </div>
        <a class="textlink" href="https://riff-app.co.uk" rel="noopener">Visit riff-app.co.uk</a>
      </div>
      <div class="frame">
        <div class="frame-rows">
          <div class="frame-row"><i style="background:var(--cyan)"></i> Questions answered <span>25 of 25</span></div>
          <div class="frame-row"><i style="background:var(--indigo)"></i> Compatibility <span>4&#8209;layer score</span></div>
          <div class="frame-row"><i style="background:var(--violet)"></i> Voice note <span>0:42</span></div>
          <div class="frame-row"><i style="background:var(--green)"></i> Verification <span>Green</span></div>
          <div class="frame-row"><i style="background:var(--amber)"></i> AI companion <span>Labelled</span></div>
          <div class="frame-row"><i style="background:var(--blue)"></i> Reveal <span>Both ready</span></div>
        </div>
      </div>
    </article>
  </div>
</section>

<section class="band">
  <div class="shell">
    <article class="project" id="teachwise" style="padding-top:0">
      <div>
        <span class="pill pill-live">Live on the web</span>
        <h3 style="margin-top:1rem">TeachWise AI</h3>
        <p>A curriculum for whatever you need to learn next. Instead of a catalogue of fixed courses, TeachWise assembles a structured path around the thing a learner is actually trying to do, then adapts it as they work through it.</p>
        <p>Generating a single good lesson is easy now. Generating forty that build on each other &mdash; without repeating themselves, contradicting each other or assuming knowledge that hasn&rsquo;t been taught yet &mdash; is the real problem, and it is where most of the engineering went: prerequisite graphs, sequencing rules, consistency checks between modules, and evaluation of generated material before a learner ever sees it.</p>
        <div class="project-meta">
          <span class="pill">Next.js</span>
          <span class="pill">Curriculum generation</span>
          <span class="pill">Adaptive sequencing</span>
          <span class="pill">Content evaluation</span>
        </div>
        <a class="textlink" href="https://teachwise-ai.com" rel="noopener">Visit teachwise-ai.com</a>
      </div>
      <div class="frame">
        <div class="frame-rows">
          <div class="frame-row"><i style="background:var(--blue)"></i> Learning goal <span>Set</span></div>
          <div class="frame-row"><i style="background:var(--indigo)"></i> Curriculum built <span>9 modules</span></div>
          <div class="frame-row"><i style="background:var(--violet)"></i> Prerequisites <span>Checked</span></div>
          <div class="frame-row"><i style="background:var(--amber)"></i> Progress <div class="frame-bar"><i></i></div></div>
          <div class="frame-row"><i style="background:var(--green)"></i> Next lesson <span>Ready</span></div>
        </div>
      </div>
    </article>
  </div>
</section>

<hr class="rule">

<section class="band band-deep">
  <div class="shell">
    <article class="project" id="project-controls" style="padding-top:0">
      <div>
        <span class="pill pill-build">In build</span>
        <h3 style="margin-top:1rem">Project controls for the energy sector</h3>
        <p>Capital projects in energy live or die on cost, schedule, change and risk information &mdash; which is usually spread across a dozen spreadsheets, three reporting tools and the memory of one very experienced planner. Our current build brings that into one application: a baseline that holds, progress tracked against it, and variance explained in language a steering committee can act on.</p>
        <p>AI does the reading and the drafting. It parses contractor progress reports, reconciles them against the plan, flags drift early, and writes the first version of the monthly narrative. What it does not do is decide: every figure stays traceable to its source document, and every forecast is reviewed and signed off by a named person before it goes anywhere.</p>
        <h3 style="font-size:1.15rem;margin-top:1.6rem">Where it goes next</h3>
        <p>The core &mdash; baselines, earned value, change control, risk and reporting &mdash; is common to any capital programme. Energy is first because the reporting burden and the consequences of drift are highest there. Construction, utilities, infrastructure and manufacturing follow, and we are speaking with teams in each about pilots.</p>
        <div class="project-meta">
          <span class="pill">Energy</span>
          <span class="pill">Cost and schedule</span>
          <span class="pill">Earned value</span>
          <span class="pill">Change control</span>
          <span class="pill">Document parsing</span>
        </div>
        <a class="textlink" href="/contact">Ask about an early pilot</a>
      </div>
      <div class="frame">
        <div class="frame-rows">
          <div class="frame-row"><i style="background:var(--cyan)"></i> Cost performance <span>CPI 0.97</span></div>
          <div class="frame-row"><i style="background:var(--blue)"></i> Schedule performance <span>SPI 1.02</span></div>
          <div class="frame-row"><i style="background:var(--amber)"></i> Float remaining <span>4 weeks</span></div>
          <div class="frame-row"><i style="background:var(--violet)"></i> Open changes <span>12</span></div>
          <div class="frame-row"><i style="background:var(--magenta)"></i> Risk exposure <div class="frame-bar"><i></i></div></div>
          <div class="frame-row"><i style="background:var(--green)"></i> Monthly narrative <span>Awaiting sign&#8209;off</span></div>
        </div>
      </div>
    </article>
  </div>
</section>

<section class="band">
  <div class="shell">
    <div class="cta">
      <div>
        <h2>Your project could be next</h2>
        <p>We take on a small number of builds at a time so the same senior team stays on each one from scope to launch.</p>
      </div>
      <div class="btn-row"><a class="btn" href="/contact">Start a project</a></div>
    </div>
  </div>
</section>
"""

write("work.html", page(
    "Work — Riff Apps",
    "Riff, a verified social app on iOS and Android. TeachWise AI, a curriculum platform on the web. And a project controls application in build for the energy sector.",
    "/work", WORK, current="/work"))


# ===========================================================================
# GOVERNANCE
# ===========================================================================
GOVERNANCE = """
<section class="doc-head">
  <div class="shell">
    <h1>Governance</h1>
    <p class="lede">How we handle data, how we use AI, and what we commit to on every build. Written for clients doing due diligence on us &mdash; and for anyone using a product we made.</p>
  </div>
</section>
<hr class="rule">

<section class="band">
  <div class="shell stack-lg">
    <div>
      <div class="section-head">
        <h2>Our commitments on AI</h2>
        <p>These apply to everything we build, including our own products. If a client asks us to break one, we say no.</p>
      </div>
      <div class="tile-set">
        <article class="tile tile-wide">
          <h3>Nobody is fooled about who they&rsquo;re talking to</h3>
          <p>AI participants and generated content are labelled in the interface at the point of use, not disclosed once in a policy page. In Riff, for example, AI companions are identified as AI throughout the experience.</p>
        </article>
        <article class="tile tile-wide">
          <h3>A human decides anything that matters</h3>
          <p>Where an output affects someone&rsquo;s money, safety, employment, learning or access to a service, a person reviews it before it takes effect and can overturn it. The route to that person is part of the design.</p>
        </article>
        <article class="tile">
          <h3>Explainable outputs</h3>
          <p>If a model ranks, scores or matches someone, the product shows the basis for it in terms they can understand.</p>
        </article>
        <article class="tile">
          <h3>Measured, not assumed</h3>
          <p>Every AI feature ships with an evaluation set, recorded failure modes and monitoring in production.</p>
        </article>
        <article class="tile">
          <h3>Your data is not training data</h3>
          <p>We do not use client or end&#8209;user content to train third&#8209;party models, and we select providers whose terms match that.</p>
        </article>
      </div>
    </div>

    <hr class="rule-soft">

    <div>
      <div class="section-head">
        <h2>Data protection</h2>
        <p>We act as a processor on client projects and a controller for our own products and enquiries. Both are documented.</p>
      </div>
      <div class="tile-set">
        <article class="tile">
          <h3>Lawful basis first</h3>
          <p>Identified and recorded before a feature is built, not reverse&#8209;engineered before an audit.</p>
        </article>
        <article class="tile">
          <h3>Minimised by design</h3>
          <p>A feature gets the fields it needs and no more, with a retention period set at the same time.</p>
        </article>
        <article class="tile">
          <h3>Impact assessed</h3>
          <p>A DPIA for anything involving special category data, children, large&#8209;scale profiling or automated decisions.</p>
        </article>
        <article class="tile">
          <h3>Rights that work</h3>
          <p>Access, correction, deletion, portability and objection built as functioning product features.</p>
        </article>
        <article class="tile">
          <h3>Transfers documented</h3>
          <p>Where data leaves the UK or EEA, the safeguard relied on is recorded and reviewed.</p>
        </article>
        <article class="tile">
          <h3>Breach ready</h3>
          <p>A tested response plan with the 72&#8209;hour regulator notification window built into it.</p>
        </article>
      </div>
      <p style="margin-top:1.5rem"><a class="textlink" href="/legal/gdpr">Read the full GDPR statement</a></p>
    </div>

    <hr class="rule-soft">

    <div>
      <div class="section-head">
        <h2>Security</h2>
        <p>Proportionate to the data a product holds, and reviewed as that changes.</p>
      </div>
      <div class="steps">
        <div class="step">
          <div>
            <h3>Encryption everywhere</h3>
            <p>TLS in transit and encryption at rest as standard, including user media and voice. Secrets held in a managed store, never in source control.</p>
          </div>
        </div>
        <div class="step">
          <div>
            <h3>Least privilege access</h3>
            <p>Named accounts, multi&#8209;factor authentication, role&#8209;based permissions and access reviews when people join or leave a project.</p>
          </div>
        </div>
        <div class="step">
          <div>
            <h3>Dependencies watched</h3>
            <p>Automated vulnerability scanning on every build, with a defined window for patching by severity.</p>
          </div>
        </div>
        <div class="step">
          <div>
            <h3>Tested independently</h3>
            <p>Third&#8209;party penetration testing before launch on products handling sensitive data, and periodically after.</p>
          </div>
        </div>
      </div>
    </div>

    <hr class="rule-soft">

    <div>
      <div class="section-head">
        <h2>Accessibility</h2>
        <p>WCAG 2.2 AA is the floor for everything we deliver, not an upgrade.</p>
      </div>
      <p class="measure" style="color:var(--on-dark-muted)">Interfaces are built to work with a keyboard alone, with a screen reader, at 200% zoom and with reduced motion enabled. Colour is never the only way meaning is conveyed, contrast is checked against the standard, and forms carry real labels and error messages that say what to fix. We test with assistive technology rather than relying on an automated checker alone.</p>
      <p class="measure" style="color:var(--on-dark-muted)">If you find something on this site or in one of our products that you cannot use, email <a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a> and we will treat it as a defect.</p>
    </div>

    <div class="cta">
      <div>
        <h2>Doing due diligence on us?</h2>
        <p>We&rsquo;ll complete your security questionnaire, sign a DPA and walk your team through how a product handles data.</p>
      </div>
      <div class="btn-row"><a class="btn" href="/contact">Request our documentation</a></div>
    </div>
  </div>
</section>
"""

write("governance.html", page(
    "Governance — Riff Apps",
    "How Riff Apps handles data protection, security, accessibility and AI governance across every project we build.",
    "/governance", GOVERNANCE, current="/governance"))


# ===========================================================================
# CONTACT
# ===========================================================================
CONTACT = """
<section class="doc-head">
  <div class="shell">
    <h1>Start a project</h1>
    <p class="lede">Tell us what you&rsquo;re trying to build and we&rsquo;ll reply within two working days with what we&rsquo;d do first.</p>
  </div>
</section>
<hr class="rule">

<section class="band">
  <div class="shell contact-grid">
    <div>
      <form class="form" id="contact-form" novalidate>
        <div class="form-row">
          <div class="field">
            <label for="name">Your name</label>
            <input type="text" id="name" name="name" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="organisation">Organisation</label>
            <input type="text" id="organisation" name="organisation" autocomplete="organization">
          </div>
        </div>

        <div class="form-row">
          <div class="field">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" autocomplete="email" required>
          </div>
          <div class="field">
            <label for="topic">What&rsquo;s it about?</label>
            <select id="topic" name="topic">
              <option value="New application">A new application</option>
              <option value="Existing product">An existing product</option>
              <option value="AI feature">Adding AI to something we have</option>
              <option value="Governance review">Governance or accessibility review</option>
              <option value="Project controls pilot">Project controls pilot</option>
              <option value="Something else">Something else</option>
            </select>
          </div>
        </div>

        <div class="field">
          <label for="message">The problem, in a paragraph</label>
          <textarea id="message" name="message" required placeholder="What should it do, who is it for, and what&rsquo;s the deadline you&rsquo;re working to?"></textarea>
          <span class="field-hint">Rough is fine. We&rsquo;d rather hear the problem than a specification.</span>
        </div>

        <label class="check">
          <input type="checkbox" id="consent" name="consent" required>
          <span>I&rsquo;m happy for Riff Apps to use these details to reply to my enquiry, as described in the <a class="textlink" href="/legal/privacy-policy">privacy policy</a>.</span>
        </label>

        <div class="btn-row">
          <button class="btn" type="submit">Send enquiry</button>
        </div>

        <p class="form-note" id="form-status" role="status" aria-live="polite"></p>
        <p class="form-note">This form opens your own email app with the message ready to send, so nothing is stored here until you press send.</p>
      </form>
    </div>

    <aside>
      <div class="frame">
        <h2 style="font-family:Outfit,sans-serif;font-size:1.2rem;margin-bottom:1.2rem">Direct</h2>
        <dl class="kv">
          <div>
            <dt>Email</dt>
            <dd><a class="textlink" href="mailto:Contact@Riff-Apps.com">Contact@Riff-Apps.com</a></dd>
          </div>
          <div>
            <dt>Based in</dt>
            <dd>United Kingdom</dd>
          </div>
          <div>
            <dt>Typical reply</dt>
            <dd>Within two working days</dd>
          </div>
        </dl>
      </div>

      <div style="margin-top:2rem">
        <h2 style="font-family:Outfit,sans-serif;font-size:1.2rem;margin-bottom:.8rem">What happens next</h2>
        <div class="steps">
          <div class="step">
            <div>
              <h3 style="font-size:1.02rem">We read it properly</h3>
              <p style="font-size:.93rem">A person replies, not an autoresponder.</p>
            </div>
          </div>
          <div class="step">
            <div>
              <h3 style="font-size:1.02rem">A call, if it looks like a fit</h3>
              <p style="font-size:.93rem">Half an hour to understand the problem and the constraints.</p>
            </div>
          </div>
          <div class="step">
            <div>
              <h3 style="font-size:1.02rem">A written proposal</h3>
              <p style="font-size:.93rem">Scope, approach, timeline and price &mdash; or an honest referral elsewhere.</p>
            </div>
          </div>
        </div>
      </div>
    </aside>
  </div>
</section>
"""

write("contact.html", page(
    "Contact — Riff Apps",
    "Tell Riff Apps what you are trying to build. Email Contact@Riff-Apps.com or send an enquiry and we will reply within two working days.",
    "/contact", CONTACT, current="/contact"))


# ===========================================================================
# 404
# ===========================================================================
NOTFOUND = """
<section class="band" style="padding-top:clamp(4rem,10vw,8rem)">
  <div class="shell">
    <h1 style="font-size:var(--step-4)">That page isn&rsquo;t here<br><span class="light">but these are.</span></h1>
    <p class="lede" style="margin:1.5rem 0 2rem">The link may be out of date, or the address slightly off.</p>
    <div class="btn-row">
      <a class="btn" href="/">Back to home</a>
      <a class="btn btn-ghost" href="/work">See our work</a>
      <a class="btn btn-ghost" href="/contact">Contact us</a>
    </div>
  </div>
</section>
"""

write("404.html", page(
    "Page not found — Riff Apps",
    "The page you were looking for could not be found.",
    "/404", NOTFOUND))
