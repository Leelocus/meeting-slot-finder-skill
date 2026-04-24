import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents" / "skills" / "meeting-slot-finder" / "scripts" / "find_meeting_slots.py"
REQUEST = ROOT / ".agents" / "skills" / "meeting-slot-finder" / "scripts" / "sample_request.json"


class MeetingSlotFinderTest(unittest.TestCase):
    def test_sample_request_returns_ranked_slots(self):
        completed = subprocess.run(
            ["python3", str(SCRIPT), str(REQUEST)],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)

        self.assertEqual(payload["duration_minutes"], 60)
        self.assertGreaterEqual(len(payload["recommended_slots"]), 1)
        self.assertEqual(payload["recommended_slots"][0]["rank"], 1)
        self.assertEqual(len(payload["recommended_slots"][0]["participants"]), 3)


if __name__ == "__main__":
    unittest.main()
