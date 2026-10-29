import unittest
# This imports your exact, unchanged code functions
from validator import parser_b_atproto_custom, transform_mechanism_1_percent

class HackathonExtendedTestSuite(unittest.TestCase):

    def test_standard_valid_uri(self):
        """Test a clean, perfectly formed AT URI."""
        uri = "at://did:plc:z72i7hdynmk6r22z27h6tvur/app.bsky.feed.post/3kzk"
        result = parser_b_atproto_custom(uri)
        self.assertTrue(result["success"])
        self.assertEqual(result["authority"], "did:plc:z72i7hdynmk6r22z27h6tvur")

    def test_invalid_scheme(self):
        """Test that non-at:// schemes are blocked immediately."""
        uri = "https://did:plc:z72i7hdynmk6r22z27h6tvur/app.bsky.feed.post/3kzk"
        result = parser_b_atproto_custom(uri)
        self.assertFalse(result["success"])

    def test_mechanism_1_lossless_roundtrip(self):
        """Verify that encoding and decoding returns the exact same string."""
        original_uri = "at://did:plc:z72i7hdynmk6r22z27h6tvur/app.bsky.feed.post/3kzk"
        encoded = transform_mechanism_1_percent(original_uri, reverse=False)
        decoded = transform_mechanism_1_percent(encoded, reverse=True)
        self.assertEqual(original_uri, decoded)

if __name__ == "__main__":
    print("Running Extended Hackathon Test Suite...")
    unittest.main()