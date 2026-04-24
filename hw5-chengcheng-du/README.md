# Meeting Slot Finder

Video: [meeting-slot-finder-demo.mp4](demo/meeting-slot-finder-demo.mp4)

## What the skill does

Meeting Slot Finder is a reusable skill for scheduling meetings across time zones. It takes structured JSON input, converts each participant's local work hours into UTC, searches for valid overlaps, and returns ranked meeting options.

## Why I chose it

I chose this skill because timezone conversion, overlap checking, and date calculations are deterministic tasks that are easy to get wrong with prompt-only reasoning. This is a good fit for a script-backed skill because the model can explain results, while Python handles the exact time math.

## Repository structure

```text
hw5-chengcheng-du/
├── .agents/
│   └── skills/
│       └── meeting-slot-finder/
│           ├── SKILL.md
│           ├── references/
│           │   └── input-schema.md
│           └── scripts/
│               ├── find_meeting_slots.py
│               └── sample_request.json
├── demo/
│   └── meeting-slot-finder-demo.mp4
├── examples/
│   ├── agent_prompts.md
│   ├── normal_request.json
│   ├── normal_output.json
│   ├── edge_request.json
│   ├── edge_output.json
│   ├── limited_request.json
│   └── limited_output.json
├── tests/
│   └── test_meeting_slot_finder.py
└── README.md
```

## How to use it

Run the main script with a JSON request file:

```bash
python3 .agents/skills/meeting-slot-finder/scripts/find_meeting_slots.py \
  .agents/skills/meeting-slot-finder/scripts/sample_request.json
```

To save a result to a file:

```bash
python3 .agents/skills/meeting-slot-finder/scripts/find_meeting_slots.py \
  examples/normal_request.json \
  --output examples/normal_output.json
```

## What the script does

The Python script:

- parses participant names, time zones, work hours, and scheduling constraints from JSON
- converts local availability windows into UTC
- searches the requested date range in 30-minute increments
- checks whether each candidate slot fits every participant's work window
- scores valid overlaps and returns the top ranked options

## Three prompt tests

The repository includes three agent-style test scenarios:

- Normal case: [examples/normal_request.json](examples/normal_request.json) and [examples/normal_output.json](examples/normal_output.json)
- Edge case: [examples/edge_request.json](examples/edge_request.json) and [examples/edge_output.json](examples/edge_output.json)
- Limited case: [examples/limited_request.json](examples/limited_request.json) and [examples/limited_output.json](examples/limited_output.json)

Prompt wording is documented in [examples/agent_prompts.md](examples/agent_prompts.md).

## What worked well

- The skill is easy for an agent to discover because the name and description are specific.
- The script produces repeatable results from structured input.
- The output is easy to explain because each recommended slot includes local times for every participant.
- The examples show both successful scheduling and a no-overlap case.

## Limitations

- The current script assumes each participant has one continuous work window per day.
- It searches in 30-minute steps rather than arbitrary minute precision.
- It does not yet model holidays, personal calendar conflicts, or recurring availability rules.
- The limited case returns no options, but a future version could generate more explicit fallback suggestions.
