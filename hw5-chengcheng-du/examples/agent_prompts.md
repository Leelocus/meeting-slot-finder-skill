# Agent Prompt Examples

## Normal Case
Find the best one hour kickoff time next week for teammates in Los Angeles, London, and Dubai. Keep the meeting inside each person's work hours and give me the top three options.

## Edge Case
Starting after 11:17 PM China time on Monday, find the earliest 30 minute handoff meeting for the same three teammates and return two ranked options.

## Limited Case
Try to schedule a 60 minute meeting for teammates in Los Angeles, London, and Dubai when each person is only available from 8:00 to 9:00 AM local time. If there is no shared slot, say so clearly instead of inventing one.
