import unittest

from app import app


class RouteTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_route_returns_hello_message(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "Hello, World!")

    def test_index_alias_returns_hello_message(self):
        response = self.client.get("/index")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "Hello, World!")

    def test_question_route_returns_placeholder_payload(self):
        response = self.client.get("/question/beginner")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {
                "question": None,
                "options": None,
                "optionCount": None,
                "xpOnSuccess": None,
            },
        )

    def test_question_route_rejects_non_get_requests(self):
        response = self.client.post("/question/beginner")

        self.assertEqual(response.status_code, 405)


if __name__ == "__main__":
    unittest.main()
