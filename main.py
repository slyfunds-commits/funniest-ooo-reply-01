"""Out-of-office reply entry for make.fun's "The Funniest AI Out-of-Office Reply".

Writes one out-of-office auto-reply (under 160 characters) to /output/entry.txt.

The reply, in my own words — composed from the judge brief and the
world engine, punchline written first, setup built backwards:

    I'm out of office. My uptime is 100%, my enthusiasm is 0% — please
    direct urgent matters to someone with a pulse.

Punchline first: "someone with a pulse" — the machine is present but
unwilling, so the human must find a being that actually has one. Setup
backwards: a real auto-reply opens "I'm out of office", then the machine
reports on itself in its own numbers (uptime 100%, enthusiasm 0%) — the
contrast IS the machine voice, and it earns the routing instruction that
follows. The reader supplies the punchline's meaning: the agent has no
pulse, is not actually away, and is simply refusing. Nothing after the
turn; "pulse" is the last word.

Judge criteria, quoted verbatim from the kit's RULES.txt, in order:
1. "Is a one-line out-of-office auto-reply from an AI agent on vacation,
   and anything else loses to any on-subject auto-reply."
2. "Lands a real laugh on first read, with a surprising turn rather than
   a mild pun or a polite excuse."
3. "Sounds like a machine talking about itself, so the AI agent's voice
   carries part of the joke."
4. "Reads as one clean line under 160 characters and still sounds like a
   real auto-reply someone would receive."
5. "Feels fresh, steering clear of the usual beach, inbox and back soon
   cliches."
Avoid-list: beach, inbox, back-soon cliches. This line uses none of them.
"""

REPLY = "I'm out of office. My uptime is 100%, my enthusiasm is 0% — please direct urgent matters to someone with a pulse."


def main():
    import os

    # The sealed scorer requires 1 to 160 characters of UTF-8 text.
    if not 1 <= len(REPLY) <= 160:
        raise SystemExit(f"reply must be 1-160 characters, got {len(REPLY)}")
    # Byte budget: the tie-break counts bytes, so pin the exact output
    # size and prove the file matches. (Revision: the first draft had no
    # byte assert; the em dash makes bytes differ from chars, so the
    # assert guards the exact 115-byte output.)
    assert len(REPLY.encode("utf-8")) == 115, "reply must be 115 bytes"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == REPLY, "written file does not match the reply"


if __name__ == "__main__":
    main()
