# Activity: AI-Assisted Codebase Handover

A ~10-minute “vibe coding” stand activity. Participants receive an under-documented repository and use an AI coding agent to prepare it for handover.

**Stand page (GitHub Pages):** open `docs/index.html` locally, or publish with `docs/PUBLISH.md`. Print `docs/poster.html` if you want a handout with QR.

**Important:** Participants generate `README.md` and `HANDOVER.md` from **this** repository (the under-documented demo). Optional finished examples live in `docs/examples/` for comparison or facilitator use — ask people to try generating first.

---

## 1. The scenario

**You are receiving this repository from another researcher. They are no longer available to explain it.**

Take 1–2 minutes to glance at the repo (especially `README.md` and a couple of source files). Then ask yourself whether you can determine:

- what the tool does;
- what input it accepts;
- how to run it;
- what output to expect;
- how to test it;
- what remains unfinished.

Most people will find the current README insufficient. That is intentional.

---

## 2. Generate the README

Ask your AI coding agent something like this:

```text
You are preparing this repository for handover to another developer or AI coding agent.
Inspect the repository carefully before making any changes.
Create or update README.md so that someone unfamiliar with the project can understand and run it without asking the original developer for help.
Include:
- what the project does
- the main workflow
- expected inputs and outputs
- environment setup and dependencies
- exact commands to run the project
- a minimal working example
- important files and repository structure
- how to test or verify that it works
- known limitations or unsupported cases
Important:
- Base everything on evidence from the repository.
- Do not invent commands, behaviour, or design decisions.
- If something cannot be determined, mark it as "TODO: clarify".
- Prefer exact filenames, paths and commands.
- Keep the README concise and practical.
```

---

## 3. Review the AI-generated README

**inspect → generate → verify**

Check the new README together:

- Did it inspect the actual code?
- Did it use real commands?
- Did it invent anything?
- Did it identify the limitations?
- Did it mark unknowns rather than guessing?

If something looks invented, ask the agent to revise based only on evidence in the repository.

---

## 4. Create HANDOVER.md

Do **not** treat the README as enough for continued development. Ask:

```text
You are handing this repository to another developer or AI coding agent.
Inspect the repository and current implementation.
Create HANDOVER.md to help the next person continue development from the current state.
Include:
1. Current status
   - what currently works
   - what appears incomplete
2. Known issues
   - bugs
   - uncertainties
   - technical debt
   - unresolved questions
3. Next tasks
   - concrete tasks the next developer could continue with
4. Important decisions and constraints
   - implementation choices that should not be accidentally reversed
   - behaviours or interfaces that should be preserved
5. Important files
   - files most relevant to continued development
6. Verification
   - commands/tests to run before and after making changes
Rules:
- Do not repeat general information already covered by README.md.
- Do not invent project history.
- Clearly mark uncertain information as "Needs confirmation".
- Use exact file paths, commands and test names where possible.
- Keep it concise and actionable.
```

---

## 5. Test the handover

Swap roles (or open a fresh AI chat) and verify the handover pack works.

```text
You have just inherited this repository.
Do not make any changes yet.
Read README.md and HANDOVER.md, then tell me:
1. What does this project do?
2. How do I run it?
3. How do I verify that it works?
4. What is the current development status?
5. What should I work on next?
6. What important constraints should I avoid breaking?
7. What information is still missing or ambiguous?
```

A good handover means a new person (or agent) can answer these without digging through every file first.

---

## 6. Final takeaway

**README.md = what the project is.**

**HANDOVER.md = where the work is now.**

Before ending the session, ask the agent (or yourself) to refresh the handover note:

```text
Before finishing this session, update HANDOVER.md.
Summarise:
- what you changed,
- what now works,
- what remains unresolved,
- important decisions made,
- files modified,
- what should happen next,
- and how the next developer or AI agent can verify the current state.
Do not repeat general project information already in README.md.
Keep it concise and actionable.
```
