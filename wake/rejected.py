# =============================================================================
# REJECTED — the failure-observation layer. Rejected proposals are not accepted state, but they are valuable evidence about what disposable cognition attempted and what deterministic governance prevented. Rendering them must preserve that distinction.
#
# MAINTENANCE PRINCIPLE
# ---------------------
# The architecture is intentionally explicit.  A future human or AI maintainer
# should be able to follow authority from input, through validation, to durable
# record without relying on folklore.  Comments explain why boundaries exist,
# what failure means, and which tempting shortcuts would weaken accountability.
# =============================================================================

"""Readable presentation of recorded rejection decisions; never rejudge old proposals."""
import html
import json
from urllib.parse import quote


# ---------------------------------------------------------------------------
# STEP: explanation
#
# Keep this function explicit because it marks a testable boundary in the
# chain from operator/provider input to durable/public output.  Do not fold it
# into a neighboring layer if doing so would hide validation, provenance,
# failure handling, or the distinction between accepted state and a derived view.


# ---------------------------------------------------------------------------


def explanation(reason):
    if 'traceable through its referenced notebooks' in reason:
        return ('The draft cited sources that were not attached to the notebooks it named. '
                'A source can exist in WAKE’s record without supporting that particular notebook. '
                'The publication rule requires that connection to be recorded first.')
    if 'contested synthesis or interpretation as established fact' in reason:
        return ('The wording check found a phrase it treats as an overclaim about a contested topic. '
                'This is a mechanical phrase check, not a verdict that the whole draft is false. '
                'It can also catch quotations, negations, or attempted corrections that do not meet '
                'the accepted retraction format. Read the draft below to judge the context.')
    if 'Limited or abstract-only sources' in reason:
        return ('The draft used certainty language while its cited material was recorded as limited '
                'or incomplete. The rule requires claims to reflect the limits of the available sources.')
    if 'Evidence reference does not exist' in reason:
        return 'At least one cited source ID was missing from the durable record at the time of this decision.'
    if 'Quantum-Carnegie connections' in reason:
        return ('The wording check detected a claim connecting quantum physics to mind or behavior '
                'as a scientific explanation. WAKE permits these connections only as clearly labeled metaphor.')
    if 'base_version' in reason:
        return 'The response did not identify the research version it was asked to continue, so applying it could conflict with the saved record.'
    return ('The response did not satisfy the recorded acceptance rule below. '
            'This page preserves that decision; it does not rerun today’s rules against an older draft.')


# ---------------------------------------------------------------------------
# STEP: _text
#
# Keep this function explicit because it marks a testable boundary in the
# chain from operator/provider input to durable/public output.  Do not fold it
# into a neighboring layer if doing so would hide validation, provenance,
# failure handling, or the distinction between accepted state and a derived view.


# ---------------------------------------------------------------------------


def _text(value):
    # Normalize the public wordmark in readable presentation only; raw state is unchanged.
    escaped = html.escape(str(value).replace("WAKE✳︎", "WAKE✳").replace("WAKE✳", "WAKE✳︎"))
    return escaped.replace("WAKE✳︎", '<strong class="wake-mark">WAKE✳︎</strong>')


# ---------------------------------------------------------------------------
# STEP: _paragraphs
#
# Keep this function explicit because it marks a testable boundary in the
# chain from operator/provider input to durable/public output.  Do not fold it
# into a neighboring layer if doing so would hide validation, provenance,
# failure handling, or the distinction between accepted state and a derived view.


# ---------------------------------------------------------------------------


def _paragraphs(value):
    return ''.join('<p>' + _text(p).replace('\n', '<br>') + '</p>' for p in str(value).split('\n\n') if p.strip())


# ---------------------------------------------------------------------------
# STEP: rejected_html
#
# Keep this function explicit because it marks a testable boundary in the
# chain from operator/provider input to durable/public output.  Do not fold it
# into a neighboring layer if doing so would hide validation, provenance,
# failure handling, or the distinction between accepted state and a derived view.


# ---------------------------------------------------------------------------


def rejected_html(state, events):
    cards = []
    for event in reversed(events):
        payload = event['payload']
        withheld = event['kind'] == 'accepted' and isinstance(payload.get('editorial'), dict)
        if event['kind'] != 'rejected' and not withheld:
            continue
        invocation = state['invocations'].get(payload['id'], {})
        reason = str(payload['editorial'].get('reason', '')) if withheld else str(payload.get('reason', ''))
        raw = payload.get('raw_response')
        proposal = None
        if isinstance(raw, str):
            try:
                proposal = json.loads(raw)
            except (ValueError, TypeError):
                pass
        if withheld:
            actions = [payload['editorial'].get('action')]
            title = (actions[0] or {}).get('title', 'Withheld blog draft')
        else:
            actions = proposal.get('actions', []) if isinstance(proposal, dict) else []
            title = proposal.get('title', 'Rejected proposal') if isinstance(proposal, dict) else 'Unreadable proposal'
        if not isinstance(actions, list):
            actions = []
        label = 'Blog withheld · research accepted' if withheld else 'Rejected · not accepted research'
        consequence = ('The other research actions were accepted. This blog draft was withheld and was not published as a blog post.'
                       if withheld else 'No research changes or journal entry from this proposal were accepted. Its claims are unapproved model output.')
        draft = ''
        if not withheld and isinstance(proposal, dict) and proposal.get('summary'):
            draft += '<h3>Proposed summary</h3>' + _paragraphs(proposal['summary'])
        for action in actions:
            if not isinstance(action, dict):
                continue
            kind = action.get('type', 'unknown')
            draft += '<section><h3>' + _text(action.get('title') or action.get('id') or kind) + '</h3>'
            draft += '<p class="meta">Proposed ' + _text(kind) + ' · not accepted</p>'
            for field in ('lede', 'body', 'statement', 'task', 'summary', 'findings', 'limitations', 'next_questions', 'lens', 'reason'):
                if action.get(field):
                    draft += '<h4>' + _text({'lens': 'Bob’s lens', 'reason': 'Model’s stated reason'}.get(field, field.replace('_', ' ').capitalize())) + '</h4>' + _paragraphs(action[field])
            for field in ('notebooks', 'evidence'):
                ids = action.get(field)
                if isinstance(ids, list):
                    draft += '<p><strong>Proposed ' + field + ':</strong> ' + ', '.join('<code>' + _text(i) + '</code>' for i in ids) + '</p>'
            draft += '</section>'
        if not draft:
            draft = '<p>No readable draft could be extracted. The exact saved response is available below.</p>'
        count = invocation.get('provider_requests_sent', payload.get('provider_requests_sent'))
        calls = str(count) + ' provider request' + ('' if count == 1 else 's') if count is not None else 'Provider request count not recorded'
        attempts = invocation.get('provider_attempts', [])
        diagnostics = ''
        if attempts:
            diagnostics = '<h3>Model attempts</h3><ul>' + ''.join(
                '<li>' + _text(a.get('model', 'Unknown model')) + ' · ' + _text(a.get('http_status') or 'No HTTP status')
                + ' · ' + _text(a.get('result', 'unknown').replace('_', ' '))
                + (' · ' + str(round(a['elapsed_ms'] / 1000, 3)) + 's' if isinstance(a.get('elapsed_ms'), (float, int)) else '')
                + '</li>' for a in attempts) + '</ul>'
        ident = payload['id']
        cards.append(
            '<article id="' + _text(ident) + '"><p class="eyebrow">' + label + '</p><h2>' + _text(title) + '</h2>'
            + '<p class="meta">' + _text(event['time']) + ' · ' + _text(calls) + '</p>'
            + '<p><strong>' + consequence + '</strong></p><h3>Why it stopped</h3><p>' + _text(explanation(reason)) + '</p>'
            + '<p><strong>Exact recorded reason:</strong> ' + _text(reason or 'No reason recorded') + '</p>'
            + '<p class="meta">This is the recorded first failing check, not an exhaustive review of every claim.</p>'
            + '<details><summary>Read the unaccepted draft</summary><div class="inside">' + draft + '</div></details>'
            + diagnostics + '<details><summary>Exact saved response</summary><pre>' + _text(raw if raw is not None else 'No raw response was saved.') + '</pre></details>'
            + '<p><a href="index.html#history/' + quote(str(ident), safe='') + '">Full invocation and decision →</a></p></article><hr>')
    intro = ('<p>These drafts show what WAKE tried to produce and why it stopped. '
             'They are displayed for inspection, not endorsed as findings or published blog posts. '
             'More rejections do not by themselves prove better judgment; some checks can be too broad.</p>')
    return '<div style="max-width:780px;overflow-wrap:anywhere">' + intro + (''.join(cards) or '<p>No rejected proposals or withheld blog drafts have been recorded.</p>') + '</div>'
