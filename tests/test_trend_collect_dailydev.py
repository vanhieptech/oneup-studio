# daily.dev fetcher in trend-collect.py (Bearer DAILY_DEV_TOKEN; no live API in tests).
import importlib.util, io, json, os, unittest, urllib.error
from unittest import mock

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = importlib.util.spec_from_file_location("trend_collect", os.path.join(R, "pipeline/scripts/trend-collect.py"))
tc = importlib.util.module_from_spec(s)
s.loader.exec_module(tc)


def _payload(n=2):
    return {
        "data": [
            {
                "id": f"p{i}",
                "title": f"Post {i} about shipping",
                "url": f"https://example.com/{i}",
                "summary": f"Summary {i}",
                "tags": ["ai", "devops"],
                "readTime": 5,
                "numUpvotes": 100 - i,
                "numComments": 10 + i,
                "publishedAt": "2026-11-28T10:00:00.000Z",
                "source": {"name": "Example", "handle": "example"},
            }
            for i in range(n)
        ],
        "pagination": {"hasNextPage": False, "cursor": None},
    }


class DailydevFetchTests(unittest.TestCase):
    def test_s_dailydev_popular_maps_fields(self):
        with mock.patch.object(tc.P, "tools_env", lambda k: "dda_test"), mock.patch.object(
            tc.urllib.request, "urlopen"
        ) as urlopen:
            body = json.dumps(_payload(2)).encode()
            resp = mock.MagicMock()
            resp.read.return_value = body
            resp.__enter__.return_value = resp
            resp.__exit__.return_value = False
            urlopen.return_value = resp
            items = tc.s_dailydev({"feed": "popular", "max": 10, "cat": "tech/AI", "lang": "en"})
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]["title"], "Post 0 about shipping")
        self.assertEqual(items[0]["url"], "https://example.com/0")
        self.assertEqual(items[0]["metric"]["upvotes"], 100)
        self.assertIn("ai", items[0]["summary"])
        req = urlopen.call_args[0][0]
        self.assertTrue(req.full_url.startswith("https://api.daily.dev/public/v1/feeds/popular"))
        self.assertEqual(req.get_header("Authorization"), "Bearer dda_test")

    def test_s_dailydev_tag_path_and_missing_token(self):
        with mock.patch.object(tc.P, "tools_env", lambda k: "dda_test"), mock.patch.object(
            tc.urllib.request, "urlopen"
        ) as urlopen:
            body = json.dumps(_payload(1)).encode()
            resp = mock.MagicMock()
            resp.read.return_value = body
            resp.__enter__.return_value = resp
            resp.__exit__.return_value = False
            urlopen.return_value = resp
            tc.s_dailydev({"feed": "tag", "tag": "webdev", "max": 5})
            self.assertIn("/feeds/tag/webdev", urlopen.call_args[0][0].full_url)
        with mock.patch.object(tc.P, "tools_env", lambda k: ""):
            with self.assertRaises(RuntimeError) as cm:
                tc.s_dailydev({"feed": "popular", "max": 1})
            self.assertIn("DAILY_DEV_TOKEN", str(cm.exception))

    def test_s_dailydev_http_error_surfaces_message(self):
        err = urllib.error.HTTPError(
            "https://api.daily.dev/public/v1/feeds/popular",
            429,
            "Too Many Requests",
            {},
            io.BytesIO(json.dumps({"message": "Quota exhausted"}).encode()),
        )
        with mock.patch.object(tc.P, "tools_env", lambda k: "dda_test"), mock.patch.object(
            tc.urllib.request, "urlopen", side_effect=err
        ):
            with self.assertRaises(RuntimeError) as cm:
                tc.s_dailydev({"feed": "popular", "max": 1})
            self.assertIn("429", str(cm.exception))
            self.assertIn("Quota", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
