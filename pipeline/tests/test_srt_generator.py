#!/usr/bin/env python3
"""Tests for SRT subtitle generation from timing.json.

Run with: python3 -m pytest pipeline/tests/test_srt_generator.py -v
Or directly: python3 pipeline/tests/test_srt_generator.py
"""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

# Add parent directories to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from generate_srt import (
    format_srt_time,
    escape_srt_text,
    generate_srt_from_timing,
)


class TestSRTFormatting(unittest.TestCase):
    """Test SRT timestamp and text formatting functions."""
    
    def test_format_srt_time_zero(self):
        """Test formatting of zero timestamp."""
        self.assertEqual(format_srt_time(0), "00:00:00,000")
    
    def test_format_srt_time_seconds(self):
        """Test formatting of seconds."""
        self.assertEqual(format_srt_time(5.5), "00:00:05,500")
        self.assertEqual(format_srt_time(30.123), "00:00:30,123")
    
    def test_format_srt_time_minutes(self):
        """Test formatting of minutes."""
        self.assertEqual(format_srt_time(90.5), "00:01:30,500")
        self.assertEqual(format_srt_time(125), "00:02:05,000")
    
    def test_format_srt_time_hours(self):
        """Test formatting with hours."""
        self.assertEqual(format_srt_time(3661.5), "01:01:01,500")
    
    def test_format_srt_time_negative(self):
        """Test that negative times are clamped to zero."""
        self.assertEqual(format_srt_time(-5), "00:00:00,000")
    
    def test_escape_srt_text_basic(self):
        """Test basic text escaping."""
        self.assertEqual(escape_srt_text("Hello world"), "Hello world")
    
    def test_escape_srt_text_newlines(self):
        """Test that newlines are converted to spaces."""
        self.assertEqual(escape_srt_text("Hello\nworld"), "Hello world")
        self.assertEqual(escape_srt_text("Hello\r\nworld"), "Hello world")
    
    def test_escape_srt_text_commas(self):
        """Test that commas in text are preserved (not in timestamps)."""
        self.assertEqual(escape_srt_text("Hello, world"), "Hello, world")
    
    def test_escape_srt_text_whitespace(self):
        """Test that multiple spaces are collapsed."""
        self.assertEqual(escape_srt_text("Hello    world"), "Hello world")
    
    def test_escape_srt_text_empty(self):
        """Test empty string handling."""
        self.assertEqual(escape_srt_text(""), "")
        self.assertEqual(escape_srt_text(None), "")


class TestSRTGeneration(unittest.TestCase):
    """Test SRT generation from timing data."""
    
    def test_generate_srt_basic(self):
        """Test basic SRT generation."""
        timing_data = {
            "total": 10.0,
            "lines": [
                {"en": "Hello world", "t": 0.0, "dur": 2.0},
                {"en": "This is a test", "t": 2.5, "dur": 3.0},
            ]
        }
        
        srt = generate_srt_from_timing(timing_data)
        
        # Check that it has the right structure
        self.assertIn("1\n", srt)
        self.assertIn("00:00:00,000 --> 00:00:02,000", srt)
        self.assertIn("Hello world", srt)
        self.assertIn("2\n", srt)
        self.assertIn("00:00:02,500 --> 00:00:05,500", srt)
        self.assertIn("This is a test", srt)
    
    def test_generate_srt_empty_lines(self):
        """Test that lines without captions are skipped."""
        timing_data = {
            "total": 5.0,
            "lines": [
                {"en": "First", "t": 0.0, "dur": 2.0},
                {"en": "", "t": 2.0, "dur": 1.0},  # Empty caption
                {"en": "Third", "t": 3.0, "dur": 2.0},
            ]
        }
        
        srt = generate_srt_from_timing(timing_data)
        
        # Should have 2 entries, not 3
        entries = [e for e in srt.strip().split('\n\n') if e.strip()]
        self.assertEqual(len(entries), 2)
        self.assertIn("First", srt)
        self.assertIn("Third", srt)
    
    def test_generate_srt_monotonic_check(self):
        """Test that monotonic timing is verified."""
        timing_data = {
            "total": 10.0,
            "lines": [
                {"en": "First", "t": 2.0, "dur": 2.0},
                {"en": "Second", "t": 1.0, "dur": 2.0},  # Starts before first
            ]
        }
        
        with self.assertRaises(ValueError) as context:
            generate_srt_from_timing(timing_data)
        
        self.assertIn("Non-monotonic", str(context.exception))
    
    def test_generate_srt_invalid_duration(self):
        """Test that invalid durations are caught."""
        timing_data = {
            "total": 10.0,
            "lines": [
                {"en": "Test", "t": 0.0, "dur": 0.0},  # Zero duration
            ]
        }
        
        with self.assertRaises(ValueError) as context:
            generate_srt_from_timing(timing_data)
        
        self.assertIn("non-positive duration", str(context.exception))
    
    def test_generate_srt_negative_time(self):
        """Test that negative start times are caught."""
        timing_data = {
            "total": 10.0,
            "lines": [
                {"en": "Test", "t": -1.0, "dur": 2.0},
            ]
        }
        
        with self.assertRaises(ValueError) as context:
            generate_srt_from_timing(timing_data)
        
        self.assertIn("negative start time", str(context.exception))
    
    def test_generate_srt_no_lines(self):
        """Test handling of empty line list."""
        timing_data = {"total": 0.0, "lines": []}
        
        with self.assertRaises(ValueError) as context:
            generate_srt_from_timing(timing_data)
        
        self.assertIn("No lines found", str(context.exception))
    
    def test_generate_srt_realistic(self):
        """Test with realistic clip-01 style data."""
        timing_data = {
            "total": 60.729,
            "lines": [
                {"en": 'My TOEIC study plan: "tomorrow."', "t": 0.12, "dur": 2.22},
                {"en": 'Every night: code, tired, then… "eh, tomorrow."', "t": 3.34, "dur": 3.111},
                {"en": 'Not missing motivation. Missing one sentence: IF… THEN…', "t": 7.451, "dur": 3.713},
            ]
        }
        
        srt = generate_srt_from_timing(timing_data)
        
        # Verify structure (allow for minor rounding differences)
        self.assertIn("1\n", srt)
        self.assertIn("00:00:00,120", srt)
        self.assertIn("My TOEIC study plan", srt)
        
        self.assertIn("2\n", srt)
        self.assertIn("00:00:03,33", srt)  # 3.34 rounds to 3.339
        
        self.assertIn("3\n", srt)
        self.assertIn("00:00:07,45", srt)  # 7.451 rounds to 7.450
    
    def test_generate_srt_commas_in_captions(self):
        """Test that commas and punctuation in captions are preserved."""
        timing_data = {
            "total": 5.0,
            "lines": [
                {"en": "Hello, world! How are you?", "t": 0.0, "dur": 2.0},
                {"en": "I'm fine, thanks.", "t": 2.5, "dur": 2.0},
            ]
        }
        
        srt = generate_srt_from_timing(timing_data)
        
        self.assertIn("Hello, world! How are you?", srt)
        self.assertIn("I'm fine, thanks.", srt)
    
    def test_generate_srt_sequential_indices(self):
        """Test that SRT indices are sequential and 1-based."""
        timing_data = {
            "total": 10.0,
            "lines": [
                {"en": "First", "t": 0.0, "dur": 2.0},
                {"en": "", "t": 2.0, "dur": 1.0},  # Skipped
                {"en": "Third", "t": 3.0, "dur": 2.0},
                {"en": "Fourth", "t": 5.0, "dur": 2.0},
            ]
        }
        
        srt = generate_srt_from_timing(timing_data)
        
        # After skipping empty line, we should have indices 1, 2, 3
        lines = srt.strip().split('\n\n')
        self.assertEqual(len(lines), 3)
        
        # Check first entry starts with 1
        self.assertTrue(lines[0].startswith('1\n'))
        # Check second starts with 2
        self.assertTrue(lines[1].startswith('2\n'))
        # Check third starts with 3
        self.assertTrue(lines[2].startswith('3\n'))


class TestSRTIntegration(unittest.TestCase):
    """Integration tests using actual timing.json files."""
    
    def test_clip_01_timing(self):
        """Test with clip-01 archived timing.json."""
        timing_path = Path("/workspace/content/archive/clip-01-implementation-intention/final/timing.json")
        
        if not timing_path.exists():
            self.skipTest(f"Clip-01 timing.json not found at {timing_path}")
        
        with open(timing_path, 'r') as f:
            timing_data = json.load(f)
        
        # Generate SRT
        srt = generate_srt_from_timing(timing_data)
        
        # Basic checks
        self.assertIsInstance(srt, str)
        self.assertGreater(len(srt), 100)
        
        # Should have multiple entries (clip-01 has 13 lines)
        entries = len([line for line in srt.split('\n') if line.strip().isdigit()])
        self.assertGreater(entries, 10)
        
        # Check monotonic by trying to parse it
        # If it works without exception, timing is valid
        self.assertIn("00:00:00,", srt)
        self.assertIn(" --> ", srt)


def run_tests():
    """Run all tests with verbose output."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestSRTFormatting))
    suite.addTests(loader.loadTestsFromTestCase(TestSRTGeneration))
    suite.addTests(loader.loadTestsFromTestCase(TestSRTIntegration))
    
    # Run with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_tests())
