import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents" / "skills" / "meeting-slot-finder" / "scripts" / "find_meeting_slots.py"
NORMAL = ROOT / "examples" / "normal_request.json"
EDGE = ROOT / "examples" / "edge_request.json"
LIMITED = ROOT / "examples" / "limited_request.json"


class MeetingSlotFinderTest(unittest.TestCase):
    def run_request(self, path: Path) -> dict:
        completed = subprocess.run(
            ["python3", str(SCRIPT), str(path)],
            check=True,
            capture_output=True,
            text=True,
        )
        return json.loads(completed.stdout)

    def test_normal_request_returns_ranked_slots(self):
        payload = self.run_request(NORMAL)
        self.assertEqual(payload["duration_minutes"], 60)
        self.assertGreaterEqual(len(payload["recommended_slots"]), 1)
        self.assertEqual(payload["recommended_slots"][0]["rank"], 1)
        self.assertEqual(len(payload["recommended_slots"][0]["participants"]), 3)

    def test_edge_request_handles_non_aligned_start_time(self):
        payload = self.run_request(EDGE)
        self.assertEqual(payload["duration_minutes"], 30)
        self.assertGreaterEqual(len(payload["recommended_slots"]), 1)
        self.assertTrue(payload["recommended_slots"][0]["start_utc"].endswith(":30:00+00:00") or payload["recommended_slots"][0]["start_utc"].endswith(":00:00+00:00"))

    def test_limited_request_returns_no_slots(self):
        payload = self.run_request(LIMITED)
        self.assertEqual(payload["duration_minutes"], 60)
        self.assertEqual(payload["recommended_slots"], [])


if __name__ == "__main__":
    unittest.main()
