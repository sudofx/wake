"""Stable research fixtures for tests.

Production topics are operator-controlled experimental inputs. Tests that exercise
research governance must therefore declare their own topic space rather than
silently inheriting research-topics.toml from the current live experiment.
"""

from wake.engine import DEFAULTS


TEST_RESEARCH_TOPICS = [
    {
        "id": "entropy",
        "label": "Entropy",
        "query": "entropy",
        "seed_question": "What distinguishes major entropy definitions?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "comedy",
        "label": "Comedy",
        "query": "comedy",
        "seed_question": "What distinguishes major theories of comedy?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "music",
        "label": "Music",
        "query": "music",
        "seed_question": "How do different accounts explain musical perception?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "neurodivergence",
        "label": "Neurodivergence",
        "query": "neurodivergence",
        "seed_question": "How do major frameworks describe neurodivergence?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "psychology",
        "label": "Psychology",
        "query": "psychology",
        "seed_question": "What distinguishes major psychological explanations?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "wake_analysis",
        "label": "WAKE✳︎",
        "query": "WAKE✳︎ sudofx/wake",
        "seed_question": "How does the runtime preserve accountable continuity?",
        "enabled": True,
        "source_kind": "repository",
        "repository": "sudofx/wake",
    },
]


def charter_settings(mission="Test research behavior.", **overrides):
    """Return isolated charter settings that never read the live topic file."""
    return {
        **DEFAULTS,
        "mission": mission,
        "research_topics": [dict(topic) for topic in TEST_RESEARCH_TOPICS],
        **overrides,
    }
