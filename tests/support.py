"""Stable research fixtures for tests.

Production topics are operator-controlled experimental inputs. Tests declare
their topic space here so they never read the production file at runtime. The
operator-selected topics mirror the current charter; one extra repository topic
is reserved for tests of the configured repository-source capability.
"""

from wake.engine import DEFAULTS


TEST_RESEARCH_TOPICS = [
    {
        "id": "observer",
        "label": "What Is an Observer?",
        "query": "observer measurement information physics cognition",
        "seed_question": "Does looking at something change what happens, or only what we know about it?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "error_detection",
        "label": "How Do We Know We're Wrong?",
        "query": "error detection falsification calibration uncertainty scientific method",
        "seed_question": "How can a person, an AI, or WAKE✳︎ notice that an idea is probably wrong?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "identity",
        "label": "What Makes You You?",
        "query": "identity continuity memory self philosophy cognitive science",
        "seed_question": "If your memories, body, and ideas change, what keeps you the same person?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "music_experience",
        "label": "Why Does Music Feel Like Something?",
        "query": "music cognition prediction emotion rhythm memory neuroscience",
        "seed_question": "Why can organized sound change attention, memory, emotion, and even movement?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "humor",
        "label": "Why Are Things Funny?",
        "query": "humor cognition incongruity prediction surprise timing social violation",
        "seed_question": "Is laughter partly what happens when the brain predicts one thing and gets another?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "information_survival",
        "label": "How Does Information Survive?",
        "query": "information persistence memory genetics software communication entropy",
        "seed_question": "What makes an idea, computer program, gene, memory, or message last instead of disappearing?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "emergence",
        "label": "When Does Simple Become Smart?",
        "query": "emergence complex systems collective intelligence simple rules computation",
        "seed_question": "How can lots of simple pieces working together create behavior no single piece understands?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "observer_disagreement",
        "label": "Can Two Honest Observers Disagree?",
        "query": "observer disagreement measurement uncertainty perspective epistemology",
        "seed_question": "How can two observers study the same thing carefully and still reach different conclusions?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "human_values",
        "label": "What Actually Matters to Us?",
        "query": "meaning values purpose beauty curiosity belonging psychology philosophy",
        "seed_question": "Can science help explain why humans care about love, purpose, beauty, fairness, curiosity, or belonging without reducing them to meaningless numbers?",
        "enabled": True,
        "source_kind": "web",
    },
    {
        "id": "curiosity",
        "label": "Can Curiosity Be Built?",
        "query": "curiosity information gain active learning uncertainty exploration AI",
        "seed_question": "Can a system learn to ask better questions instead of only getting better at answering them?",
        "enabled": True,
        "source_kind": "web",
    },
    # A focused capability fixture for tests of configured repository topics.
    {
        "id": "self_study",
        "label": "Self study",
        "query": "runtime architecture",
        "seed_question": "How does this repository implement its runtime architecture?",
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
