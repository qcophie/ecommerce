from .test_helper import TestSetUp
import pdb


class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        response = self.client.post(self.register_url)
        # pdb.set_trace()
        self.assertEqual(response.status_code, 400)

    def test_user_can_register_correctly(self):
        response = self.client.post(
            self.register_url, self.user_data, format="json")
        print(response.status_code)
        # self.assertEqual(response.data['user']['email'], self.user_data['email'])
        self.assertEqual(response.status_code, 200)
