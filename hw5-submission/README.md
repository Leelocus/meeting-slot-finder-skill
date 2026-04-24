# Meeting Slot Finder

A small project for finding meeting times across time zones.

## Files

```text
hw5-submission/
├── .agents/
│   └── skills/
│       └── meeting-slot-finder/
│           ├── SKILL.md
│           ├── references/
│           │   └── input-schema.md
│           └── scripts/
│               ├── find_meeting_slots.py
│               └── sample_request.json
├── README.md
├── demo/
│   └── meeting-slot-finder-demo.mp4
└── tests/
    └── test_meeting_slot_finder.py
```

## What it does

The script reads a JSON request with participant names, time zones, work hours, a meeting length, and a search window. It returns ranked meeting slots that fit everyone.

## Run

```bash
python3 .agents/skills/meeting-slot-finder/scripts/find_meeting_slots.py \
  .agents/skills/meeting-slot-finder/scripts/sample_request.json
```

## Video

- [meeting-slot-finder-demo.mp4](demo/meeting-slot-finder-demo.mp4)
